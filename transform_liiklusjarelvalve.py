import pandas as pd

# Read in data from Excel (requires openpyxl). Adjust the filename as needed:
df = pd.read_excel('data/liiklusjarelvalve.xlsx', decimal=',')

# Rename date-related columns (optional, but helpful for clarity).
#df = df.rename(columns={'Aasta': 'year', 'Kuu': 'month', 'Päev': 'day', 'Kell (UTC)': 'time'})

# Merge date information into a single DateTime column, and drop the originals.
#df['ToimKpv'] = pd.to_datetime(
#    df['year'].astype(str) + '-' + df['month'].astype(str) + '-' + df['day'].astype(str) + ' ' + df['time'].astype(str),
#    format='%Y-%m-%d %H:%M:%S', 
#    utc=True
#)
#df = df.drop(columns=['year', 'month', 'day', 'time'])

# Export to Parquet
df.to_parquet('superset_build/data/liiklus.parquet', index=False)