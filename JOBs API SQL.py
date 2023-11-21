import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Open a database connection
conn = sqlite3.connect("m4_survey_data.sqlite")

# Query to get the column names in the table 'master'
QUERY = """
PRAGMA table_info('master')
"""

# The read_sql_query runs the SQL query and returns the data as a DataFrame
column_info_df = pd.read_sql_query(QUERY, conn)

# Print the column names and their details
print(column_info_df)

# Print how many rows are there in the table named 'master'
QUERY = """
SELECT COUNT(*)
FROM master
"""

# Print the column names
column_names = column_info_df['name'].tolist()
print("All Columns in 'master' table:")
print(column_names)

# The read_sql_query runs the SQL query and returns the data as a DataFrame
df = pd.read_sql_query(QUERY, conn)
print(df.head())

# Query to count the number of records for each age
QUERY = """
SELECT Age, COUNT(*) as count
FROM master
GROUP BY age
ORDER BY age
"""

# The read_sql_query runs the SQL query and returns the data as a DataFrame
age_count_df = pd.read_sql_query(QUERY, conn)
print(age_count_df)

# Plot a histogram of age counts
plt.figure(figsize=(10, 6))
plt.hist(age_count_df['Age'], bins=30, edgecolor='black')
plt.title('Histogram of Age Counts')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Box plot for age
plt.figure(figsize=(10, 6))
plt.boxplot(age_count_df['Age'])
plt.title('Boxplot of Age')
plt.ylabel('Age')
plt.show()

# Scatter plot for age and count
plt.figure(figsize=(10, 6))
plt.scatter(age_count_df['Age'], age_count_df['count'])
plt.title('Scatter Plot of Age and Count')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Bubble plot of WorkWeekHrs and CodeRevHrs, use Age column as bubble size
QUERY = """
SELECT WorkWeekHrs, CodeRevHrs, Age
FROM master
WHERE WorkWeekHrs IS NOT NULL AND CodeRevHrs IS NOT NULL AND Age IS NOT NULL
"""

bubble_data = pd.read_sql_query(QUERY, conn)

plt.figure(figsize=(12, 8))
plt.scatter(bubble_data['WorkWeekHrs'], bubble_data['CodeRevHrs'], s=bubble_data['Age'], alpha=0.5)
plt.title('Bubble Plot of WorkWeekHrs and CodeRevHrs')
plt.xlabel('WorkWeekHrs')
plt.ylabel('CodeRevHrs')
plt.show()


# Query to get unique values for the 'BetterLife' column
better_life_query = """
SELECT DISTINCT OpSys
FROM master
WHERE OpSys IS NOT NULL
"""

better_life_values = pd.read_sql_query(better_life_query, conn)
print("Unique values for the 'BetterLife' column:")
print(better_life_values)

# Query to get the top 5 databases respondents wish to learn next year
QUERY = """
SELECT LanguageDesireNextYear, COUNT(*) as count
FROM master
WHERE LanguageDesireNextYear IS NOT NULL
GROUP BY LanguageDesireNextYear
ORDER BY count DESC
LIMIT 5
"""

top_databases = pd.read_sql_query(QUERY, conn)
plt.figure(figsize=(8, 8))
plt.pie(top_databases['count'], labels=top_databases['LanguageDesireNextYear'], autopct='%1.1f%%', startangle=90)
plt.title('Top 5 Languages Respondents Wish to Learn Next Year')
plt.show()

# Query for the percentage of MongoDB
mongodb_percentage = top_databases[top_databases['LanguageDesireNextYear'] == 'MongoDB']['count'].values[0] / top_databases['count'].sum() * 100
print(f"Percentage of MongoDB: {mongodb_percentage:.2f}%")

# Query for respondents currently working with 'SQL'
sql_currently_working_query = """
SELECT COUNT(*) as count
FROM master
WHERE LanguageWorkedWith LIKE '%SQL%'
"""

sql_currently_working = pd.read_sql_query(sql_currently_working_query, conn)
print(f"Respondents currently working with 'SQL': {sql_currently_working['count'].values[0]}")

# Query for respondents working on 'MySQL' only
mysql_only_query = """
SELECT COUNT(*) as count
FROM master
WHERE DatabaseWorkedWith LIKE '%MySQL%' AND LanguageDesireNextYear NOT LIKE '%MySQL%'
"""

mysql_only = pd.read_sql_query(mysql_only_query, conn)
print(f"Respondents working on 'MySQL' only: {mysql_only['count'].values[0]}")


# Query to count the number of respondents for each MainBranch
main_branch_query = """
SELECT MainBranch, COUNT(*) as count
FROM master
WHERE MainBranch IS NOT NULL
GROUP BY MainBranch
ORDER BY count DESC
"""

main_branch_counts = pd.read_sql_query(main_branch_query, conn)
print("Number of respondents for each MainBranch:")
print(main_branch_counts)


# Close the database connection
conn.close()
