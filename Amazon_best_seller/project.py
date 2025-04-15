# -------- STEP 1: Import Libraries --------
import pandas as pd
import numpy as np
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt

# -------- STEP 2: Load and Preview CSV --------
try:
    df = pd.read_csv('data/best_sellers_data2.csv')
    print("CSV loaded successfully!")
except FileNotFoundError:
    print(" CSV file not found. Please check the path.")
    exit()

# Print actual column names to debug
print(" Original Columns:", df.columns.tolist())

# -------- STEP 3: Clean & Normalize Columns --------
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df.rename(columns={
    'product_price': 'price',
    'product_star_rating': 'rating',
    'product_num_ratings': 'reviews',
    'product_title': 'name',
    'rank': 'rank',
    'country': 'country'
}, inplace=True)

print("Normalized Columns:", df.columns.tolist())

# -------- STEP 4: Clean Data --------
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Clean price column
if 'price' in df.columns:
    df['price'] = df['price'].astype(str)
    df['price'] = df['price'].replace(r'[^\d.]', '', regex=True).replace('', '0').astype(float)
else:
    print("'price' column not found.")
    exit()

# Clean rating column
if 'rating' in df.columns:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
else:
    print(" 'rating' column not found.")
    exit()

# Clean reviews column
if 'reviews' in df.columns:
    df['reviews'] = df['reviews'].replace('[,]', '', regex=True).astype(int)
else:
    print(" 'reviews' column not found.")
    exit()

# -------- STEP 5: Analytical Computation --------
df['price_type'] = df['price'].apply(lambda x: 'Free' if x == 0 else 'Paid')

# -------- STEP 6: Console Output --------
print("\nTop 10 Best-Selling Software by Rating:")
print(df.sort_values(by='rating', ascending=False)[['name', 'rating', 'reviews', 'price']].head(10))

# Check if 'category' column exists
if 'category' in df.columns:
    print("\nAverage Price of Software per Category:")
    print(df.groupby('category')['price'].mean().sort_values(ascending=False))
else:
    print("\nNo 'category' column found. Analyzing by 'country' instead:")
    print(df.groupby('country')['price'].mean().sort_values(ascending=False))

# Pricing trend summary
print("\nPricing Trend Summary:")
print(f"Min Price: {df['price'].min():.2f}")
print(f"Max Price: {df['price'].max():.2f}")
print(f"Average Price: {df['price'].mean():.2f}")
print(f"Median Price: {df['price'].median():.2f}")

# Most Reviewed Software (Grouped by Country)
print("\nMost Reviewed Software Categories (Grouped by Country):")
print(df.groupby('country')['reviews'].sum().sort_values(ascending=False))

# Average Rating and Reviews per Country
print("\nAverage Rating and Reviews per Country:")
print(df.groupby('country')[['rating', 'reviews']].mean().sort_values(by='rating', ascending=False))

# Free vs Paid Software Performance (Avg Rating & Reviews)
print("\nFree vs Paid Software Performance (Avg Rating & Reviews):")
print(df.groupby('price_type')[['rating', 'reviews']].mean())

# -------- STEP 7: Visualizations --------
# Rating vs Review Count
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='reviews', y='rating', hue='price_type', alpha=0.7)
plt.title('Rating vs Review Count')
plt.xlabel('Number of Reviews')
plt.ylabel('Star Rating')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------- STEP 8: Save Cleaned Data (Optional) --------
df.to_csv('cleaned_best_sellers.csv', index=False)
print("Cleaned data saved as 'cleaned_best_sellers.csv'")


# -------- STEP 9: SQL Database Insertion --------
# MySQL connection setup
db_config = {
    'host': 'localhost',       
    'user': 'root',              
    'password': 'mohit123',      
    'database': 'best_sellers'  
}

# Connect to MySQL
db_config_no_db = db_config.copy()
db_config_no_db.pop('database', None)  

# Connect without a specific DB to create one
conn = mysql.connector.connect(**db_config_no_db)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS best_sellers")
cursor.execute("USE best_sellers")

# Create table with modified column name to avoid using 'rank'
cursor.execute("""
CREATE TABLE IF NOT EXISTS software_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price FLOAT,
    rating FLOAT,
    reviews INT,
    software_rank INT,  -- Changed 'rank' to 'software_rank'
    country VARCHAR(100),
    price_type VARCHAR(10)
);
""")

print("Table 'software_data' created or already exists.")

# Insert data into the database

insert_query = """
    INSERT INTO software_data (name, price, rating, reviews, software_rank, country, price_type)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

# Commit the transaction
conn.commit()
print("Data inserted into MySQL database successfully!")


