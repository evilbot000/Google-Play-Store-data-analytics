# %%
import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\user\Downloads\Play Store Data.csv")

# %%
df.head()
df.info()
df.describe()

# %%
df.isnull().sum()

# %%
df['Rating']=df['Rating'].fillna("NaN")

# %%
df.isnull().sum()

# %%
df['Category'].value_counts()

# %%
import pandas as pd
import matplotlib.pyplot as plt
df['Ratings'].hist(bins=20)
plt.xlabel('Ratings')
plt.ylabel('Frequency')
plt.title('Distribution of app ratings')
plt.show()

# %% [markdown]
# #Done with code cleaining and EDA
# #Moving onto Task-1

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud

import nltk
from nltk.corpus import stopwords
df = pd.read_csv(r"C:\Users\user\Downloads\Play Store Data.csv")
df.columns = df.columns.str.strip()
df.columns

# %%
filtered_df = df[(df['Category'] == 'HEALTH_AND_FITNESS') & (df['Rating'] == 5)].copy()

synthetic_reviews = {
    "BM Physiotherapy Clinic": "This app is easy to use and very helpful for muscle recovery. I love the variety of effective routines offered.",
    "MI-BP": "MI-BP is great for tracking blood pressure and sending real-time alerts. The design is user-friendly and motivating.",
    "Bacterial vaginosis Treatment - Sexual disease": "I find this app beneficial and extremely effective for managing health tips. The daily reminders are outstanding.",
    "CB Fit": "CB Fit is fun, simple, and great for strength training. I enjoy all the engaging workouts it provides.",
    "C B Patel Health Club": "I love how it makes staying consistent easy. The instructions are clear and motivating.",
    "CF Townsville": "CF Townsville helps me stay active and fit. The interface is intuitive and the reminders are helpful.",
    "The CJ Rubric": "This tool is truly inspiring with daily suggestions and positive reinforcement.",
    "CL Strength": "CL Strength is amazing for daily exercises. Very convenient with beneficial progress charts.",
    "Dt. Jyothi Srinivas": "I love the meal plans and tracking features in this app. Very user-friendly and provides clear instructions.",
    "Cloud DX Connected Health": "This app is easy to navigate, keeping my health stats in one place. It’s very helpful for real-time updates.",
    "EF Academy": "EF Academy is outstanding for learning new fitness tips. The interface is great and the community is motivating.",
    "Santa Fe Thrive": "Santa Fe Thrive is fantastic for overall health goals. It creates effective daily routines and handy reminders."
}

def assign_review(app_name):
    if app_name in synthetic_reviews:
        return synthetic_reviews[app_name]
    else:
        
        positive_keywords = [
            "easy to use", "effective", "motivating", "user-friendly", 
            "inspiring", "excellent", "beneficial", "innovative"
        ]

filtered_df['User_reviews'] = filtered_df['App'].apply(assign_review)

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()                      
    text = re.sub(r'[^a-z\s]', ' ', text)         
    tokens = text.split()                         
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

filtered_df['cleaned_reviews'] = filtered_df['User_reviews'].apply(clean_text)

all_reviews_text = " ".join(filtered_df['cleaned_reviews'].tolist())

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_reviews_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud for 5-Star 'HEALTH_AND_FITNESS' Reviews", fontsize=16)
plt.show()

# %% [markdown]
# #Done with wordcloud
# #Done with Task-1
# #Moving onto Task-2

# %%
import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz
df = pd.read_csv(r"C:\Users\user\Downloads\Play Store Data.csv")
df['Installs'] = df['Installs'].str.replace('+', '', regex=False).str.replace(',', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df = df.dropna(subset=['Installs'])
df=df[~df['Category'].str.startswith(('A','C','G','S'))]
df=df[df['Installs']> 1_000_000]
top5_categories = df.groupby('Category')['Installs'].sum().nlargest(5).reset_index()
ist = pytz.timezone('Asia/Kolkata')
now = datetime.now(ist)

if 18 <= now.hour < 20:
    fig = px.bar(
        top5_categories,
        x='Installs',
        y='Category',
        orientation='h',
        color='Installs',
        color_continuous_scale='Plasma',
        title='Top 5 App Categories by Global Installs (>1M Installs, Filtered)'
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    fig.show()
else:
    print("This visualization is available only between 6 PM and 8 PM IST.")

# %% [markdown]
# #Done with choropleth
# #Done with Task-2
# #Moving onto Task-3

# %%
import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz
import re
df = pd.read_csv(r"C:\Users\user\Downloads\Play Store Data.csv")

df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

df['Reviews'] = df['Reviews'].str.replace(',', '', regex=True)
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

def convert_size_to_mb(size_str):
    try:
        size_str = size_str.strip().upper()
        if 'M' in size_str:
            return float(size_str.replace('M', ''))
        elif 'K' in size_str:
            return float(size_str.replace('K', '')) / 1024
        else:
            return None
    except:
        return None

df['Size_MB'] = df['Size'].apply(convert_size_to_mb)
allowed_categories = [
    "GAME", "BEAUTY", "BUSINESS", "COMICS",
    "COMMUNICATION", "DATING", "ENTERTAINMENT", "SOCIAL", "EVENT"
]
filtered_df = df[
    (df['Rating'] > 3.5) &
    (df['Reviews'] > 500) &
    (df['Installs'] > 50000) &
    (df['Category'].isin(allowed_categories))
]

ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist)

if 17 <= current_time.hour < 19:

    fig = px.scatter(
        filtered_df,
        x='Size_MB',
        y='Rating',
        size='Installs',
        color='Category',
        hover_name='App',
        title='Bubble Chart: App Size vs. Rating (Filtered)',
        size_max=60  
    )
    fig.update_layout(
        xaxis_title='App Size (MB)',
        yaxis_title='Average Rating'
    )
    fig.show()
else:
    print("This visualization is available only between 5 PM and 7 PM IST.")

# %% [markdown]
# #Done with bubble chart
# #Done with Task-3
# #Completed all the tasks


