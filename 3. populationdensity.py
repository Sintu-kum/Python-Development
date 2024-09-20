#3.Calculate the population density (population per unit area) for each city and add it as a new column to the Dataframe.
import pandas as pd

def population_density(df):
    df['Population Density (per sq km)'] = df['Population'] / df['Area (sq km)']
    
    return df
data = {
    'City': ['CityA', 'CityB', 'CityC'],
    'Population': [500000, 1200000, 300000],
    'Area (sq km)': [300, 500, 150]
}

df = pd.DataFrame(data)
df_density = population_density(df)
print(df_density)
