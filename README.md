# Google-Play-Store-data-analytics

Overview
This project is developed as part of the NullClass Internship and focuses on analyzing data from the Google Play Store using Python. The project contains three main analytics tasks implemented using Python, Pandas, Plotly, and other data visualization libraries.

The goal is to uncover insights from app data such as installs, ratings, reviews, and sizes through visualizations, with certain conditional behaviors like time-based chart rendering.

  Tasks Implemented
Task 1: Word Cloud for 5-Star Reviews in Health & Fitness
Filters 5-star reviews in the “HEALTH_AND_FITNESS” category.

Extracts and cleans text data.

Generates a word cloud to visualize the most frequent words.

Task 2: Interactive Choropleth Map (Bar Chart as Alternative)
Filters app categories with over 1 million installs.

Excludes categories starting with A, C, G, or S.

Renders an interactive bar chart (as country-level mapping is unavailable).

Chart is displayed only between 6:00 PM and 8:00 PM IST.

Task 3: Bubble Chart for App Size vs. Ratings
Filters apps with:

Rating > 3.5

Category ∈ {"GAME", "BEAUTY", "BUSINESS", "COMICS", "COMMUNICATION", "DATING", "ENTERTAINMENT", "SOCIAL", "EVENT"}

Reviews > 500

Installs > 50,000

Creates a bubble chart where:

X-axis: App Size (MB)

Y-axis: Rating

Bubble size: Number of installs

Chart is shown only between 5:00 PM and 7:00 PM IST.

Required Libraries
Library              	Purpose
pandas	              Data loading and manipulation
matplotlib	          Visualization (used in word cloud rendering)
wordcloud	            Generating word cloud
plotly	              Interactive visualizations
datetime	            Time-based chart rendering

Time-Based Behavior
This project introduces time-aware visualizations using the datetime library, based on Indian Standard Time (IST):

Task 2 (Choropleth/Bar Chart):

Chart is displayed only between 6 PM and 8 PM IST.

Outside that window, a message is shown:
“This chart is viewable only between 6 PM to 8 PM IST.”

Task 3 (Bubble Chart):

Chart is displayed only between 5 PM and 7 PM IST.

Outside that window, a message is shown:
“This chart is viewable only between 5 PM to 7 PM IST.”

This simulates real-time conditional rendering based on business logic or user interaction timing.


