from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy import Table, Column, String, Integer
import pandas as pd
# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata =MetaData()

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age',Integer()),
               Column('pop2000',Integer()),
               Column('pop2008',Integer()))

# Create the table in the database
metadata.create_all(engine)

### Adding Data

# read census.csv into a DataFrame : census_df
census_df = pd.read_csv('census.csv', header=None)

# rename the columns of the census DataFrame
census_df.columns = ['state','sex','age', 'pop2000', 'pop2008']
# append the data from census_df to the "census" table via connection
census_df.to_sql(name='census', con=connection, if_exists='append', index=False)

# Create an empty list: values_list
values_list = []

# Iterate over the rows
for row in csv_reader:
    # Create a dictionary with the values
    data = {'state': row[0], 'sex': row[1], 'age':row[2],'pop2000':row [3],'pop2008':row[4]}
    # Append the dictionary to the values list
    values_list.append(data)
   
# Build insert statement: stmt
stmt=insert(census)

# Use values_list to insert data: results
results=connection.execute(stmt,values_list)

# Print rowcount
print(results.rowcount)
