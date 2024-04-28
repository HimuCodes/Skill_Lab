import pandas as pd
# Assuming you have a DataFrame named 'gdp_data' with columns 'Country' and 'GDP'
# Sample dataset
data = {
'Country': ['USA', 'China', 'Japan', 'Germany', 'India'],
'GDP': [21.43, 14.34, 5.08, 4.42, 3.17]
}
gdp_data = pd.DataFrame(data)
# a. Find and print the name of the country with the highest GDP
country_highest_gdp = gdp_data.loc[gdp_data['GDP'].idxmax(), 'Country']
print("Country with the highest GDP:", country_highest_gdp)
# b. Find and print the name of the country with the lowest GDP
country_lowest_gdp = gdp_data.loc[gdp_data['GDP'].idxmin(), 'Country']
print("Country with the lowest GDP:", country_lowest_gdp)
# c. Print text and input values iteratively
for index, row in gdp_data.iterrows():
    print("Country:", row['Country'], "- GDP:", row['GDP'])
# d. Print the entire list of the countries with their GDPs
    print(gdp_data)
# e. Print the highest GDP value, lowest GDP value, mean GDP value, standardized GDP

highest_gdp = gdp_data['GDP'].max()
lowest_gdp = gdp_data['GDP'].min()
mean_gdp = gdp_data['GDP'].mean()
std_gdp = gdp_data['GDP'].std()
sum_gdp = gdp_data['GDP'].sum()
print("Highest GDP:", highest_gdp)
print("Lowest GDP:", lowest_gdp)
print("Mean GDP:", mean_gdp)
print("Standardized GDP:", std_gdp)
print("Sum of all GDPs:", sum_gdp)