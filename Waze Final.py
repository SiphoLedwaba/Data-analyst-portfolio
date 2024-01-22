# Import packages for data manipulation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import make_scorer, recall_score, precision_score, f1_score
from sklearn.model_selection import GridSearchCV
import joblib

#This lets us see all the columns, preventing Jupyter from redacting them.
pd.set_option('display.max_columns', None)

#This is the function that helps plot feature importance
def plot_feature_importance(importance, names, model_type='Random Forest'):
    feature_importance = np.array(importance)
    feature_names = np.array(names)

    data = {'feature_names': feature_names, 'feature_importance': feature_importance}
    fi_df = pd.DataFrame(data)

    fi_df.sort_values(by=['feature_importance'], ascending=False, inplace=True)

    plt.figure(figsize=(10, 8))
    sns.barplot(x=fi_df['feature_importance'], y=fi_df['feature_names'])
    plt.title(model_type + ' - Feature Importance')
    plt.xlabel('Feature Importance')
    plt.ylabel('Feature Names')

#Import dataset
file_path = "C:\\Users\\Snipes\\OneDrive\\Documents\\DA Portfolio-20230122T081035Z-001\\DA Portfolio\\Waze\\waze\\Waze Lab 5\\Files\\home\\jovyan\\work\\waze_dataset.csv"
df = pd.read_csv(file_path)

#Inspecting the first five rows
print(df.head())

#Copying the df dataframe
df_copy = df.copy()

print("Columns with NaN values:")
print(df.columns[df.isnull().any()])


# 1. Creating `km_per_driving_day` feature
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']

# 2. Getting descriptive stats
print("Descriptive Stats for km_per_driving_day:")
print(df['km_per_driving_day'].describe())


# 1. Converting infinite values to zero
df.replace([np.inf, -np.inf], 0, inplace=True)

# 2. Confirming that it worked
infinite_values_check = df[df['km_per_driving_day'].isin([np.inf, -np.inf])]
print("Number of infinite values after replacement:", len(infinite_values_check))

# 1. Creating `percent_sessions_in_last_month` feature
df['percent_sessions_in_last_month'] = (df['sessions'] / df['total_sessions']) * 100

# 2. Getting descriptive stats
percent_sessions_stats = df['percent_sessions_in_last_month'].describe()
print(percent_sessions_stats)

# Creating `professional_driver` feature
df['professional_driver'] = np.where((df['drives'] >= 60) & (df['driving_days'] >= 15), 1, 0)

# Creating `total_sessions_per_day` feature
df['total_sessions_per_day'] = df['total_sessions'] / df['n_days_after_onboarding']

# Getting descriptive stats for `total_sessions_per_day`
total_sessions_per_day_stats = df['total_sessions_per_day'].describe()
print(total_sessions_per_day_stats)

# 1. Creating `km_per_driving_day` feature
df['km_per_driving_day'] = df['driven_km_drives'] / np.where(df['driving_days'] == 0, 1, df['driving_days'])

# 1. Creating `percent_sessions_in_last_month` feature
df['percent_sessions_in_last_month'] = np.where(df['total_sessions'] == 0, 0, (df['sessions'] / df['total_sessions']) * 100)

# Creating `km_per_hour` feature
df['km_per_hour'] = df['driven_km_drives'] / (df['duration_minutes_drives'] / 60)

# Creating a column representing each user's mean number of kilometers per drive made in the last month.
# Then, print descriptive statistics for the feature.
df['km_per_drive'] = df['driven_km_drives'] / df['drives']

# 1. Converting infinite values to zero
df.replace([np.inf, -np.inf], 0, inplace=True)

# 2. Confirming that it worked
infinite_values_check_km_per_drive = df[df['km_per_drive'].isin([np.inf, -np.inf])]
print("Number of infinite values after replacement:", len(infinite_values_check_km_per_drive))

# Printing descriptive statistics for `km_per_drive`
km_per_drive_stats = df['km_per_drive'].describe()
print(km_per_drive_stats)

# Creating `percent_of_sessions_to_favorite` feature
df['percent_of_sessions_to_favorite'] = (df['total_navigations_fav1'] + df['total_navigations_fav2']) / df['total_sessions'] * 100

# Getting descriptive stats for `percent_of_sessions_to_favorite`
percent_of_sessions_to_favorite_stats = df['percent_of_sessions_to_favorite'].describe()
print(percent_of_sessions_to_favorite_stats)

# Dropping rows with missing values
df.dropna(inplace=True)

# Creating new `device2` variable
df['device2'] = df['device'].map({'Android': 0, 'iPhone': 1})

# Creating binary `label2` column
df['label2'] = np.where(df['label'] == 'retained', 0, 1)

# Dropping `ID` column
df.drop('ID', axis=1, inplace=True)

# Getting class balance of 'label2' col
class_balance = df['label2'].value_counts()
print(class_balance)

# Function to get test scores
def get_test_scores(model_name, predictions, true_labels):
    accuracy = accuracy_score(true_labels, predictions)
    precision = precision_score(true_labels, predictions)
    recall = recall_score(true_labels, predictions)
    f1 = f1_score(true_labels, predictions)

    results_table = pd.DataFrame({
        'Model': [model_name],
        'Precision': [precision],
        'Recall': [recall],
        'F1 Score': [f1],
        'Accuracy': [accuracy]
    })

    return results_table

