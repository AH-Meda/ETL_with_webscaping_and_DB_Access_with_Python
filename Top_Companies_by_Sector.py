# 1. Import required Libraries
import pandas as pd
import numpy as np
import requests
import sqlite3
from bs4 import BeautifulSoup


# 2. Initialize particulars
url = 'https://en.wikipedia.org/wiki/Forbes_Global_2000'
table_attr = ["Company_Name", "Sector", "Headquarters", "Sales_in[$B]", "Profit_in[$B]",\
              "Asset_in[$B]", "Market_Value_in[$B]", "Overall_Rank"]
tranformed_data_path = './Top_Companies_by_Sector_data2.csv' #if you want run notebook and python script


# 3. Extract the data from the Website
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')
    
df = pd.DataFrame(columns=table_attr)
table = data.find_all('tbody') 
rows = table[7].find_all('tr')# the seventh table on the website

for row in rows:
    col = row.find_all('td')
    if len(col) != 0:
        data_dict = {"Company_Name":col[1].contents[0],
                     "Sector":col[0].contents[0],
                     "Headquarters":col[2].contents[0],
                     "Sales_in[$B]":col[4].contents[0],
                     "Profit_in[$B]":col[5].contents[0],
                     "Asset_in[$B]":col[6].contents[0],
                     "Market_Value_in[$B]":col[7].contents[0],
                     "Overall_Rank":col[3].contents[0]
                        }
        df1 = pd.DataFrame(data_dict, index=[0])
        df = pd.concat([df,df1], ignore_index=True)
#There is a \n in market value column, that needs to be removed
MV = list(df['Market_Value_in[$B]'])
Modified_MV = [float(''.join(cell.split('\n'))) for cell in MV]
df['Market_Value_in[$B]'] = Modified_MV

#Remove the 0 in the beginning represent # in data from each cell in the overall rank column
OR = list(df['Overall_Rank'])
Modified_OR = [int(str(cell)[1:]) for cell in OR]
df['Overall_Rank'] = Modified_OR

print("Shape of the Dataframe: ", df.shape)
print(df.head(), '\n') # to add new line between print in the terminal


#4. Transoform
print(df.info(), '\n') #We have clean data and not much to do 

#create a new metrics -profit margin-ration of profit to sales and  to the df.
df['Sales_in[$B]'] = df['Sales_in[$B]'].astype(float)
df['Profit_in[$B]'] = df['Profit_in[$B]'].astype(float)
df['Profit_Margin_ratio[%]'] = (df['Profit_in[$B]']/df['Sales_in[$B]'] *100).round(2)
df.head()

# Save the dataframe as CSV
df.to_csv(tranformed_data_path, index=False) #'./Top_Companies_by_Sector_data2.csv'

## `5. Load to the Database and SQL Querying as necessary`
df = pd.read_csv("Top_Companies_by_Sector_data.csv") #read transformed csv file to df
conn = sqlite3.connect('Global_Companies.db') #create connectionn to the new DB and it will be created locally

#create a table and connect to the database
table_name ='Top_Companies_by_Sector'
df.to_sql(table_name, conn, if_exists = 'replace', index =False) #if exists, fail or replace also exist
print("The table is ready to use", '\n')

#Run SQL queries using read_sql function in pandas
# View the first five rows of the table
query_statement1 = f"SELECT * FROM {table_name} LIMIT(5)"
query_output = pd.read_sql(query_statement1, conn)
print("print the query output: The first five rows of the table\n", query_output)


# View Company name and its Headquarter for the first five rows
query_statement2 = f"SELECT Company_Name, Headquarters From {table_name} LIMIT(5)"
query_output2 = pd.read_sql(query_statement2, conn)
print("company name and their Headquareter location for the first five rows: \n", query_output2)

conn.close()

















