import pandas as pd
data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'Karnataka', 'Tamil Nadu'],
    'Area': [307713, 196024, 342239, 191791, 130058], 
    'Population': [124000000, 70000000, 81000000, 68000000, 75000000]
}

df = pd.DataFrame(data)

print("\nState Information:\n")
print(df)

largest_area = df.loc[df['Area'].idxmax()]
print("\nState with largest Area:", largest_area['State'])

largest_pop = df.loc[df['Population'].idxmax()]
print("State with largest Population:", largest_pop['State'])

df['Density'] = df['Population'] / df['Area']

print("\nWith Population Density:\n")
print(df)

highest_density = df.loc[df['Density'].idxmax()]
print("\nState with highest Population Density:", highest_density['State'])