# Splitting the data into train, validation, and test sets
X = df.drop(['label', 'device', 'device2', 'label2'], axis=1)
y = df['label2']

X_train_interim, X_test, y_train_interim, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train_interim, y_train_interim, test_size=0.25, stratify=y_train_interim, random_state=42)

print("Training set samples:", len(X_train))
print("Validation set samples:", len(X_val))
print("Test set samples:", len(X_test))

# Random Forest Model
rf = RandomForestClassifier(random_state=42)
cv_params = {
    'max_depth': [None, 10, 20, 30],
    'max_features': ['auto', 'sqrt', 'log2'],
    'min_samples_leaf': [1, 2, 4],
    'min_samples_split': [2, 5, 10],
    'n_estimators': [50, 100, 200, 300]
}
scoring = {
    'precision': make_scorer(precision_score),
    'recall': make_scorer(recall_score),
    'f1': make_scorer(f1_score),
    'accuracy': make_scorer(accuracy_score)
}
rf_cv = GridSearchCV(estimator=rf, param_grid=cv_params, scoring=scoring, cv=5, refit='recall')
rf_cv.fit(X_train, y_train)

best_recall_score = rf_cv.best_score_
print(f"Best Average Recall Score (Random Forest): {best_recall_score:.4f}")

best_params = rf_cv.best_params_
print("Best Hyperparameter Combination (Random Forest):")
print(best_params)

# XGBoost Model
import xgboost as xgb
xgb_model = xgb.XGBClassifier(objective='binary:logistic', random_state=42)
xgb_params = {
    'max_depth': [3, 5, 7],
    'min_child_weight': [1, 3, 5],
    'learning_rate': [0.1, 0.01, 0.001],
    'n_estimators': [50, 100, 200]
}
xgb_scoring = {
    'precision': make_scorer(precision_score),
    'recall': make_scorer(recall_score),
    'f1': make_scorer(f1_score),
    'accuracy': make_scorer(accuracy_score)
}
xgb_cv = GridSearchCV(estimator=xgb_model, param_grid=xgb_params, scoring=xgb_scoring, cv=5, refit='recall')
xgb_cv.fit(X_train, y_train)

best_recall_score_xgb = xgb_cv.best_score_
print(f"Best Average Recall Score (XGBoost): {best_recall_score_xgb:.4f}")

best_params_xgb = xgb_cv.best_params_
print("Best Hyperparameter Combination (XGBoost):")
print(best_params_xgb)

# Function to make results table
def make_results(model_name, model_object, metric):
    metric_mapping = {
        'precision': 'mean_test_precision',
        'recall': 'mean_test_recall',
        'f1': 'mean_test_f1',
        'accuracy': 'mean_test_accuracy'
    }

    results_df = pd.DataFrame(model_object.cv_results_)
    best_metric_row = results_df.loc[results_df[metric_mapping[metric]].idxmax()]
    accuracy = best_metric_row['mean_test_accuracy']
    precision = best_metric_row['mean_test_precision']
    recall = best_metric_row['mean_test_recall']
    f1 = best_metric_row['mean_test_f1']

    results_table = pd.DataFrame({
        'Model': [model_name],
        'Precision': [precision],
        'Recall': [recall],
        'F1 Score': [f1],
        'Accuracy': [accuracy]
    })

    return results_table

# Results for Random Forest
results_table_rf = make_results('Random Forest', rf_cv, 'recall')

# Results for XGBoost
results_table_xgb = make_results('XGBoost', xgb_cv, 'recall')

# Displaying the results
print(results_table_rf)
print(results_table_xgb)

# Using random forest model to predict on validation data
rf_val_preds = rf_cv.predict(X_val)

# Getting validation scores for RF model
results_table_rf_val = get_test_scores('Random Forest (Validation)', rf_val_preds, y_val)

# Appending to the results table
results_table_rf = pd.concat([results_table_rf, results_table_rf_val], ignore_index=True)

# Using XGBoost model to predict on validation data
xgb_val_preds = xgb_cv.predict(X_val)

# Getting validation scores for XGBoost model
results_table_xgb_val = get_test_scores('XGBoost (Validation)', xgb_val_preds, y_val)

# Append to the results table
results_table_xgb = pd.concat([results_table_xgb, results_table_xgb_val], ignore_index=True)

# Using XGBoost model to predict on test data
xgb_test_preds = xgb_cv.predict(X_test)

# Getting test scores for XGBoost model
results_table_xgb_test = get_test_scores('XGBoost (Test)', xgb_test_preds, y_test)

# Appending to the results table
results_table_xgb = pd.concat([results_table_xgb, results_table_xgb_test], ignore_index=True)

# Displaying final results
print(results_table_rf)
print(results_table_xgb)

# Generating array of values for confusion matrix
cm_values_xgb = confusion_matrix(y_test, xgb_test_preds)

# Plotting confusion matrix for XGBoost model
plot_confusion_matrix(xgb_cv, X_test, y_test, cmap='Blues', values_format='d')
plt.title('Confusion Matrix - XGBoost (Test)')
plt.show()

# Using the plot_importance function to inspect the most important features of your final model.
xgb.plot_importance(xgb_cv.best_estimator_, importance_type='weight', title='Feature Importance - XGBoost')
plt.show()
