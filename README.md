# 📱 Mobile Banking Review Analysis - Omega Consultancy

Omega Consultancy supports banks in enhancing their mobile apps by analyzing user feedback to improve customer retention and satisfaction. This project focuses on scraping, cleaning, and preparing review data from the Google Play Store.

---

## Objectives

- Scrape user reviews from Google Play Store for selected banking apps.

- Preprocess and clean review data.

- Perform sentiment and thematic analysis to uncover user satisfaction drivers and pain points.

- Standardize and store structured review data for further analysis and reporting.
---

##  Methodology

### 1. Scraping Reviews

Using `scraper.py`, fetch up to 400 reviews per app. Each review contains:

- Review Text
- Rating (1–5)
- Date
- Bank/App Name
- Source: Google Play

### 2. Preprocessing 

Using `preprocess.py`, clean data and save as cleaned dataset. Cleaning includes:

- Remove duplicates
- Handle missing values
- Normalize dates to YYYY-MM-DD
- Standardize columns:
review, rating, date, bank, source

3. Sentiment Analysis

- Implemented sentiment classification using VADER (for faster runtime compared to transformer-based models).

- Classified each review as Positive, Negative, or Neutral.

- Aggregated sentiment distributions by bank and rating level.

4. Thematic Analysis

- Extracted top keywords and n-grams using TF-IDF.

- Applied topic modeling (LDA) to identify coherent themes from reviews.

- Grouped keywords into 5 core themes:

User Interface & Experience: e.g., easy, simple

Transaction Performance

Account Access Issues

Feature Requests: e.g., update

Customer Support
---

## Tools Used

* google-play-scraper: For app review extraction
* pandas: Data manipulation and preprocessing
* nltk, vaderSentiment: For sentiment scoring
* scikit-learn, spaCy: For TF-IDF, topic modeling
* Jupyter Notebooks: Interactive data exploration
* Python 3.10+



