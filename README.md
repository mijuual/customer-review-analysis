# 📱 Mobile Banking Review Analysis - Omega Consultancy

Omega Consultancy supports banks in enhancing their mobile apps by analyzing user feedback to improve customer retention and satisfaction. This project focuses on scraping, cleaning, and preparing review data from the Google Play Store.

---

## Objectives

- Scrape user reviews from Google Play Store for selected banking apps.
- Preprocess and clean review data.
- Standardize and store structured review data for further analysis.

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

## Tools Used

- `google-play-scraper`: To collect app reviews
- `pandas`: Data manipulation and preprocessing
- `Jupyter Notebooks`: For interactive analysis
- `Python 3.10+`


