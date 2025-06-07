import pandas as pd
import os

def preprocess_reviews(input_path, output_path):
    # Load raw data
    df = pd.read_csv(input_path)
    print(f"Initial rows loaded: {len(df)}")

    # Drop rows with missing values in key columns
    df = df.dropna(subset=["Review Text", "Rating", "Date", "Bank/App Name", "Source"])
    print(f"Rows after dropping missing values: {len(df)}")

    # Drop duplicates
    df = df.drop_duplicates()
    print(f"Rows after dropping duplicates: {len(df)}")

    # Normalize date
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m-%d')

    # Rename columns to standard schema
    df_cleaned = df.rename(columns={
        "Review Text": "review",
        "Rating": "rating",
        "Date": "date",
        "Bank/App Name": "bank",
        "Source": "source"
    })

    # Save cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_cleaned.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    print(f"Final row count: {len(df_cleaned)}")
