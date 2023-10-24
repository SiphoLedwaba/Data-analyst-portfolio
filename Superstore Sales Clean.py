import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load the dataset
df = pd.read_excel('Superstore_Sales_Raw.xlsx')

# Clean data (e.g., remove rows with missing values)
columns_to_remove = ['Year ID', 'Count Customers - CY', 'Sales (CY)', 'Sales - <K', 'Sales - K', 'Sales - M', 'Sales per Customer CY']
df_cleaned = df.drop(columns=columns_to_remove)

# Remove '$' from relevant columns
columns_with_dollar = ['Sales', 'Sales - Boost']
df_cleaned[columns_with_dollar] = df_cleaned[columns_with_dollar].replace('[\$,]', '', regex=True).astype(float)

# Summary statistics for numerical columns
numeric_columns = ['Sales', 'Sales - Boost']
numeric_summary = df_cleaned[numeric_columns].describe()

print("Summary Statistics for Numeric Columns:")
print(numeric_summary)

# Count occurrences of string values in specified columns
text_columns = ['Segment', 'Category', 'Region', 'Category Filter', 'City', 'Ship Mode', 'State', 'Sub-Category', 'Customer Name']
word_counts = {col: Counter(df_cleaned[col].astype(str)) for col in text_columns}

# Print the most common words for each column
for col, word_count in word_counts.items():
    print(f"Most common words in {col}:")
    for word, count in word_count.most_common(10):  # Change 10 to show a different number of top words
        print(f"{word}: {count} times")
    print()

# Visualize category distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cleaned, x='Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Distribution of Categories')
plt.show()

# Visualize sales distribution
plt.hist(df_cleaned['Sales'], bins=20)
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Sales Distribution')
plt.show()

# Visualize sales boost distribution
plt.hist(df_cleaned['Sales - Boost'], bins=20, color='orange')
plt.xlabel('Sales - Boost')
plt.ylabel('Frequency')
plt.title('Sales - Boost Distribution')
plt.show()

# Visualize subcategory breakdown
plt.figure(figsize=(12, 6))
sns.countplot(data=df_cleaned, y='Sub-Category')
plt.ylabel('Sub-Category')
plt.xlabel('Count')
plt.title('Distribution of Sub-Categories')
plt.show()

# Visualize customer count by state
plt.figure(figsize=(12, 6))
sns.countplot(data=df_cleaned, x='State')
plt.xlabel('State')
plt.ylabel('Customer Count')
plt.title('Customer Count by State')
plt.xticks(rotation=45)
plt.show()

# Export script as an Excel file
df_cleaned.to_excel('Superstore_Sales_Cleaned.xlsx', index=False)
