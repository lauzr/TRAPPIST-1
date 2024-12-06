import pandas as pd

df = pd.read_excel("helio_degrees.xlsx")
df = df.drop(columns=['Unnamed: 0'])
df.info()

# Rounding the values to 2 decimal places
df['earth'] = df['earth'].round(2)
df['moon'] = df['moon'].round(2)
df['mercury'] = df['mercury'].round(2)
df['venus'] = df['venus'].round(2)
df['mars'] = df['mars'].round(2)
df['jupiter'] = df['jupiter'].round(2)
df['saturn'] = df['saturn'].round(2)
df['uranus'] = df['uranus'].round(2)
df['neptune'] = df['neptune'].round(2)
df['pluto'] = df['pluto'].round(2)

print(df)

def map_value_with_decimal(x):
    # Extract integer part before the point and decimal part
    int_part = int(x)
    decimal_part = round(x - int_part, 2)  # Keep two decimal places

    # Map the integer part based on the given range to indicate the flux change for how close or faw away it gets from the exact galactic degree
    if int_part >= 351:
        int_part = 5
    elif int_part == 350:
        int_part = 4
    elif int_part == 349:
        int_part = 3
    elif int_part == 348:
        int_part = 2
    elif int_part == 347:
        int_part = 1
    elif int_part == 346:
        int_part = 0
    elif int_part == 345:
        int_part = 1
    elif int_part == 344:
        int_part = 2
    elif int_part == 343:
        int_part = 3
    elif int_part == 342:
        int_part = 4
    elif int_part <= 341:
        int_part = 5

    # Combine the modified integer part with the original decimal part
    new_value = int_part + decimal_part
    return new_value

# Apply the mapping function to the DataFrame as a new column and dropping the columns with the old values
df['earth_mapped_value'] = df['earth'].apply(map_value_with_decimal)
df = df.drop(columns=['earth'])

df['moon_mapped_value'] = df['moon'].apply(map_value_with_decimal)
df = df.drop(columns=['moon'])

df['mercury_mapped_value'] = df['mercury'].apply(map_value_with_decimal)
df = df.drop(columns=['mercury'])

df['venus_mapped_value'] = df['venus'].apply(map_value_with_decimal)
df = df.drop(columns=['venus'])

df['mars_mapped_value'] = df['mars'].apply(map_value_with_decimal)
df = df.drop(columns=['mars'])

df['jupiter_mapped_value'] = df['jupiter'].apply(map_value_with_decimal)
df = df.drop(columns=['jupiter'])

df['saturn_mapped_value'] = df['saturn'].apply(map_value_with_decimal)
df = df.drop(columns=['saturn'])

df['uranus_mapped_value'] = df['uranus'].apply(map_value_with_decimal)
df = df.drop(columns=['uranus'])

df['neptune_mapped_value'] = df['neptune'].apply(map_value_with_decimal)
df = df.drop(columns=['neptune'])

df['pluto_mapped_value'] = df['pluto'].apply(map_value_with_decimal)
df = df.drop(columns=['pluto'])

# Display the updated DataFrame
print(df)
df.to_excel('mapped_helio_degrees.xlsx')