#Program 7(a)
#create a pandas dataframe frome a list of dictionaries.The data represents information about prouducts 
#(Products Name, Category, and Price). Add a new column that calculates the discounted price (90% of the original price) and display the DataFrame
import pandas as pd
data= {
     'Products Name' : ['Face Wash', 'Soap', 'Gel'],
     'Category' : ['A', 'B', 'A'],
     'Price' : [200, 190, 250]
     }
df = pd.DataFrame(data,index=["i", "ii", "iii"])
print(df)
print()
df['Discounted Price'] = df['Price'] * 0.90
print(df)
