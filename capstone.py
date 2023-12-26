# Step 1: Imports and Data Loading
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# Load dataset
file_path = r"C:\Users\Snipes\OneDrive\Documents\Work\Projects\waze\Files (2)\Files\home\jovyan\work\HR_capstone_dataset.csv"
df = pd.read_csv(file_path)

# Rename columns
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Check for missing values
missing_values = df.isnull().sum()

# Check for duplicates
duplicates = df.duplicated().sum()

# Check outliers (boxplot)
sns.boxplot(x=df['time_spend_company'])
plt.show()

# Step 2: Data Exploration (Continued)
# Employee Turnover Analysis
num_left = df['left'].sum()
num_stayed = df['left'].count() - num_left
percent_left = (num_left / df['left'].count()) * 100
percent_stayed = 100 - percent_left

# Data Visualizations
sns.pairplot(df, hue='left', diag_kind='kde')
plt.show()

# Step 3: Model Building
# Encode categorical variables
X_encoded = pd.get_dummies(df, columns=['department'], drop_first=True)
X_encoded['salary'] = X_encoded['salary'].map({'low': 0, 'medium': 1, 'high': 2})

# Define features and target
X = X_encoded.drop('left', axis=1)
y = X_encoded['left']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Model Interpretation and Results
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
print(f"ROC AUC: {roc_auc}")
print(f"Confusion Matrix:\n{conf_matrix}")
