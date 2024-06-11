import os
os.environ['LOKY_MAX_CPU_COUNT'] = '4'  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, mean_squared_error
from imblearn.over_sampling import SMOTE

# Function to load and display dataset information
def load_data(fraud):
    # Loading the dataset
    data = pd.read_csv(fraud)
    
    # Displaying the first few rows of the dataset
    print('Dataset Head')
    print(data.head())
    
    # Basic information about the dataset
    print('Dataset Information')
    print(data.info())
    
    # Summary statistics of the dataset
    print('Dataset Summary')
    print(data.describe())
    
    # Checking for missing values
    missing_values = data.isnull().sum()
    print('Missing Values:')
    print(missing_values)
    
    return data

# Function for Exploratory Data Analysis (EDA)
def perform_eda(data):
    # Distribution of the transaction amount
    plt.figure(figsize=(10, 5))
    sns.histplot(data['Amount'], bins=50, kde=True)
    plt.title('Distribution of Transaction Amount')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.show()

    # Distribution of the class variable
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Class', data=data)
    plt.title('Distribution of Fraudulent (1) vs Non-Fraudulent (0) Transactions')
    plt.xlabel('Class')
    plt.ylabel('Count')
    plt.show()

    # Boxplot of transaction amount by class
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='Class', y='Amount', data=data)
    plt.title('Transaction Amount by Class')
    plt.xlabel('Class')
    plt.ylabel('Amount')
    plt.show()

    # Computing the correlation matrix
    corr_matrix = data.corr()

    # Displaying the heatmap of the correlation matrix
    plt.figure(figsize=(15, 10))
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix of Features')
    plt.show()

# Function for feature normalization
def normalize_features(data):
    # Normalising the 'Amount' feature
    scaler = StandardScaler()
    data['Amount'] = scaler.fit_transform(data[['Amount']])
    return data

# Function to split dataset into training and testing sets
def split_data(data):
    # Separating features and target variable
    X = data.drop(columns=['id', 'Class'])
    y = data['Class']

    # Splitting the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    return X_train, X_test, y_train, y_test

# Function to handle class imbalance using SMOTE
def balance_data(X_train, y_train):
    # Apply SMOTE to the training data
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    return X_train_resampled, y_train_resampled

# Function to train and evaluate the logistic regression model
def train_and_evaluate_model(X_train_resampled, y_train_resampled, X_test, y_test):
    # Training a logistic regression model
    model = LogisticRegression(random_state=42)
    model.fit(X_train_resampled, y_train_resampled)

    # Predicting on the test set
    y_pred = model.predict(X_test)

    # Evaluating the model
    print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("ROC AUC Score:\n", roc_auc_score(y_test, y_pred))

    # Calculating RMSE
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error (RMSE):", rmse)

# Main function to execute the workflow
def main():
    # Path to the dataset
    fraud = r"C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Fraud Detection\creditcard_2023.csv"
    
    # Loading and displaying dataset information
    data = load_data(fraud)
    
    # Performing Exploratory Data Analysis (EDA)
    perform_eda(data)
    
    # Normalising features
    data = normalize_features(data)
    
    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(data)
    
    # Handling class imbalance using SMOTE
    X_train_resampled, y_train_resampled = balance_data(X_train, y_train)
    
    # Training and evaluateing the model
    train_and_evaluate_model(X_train_resampled, y_train_resampled, X_test, y_test)

    # Saving processed data for Tableau
    data.to_excel('processed_creditcard_data.xlsx', index=False)
    print("Processed data saved to 'processed_creditcard_data.xlsx'")

# Execute the main function
if __name__ == "__main__":
    main()
