# **WebScrapping (ETL) and Accessing DB with Python**
This project involves extracting data about top-ranked companies in each industry sector from a specified website, transforming the data (cleaning and adding additional comparison metrics), and then saving the data as a CSV format file on your local machine. Once saved, load the CSV data into a database and run basic SQL queries to access the information.


## 1. Project Overview
 Imagine you're a junior data engineer at a research firm. Your task is to write a Python script that extracts data about the top companies in the world, ranked by various factors such as sales amount, asset valuation, profit, or market valuation. This data is available on a specific website (URL provided). In addition to data extraction, you're tasked with data wrangling, including adding a new metric—profit margin (a ratio of profit to total sales). After transforming the data, save it in CSV format and load it into a database for executing  basic SQL queries

Use the following as particular of the code
Code Name: `top_companies_by_sector`
Data URL:`https://en.wikipedia.org/wiki/Forbes_Global_2000#2023_list`
Table Attribute(b4_transform): `Sector`, `Company`, `Headquarters`, `Sales_Billion`, `Profit_Billion`, `Asset_Billion`, `MV_Billion`, `Overall_Rank`
Table Attribute(After_transform): `Sector`, `Company`, `Headquarters`, `Sales_Billion`, `Profit_Billion`, `Asset_Billion`, `MV_Billion`,  `Overall_Rank`, `Profit_Margin_in[%]`,

Transformed_data: 	`./Top_Companies_by_Sector.csv`
Database_Name: `Global_Companies.db`
Table name: `Top_Companies_by_Sector`


## 2. Procedure
### 1. Import all need Libraries
Before you start building the code, you need to install the required libraries for it, if not installed already.  The libraries needed for the code are as follows:
* `numpy` - For mathematical operations.
* `pandas` -  For data processing, storage, and database communication.
* `requests` - For accessing information from the URL.
* `bs4` -  for web scraping.
* `sqlite3` -  For creating a database server connection.`

### 2. Extract Tabular Information from the URL.
* `Inspect the web page`: - identify the position and pattern of tabular information in the HTML code.
- Write and execute the extraction code to verify the output.
  
### 3. Transform the Extracted Data and Save as CSV.
* Do data cleaning - if there are missing values or null values
* Create a column that is a ratio of profit to sales column - to add the Net profit margin attribute to the data as a new metric.
* Save the output as `Top_Companies_by_Sector.csv`

### 4. Load the transformed data to the SQL database
write a code(function) to load and execute it to verify the output.

    a. Write the code for a function transform() to perform the said task.
    b. Execute a function call to transform() and verify the output.

### 5. Load the transformed data to the SQL database
Run `SQL queries` on the database to access the information. 


