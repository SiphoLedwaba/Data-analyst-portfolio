import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load shapefiles
police_bounds = gpd.read_file(r"C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Final Cut\Crime RSA\Datasets\Police_bounds.shp")
police_points = gpd.read_file(r"C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Final Cut\Crime RSA\Datasets\Police_points.shp")

# Load CSV files
province_population = pd.read_csv(r"C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Final Cut\Crime RSA\Datasets\ProvincePopulation.csv")
crime_stats = pd.read_csv(r"C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Final Cut\Crime RSA\Datasets\SouthAfricaCrimeStats_v2.csv")

# Inspect the data
print(police_bounds.head())
print(police_points.head())
print(province_population.head())
print(crime_stats.head())

# Checking for null values in critical columns
null_values = crime_stats.isnull().sum()
print("Null values in each column:\n", null_values)

# Total crimes by province and category
crime_stats['Total_Crimes'] = crime_stats.iloc[:, 3:].sum(axis=1)
total_crimes_by_province_category = crime_stats.groupby(['Province', 'Category'])['Total_Crimes'].sum().reset_index()
total_crimes_by_province_category = total_crimes_by_province_category.sort_values(by='Total_Crimes', ascending=False)
print("Total crimes by province and category:\n", total_crimes_by_province_category.head())

# Total crimes by province
total_crimes_by_province = crime_stats.groupby('Province')['Total_Crimes'].sum().reset_index()
print("Total crimes by province:\n", total_crimes_by_province.head())

# Merge crime statistics with population data
crime_stats_population = pd.merge(crime_stats, province_population, on='Province')
crime_stats_population['Crime_Rate_per_100k'] = (crime_stats_population['Total_Crimes'] / crime_stats_population['Population']) * 100000
print("Crime rate per 100k by province:\n", crime_stats_population[['Province', 'Crime_Rate_per_100k']].head())

# Trend analysis: Yearly total crimes
yearly_crimes = crime_stats.iloc[:, 3:-1].sum().reset_index()
yearly_crimes.columns = ['Year', 'Total_Crimes']
print("Yearly crime trends:\n", yearly_crimes)

# Visualization: Crime trends over time
plt.figure(figsize=(12, 6))
plt.plot(yearly_crimes['Year'], yearly_crimes['Total_Crimes'], marker='o')
plt.title('Total Crimes in South Africa Over Time')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Visualization: Police station locations
plt.figure(figsize=(10, 10))
police_points.plot(ax=plt.gca(), color='blue', markersize=10)
plt.title('Police Station Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Calculate Total Crimes by Province and Year
crime_stats_population['Total_Crimes'] = crime_stats_population.iloc[:, 3:-4].sum(axis=1)

# Calculate crime rate per 100k people
crime_stats_population['Crime_Rate_Per_100k'] = (crime_stats_population['Total_Crimes'] / crime_stats_population['Population']) * 100000

# Group by Province and Category to get crime stats
province_category_stats = crime_stats_population.groupby(['Province', 'Category'])['Total_Crimes'].sum().reset_index()

# Plotting total crimes by province
plt.figure(figsize=(12, 6))
sns.barplot(x='Total_Crimes', y='Province', data=province_category_stats, hue='Category', palette='Set2')
plt.title('Total Crimes by Province and Category')
plt.show()

# Analyzing crime rate per 100k people
province_crime_rate = crime_stats_population.groupby('Province')['Crime_Rate_Per_100k'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='Crime_Rate_Per_100k', y='Province', data=province_crime_rate, hue='Province', palette='Set3', legend=False)
plt.title('Average Crime Rate per 100k People by Province')
plt.show()

# Crime trend over years
years = [col for col in crime_stats.columns if '20' in col]
crime_trend = crime_stats_population.groupby('Province')[years].sum().T
plt.figure(figsize=(14, 8))
sns.lineplot(data=crime_trend)
plt.title('Crime Trend Over the Years by Province')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.legend(title='Province', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Hotspot analysis
if 'Longitude' in crime_stats_population.columns and 'Latitude' in crime_stats_population.columns:
    merged_gdf = gpd.GeoDataFrame(crime_stats_population, geometry=gpd.points_from_xy(crime_stats_population['Longitude'], crime_stats_population['Latitude']))
    merged_gdf = merged_gdf.set_crs(epsg=4326)
    crime_hotspots = merged_gdf.dissolve(by='Province', aggfunc='sum')
    plt.figure(figsize=(10, 10))
    crime_hotspots.plot(column='Crime_Rate_Per_100k', cmap='Reds', legend=True)
    plt.title('Crime Hotspots by Province')
    plt.show()
else:
    print("Columns 'Longitude' or 'Latitude' not found in the DataFrame.")

# Crimes per square km
crime_stats_population['Crimes_per_SqKm'] = crime_stats_population['Total_Crimes'] / crime_stats_population['Density']
plt.figure(figsize=(10, 8))
sns.barplot(data=crime_stats_population, x='Province', y='Crimes_per_SqKm', ci=None)
plt.xticks(rotation=45)
plt.title('Crimes per Square Kilometer by Province')
plt.ylabel('Crimes per Square Kilometer')
plt.show()
