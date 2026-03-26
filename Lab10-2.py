import pandas as pd
data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'Karnataka', 'Tamil Nadu'],
    'Area': [307713, 196024, 342239, 191791, 130058],  # in sq km
    'Population': [124000000, 70000000, 81000000, 68000000, 75000000]
}

df = pd.DataFrame(data)

# a) Complete information
print("\nState Information:\n")
print(df)

# b) State with largest area
largest_area = df.loc[df['Area'].idxmax()]
print("\nState with largest Area:", largest_area['State'])

# c) State with largest population
largest_pop = df.loc[df['Population'].idxmax()]
print("State with largest Population:", largest_pop['State'])

# d) Population density calculation
df['Density'] = df['Population'] / df['Area']

print("\nWith Population Density:\n")
print(df)

# e) State with highest density
highest_density = df.loc[df['Density'].idxmax()]
print("\nState with highest Population Density:", highest_density['State'])