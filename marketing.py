import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Marketing_Analytics\ifood_df.csv")

# df information
print('Dataset Information')
print(df.info())

# dataset head
print('Few rows of data')
print(df.head())

# basic summary statistics
print('Summary statistics of the dataset')
print(df.describe())

# data cleaning and feature engineering
df['MntTotal'] = df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)
df['TotalPurchases'] = df[['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1)
df['AcceptedCmpOverall'] = df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']].sum(axis=1)

# handling missing values if there are any
df = df.fillna(df.mean())

# combining marital status columns into a single column
df['Marital_Status'] = df[['marital_Divorced', 'marital_Married', 'marital_Single', 'marital_Together', 'marital_Widow']].idxmax(axis=1).str.replace('marital_', '')

# combining education level columns into a single column
df['Education'] = df[['education_2n Cycle', 'education_Basic', 'education_Graduation', 'education_Master', 'education_PhD']].idxmax(axis=1).str.replace('education_', '')

# converting categorical columns to numeric codes
df['Marital_Status_Code'] = df['Marital_Status'].astype('category').cat.codes
df['Education_Code'] = df['Education'].astype('category').cat.codes

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(10, 6))
sns.histplot(df['Income'], kde=True, color='darkorange')
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Marital_Status', y='MntTotal', data=df, palette='viridis')
plt.title('Total Amount Spent by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Total Amount Spent')
plt.show()

# Total Purchases by Education Level
plt.figure(figsize=(10, 6))
sns.boxplot(x='Education', y='TotalPurchases', data=df, palette='coolwarm')
plt.title('Total Purchases by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Total Purchases')
plt.show()

# Correlation Matrix
plt.figure(figsize=(15, 10))

# selecting only numeric columns for correlation matrix
numeric_cols = df.select_dtypes(include=[int, float]).columns
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt='.2f', cmap='Spectral')
plt.title('Correlation Matrix')
plt.show()

# Acceptance of Campaigns
campaigns = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']
accepted_counts = df[campaigns].sum().reset_index()
accepted_counts.columns = ['Campaign', 'Count']

plt.figure(figsize=(10, 6))
sns.barplot(x='Campaign', y='Count', data=accepted_counts, palette='Set2')
plt.title('Number of Accepted Campaigns')
plt.xlabel('Campaign')
plt.ylabel('Count')
plt.show()

# Complaints vs. Total Amount Spent
plt.figure(figsize=(10, 6))
sns.boxplot(x='Complain', y='MntTotal', data=df, palette='rocket')
plt.title('Total Amount Spent vs. Complaints')
plt.xlabel('Complaints')
plt.ylabel('Total Amount Spent')
plt.show()

# Average spending based on the number of accepted campaigns
plt.figure(figsize=(10, 6))
sns.barplot(x='AcceptedCmpOverall', y='MntTotal', data=df, estimator=lambda x: sum(x) / len(x), palette='cubehelix')
plt.title('Average Spending Based on Number of Accepted Campaigns')
plt.xlabel('Number of Accepted Campaigns')
plt.ylabel('Average Spending')
plt.show()

# saving the processed dataset to a new Excel file
output_path = r'C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Marketing_Analytics\processed_marketing_dataset.xlsx'
df.to_excel(output_path, index=False)

print(f"\nProcessed dataset saved to {output_path}")
