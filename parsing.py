import pandas as pd
import json

# Trying to import the JSON file I am getting the error:
# json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
# Which means that the json file should have double quoutes instead of single ones. 
# Another error is that the values `None` and `True` do not have double quoutes either. 
# As a consequence, I am replacing single quotes for double quotes, and adding double quotes to `None` and `True`
# before reading the data in JSON format.

# Read the JSON file with single quotes
with open('ubo.json', 'r') as f:
    data = f.read()

# In this case I duplicated the company information to see whether the
# information for each company is parsed correctly (one row for each company). In case you're interested in run it,
# just uncomment these two lines.
# with open('ubo_v2.json', 'r') as f:
#     data = f.read()

# Replace single quotes with double quotes and adding quotes to `None` and `True`
data = data.replace("'", "\"").replace("None", "\"None\"").replace("True", "\"True\"")

# Parse the JSON data
parsed_data = json.loads(data)
print('_'*50)
print('_'*20, ' Parsed data:')
print(parsed_data)

# Since all the relevant information is inside the element 'results/companies', I will start working with it
print('_'*50)
print('_'*20, ' Companies data:')
companies = parsed_data['results']['companies']
print('Number of companies: ', len(companies))
print(companies)

# Trying different options to parse the data into a dataframe
# Option 1: Create a DataFrame from a dictionary
# Result: This option does not work because of the dept of the JSON
# Comment: This dataframe is exported in a csv file
print('_'*50)
print('_'*20, ' Option 1:')
try: 
    df1 = pd.DataFrame(companies)
    df1.to_csv('parsed_json/option1.csv')
    print(df1.head())
except:
    print("Unable to export file because of an error")

# Option 2: Normalize the JSON and create a dataframe
# Result: This option offers enough flexibility to access most of the information.
# Comment: variable 'Industry code' has more nested variables but they are inside a list
print('_'*50)
print('_'*20, ' Option 2:')
try: 
    df2 = pd.json_normalize(companies,max_level=10)
    df2.to_csv('parsed_json/option2.csv')
    print(df2.head())
except:
    print("Unable to export file because of an error normalizing the JSON file")

# Option 3: Parsing manually
# Comment: Having checked the information in the option 2, the best way to keep a dataframe 
# where there's a single row per company, is to keep industry codes in another table and when
# needed apply a join to merge both tables. In this option the first table will have all the variables
# of the company, and the second will have its corresponding industry tables
print('_'*50)
print('_'*20, ' Option 3:')
# print(companies[0])
# print('+'*50)
# print(companies[0]['company']['industry_codes'])
# print(companies[1]['company']['industry_codes'])
try: 
    df3_1 = pd.json_normalize(companies,max_level=10)
    df3_1.to_csv('parsed_json/option3_1.csv')
    print(df3_1.head())
    # If there's more than 1 company then extracts a industry_code dataframe for each company
    if len(companies) == 1:
       df3_2 = pd.json_normalize(companies[0]['company']['industry_codes'],max_level=10)
       df3_2.to_csv('parsed_json/option3_2.csv')
       print(df3_2.head())
    else:
        for i in range(len(companies)):
            temp = pd.json_normalize(companies[i]['company']['industry_codes'],max_level=10)
            temp.to_csv('parsed_json/option3_company' + str(i) + '.csv')
            print('Industry_codes for company ' + str(i))
            print(temp.head())    
except:
    print("Unable to export file because of an error normalizing the JSON file")