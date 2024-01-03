import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
file_path = r"C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Rhino\Customer Churn\Csutomer Churn\customer_churn_dataset-testing-master.csv"
df = pd.read_csv(file_path)

# Replace 'Quarterly' in 'Subscription Type' with a numerical value (e.g., 3 for three months)
df['Subscription Type'] = df['Subscription Type'].replace('Quarterly', 3)

# Display basic information about the dataset
print('Dataset Information')
print(df.info())

# Data types of each column in the dataframe
print('\nData types of each column in the dataframe:')
print(df.dtypes)

# Total Customers by Gender
gender_counts = df['Gender'].value_counts()
print('\nTotal Customers by Gender:')
print(gender_counts)

# Total Counting Churned Customers vs Retained Customers
churned_count = df[df['Churn'] == 1].shape[0]
retained_count = df[df['Churn'] == 0].shape[0]

print("\nNumber of churned customers: ", churned_count)
print("Number of retained customers: ", retained_count)

# Visualizing the churn distribution
sns.countplot(x='Churn', data=df)
plt.title('Churn Distribution')
plt.show()

# Exploratory Data Analysis (EDA)

# Distribution of SeniorCitizen, Partner, and Dependents
categorical_columns = ['SeniorCitizen', 'Partner', 'Dependents']

for column in categorical_columns:
    if column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, hue='Churn', data=df)
        plt.title(f'{column} Distribution by Churn')
        plt.show()
    else:
        print(f"Column '{column}' not found in the dataset.")

# Distribution of numerical variables
numerical_columns = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 'Payment Delay', 'Contract Length', 'Total Spend']

for column in numerical_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=30, kde=True)
    plt.title(f'{column} Distribution')
    plt.show()

# Correlation Analysis
numeric_columns = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_columns].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix')
plt.show()

# Customer Churn by Contract Type
plt.figure(figsize=(10, 6))
sns.countplot(x='Subscription Type', hue='Churn', data=df)
plt.title('Churn by Subscription Type')
plt.show()

# Customer Churn by Payment Method
plt.figure(figsize=(10, 6))
sns.countplot(x='Payment Delay', hue='Churn', data=df)
plt.title('Churn by Payment Delay')
plt.show()

# Customer Churn by Monthly Charges
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Total Spend', y='Usage Frequency', hue='Churn', data=df)
plt.title('Churn by Total Spend and Usage Frequency')
plt.show()

# Customer Churn by Tenure
plt.figure(figsize=(10, 6))
sns.boxplot(x='Churn', y='Tenure', data=df)
plt.title('Churn by Tenure')
plt.show()

