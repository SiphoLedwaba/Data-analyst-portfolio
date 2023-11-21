import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # For boxplot

# Load the data
file_path = r'C:\Users\Snipes\Downloads\m2_survey_data.csv'
survey_data = pd.read_csv(file_path)

# What is the median ConvertedComp before removing outliers?
median_comp_before = survey_data['ConvertedComp'].median()
print(f"The median ConvertedComp before removing outliers is: {median_comp_before}")

# Define a function to remove outliers based on IQR (Interquartile Range)
def remove_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# What is the median ConvertedComp after removing outliers?
survey_data_no_outliers = remove_outliers(survey_data, 'ConvertedComp')
median_comp_after = survey_data_no_outliers['ConvertedComp'].median()
print(f"The median ConvertedComp after removing outliers is: {median_comp_after}")

# Boxplot for 'Age' to identify outliers
plt.figure(figsize=(8, 6))
sns.boxplot(x='Age', data=survey_data)
plt.title('Boxplot of Age with Outliers')
plt.show()

# Count outliers below Q1 for 'Age'
Q1 = survey_data['Age'].quantile(0.25)
Q3 = survey_data['Age'].quantile(0.75)  # Add this line to define Q3
outliers_below_Q1 = survey_data[survey_data['Age'] < Q1 - 1.5 * (Q3 - Q1)]
num_outliers_below_Q1 = len(outliers_below_Q1)
print(f"The number of outliers below Q1 for 'Age' is: {num_outliers_below_Q1}")

# Calculate the mean ConvertedComp after removing outliers
mean_comp_after = survey_data_no_outliers['ConvertedComp'].mean()
print(f"The mean ConvertedComp after removing outliers is: {mean_comp_after}")

# Identify non-numeric columns
non_numeric_columns = survey_data.select_dtypes(exclude=['float64', 'int64']).columns

# Drop non-numeric columns from the dataset
numeric_data = survey_data.drop(columns=non_numeric_columns)

# Calculate correlations with "Age"
correlations = numeric_data.corr()['Age']

# Find the column with the highest positive correlation
highest_corr_column = correlations.idxmax()
highest_corr_value = correlations.max()
print(f"The column with the highest positive correlation with 'Age' is '{highest_corr_column}' with a correlation value of {highest_corr_value}")

# Find the column with the highest negative correlation
lowest_corr_column = correlations.idxmin()
lowest_corr_value = correlations.min()
print(f"The column with the highest negative correlation with 'Age' is '{lowest_corr_column}' with a correlation value of {lowest_corr_value}")