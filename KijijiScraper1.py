from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import re
import csv
sns.set()

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

# Load the webpage

for i in range(20):
    kijiji='https://www.kijiji.ca/b-espaces-commerciaux-bureaux-a-vendre/ville-de-montreal/c44l1700281'.format(i)

r = get(kijiji, headers=headers)

# Creating a Beautiful Soup Object
soup = bs(r.content, 'html.parser')



results = soup.find_all('div', attrs={'class':'clearfix'})
records = []  
for result in results:  
    
    titles = result.find_all('div', attrs={'class':'title'})
    titles = [str(titles.text).strip() for titles in titles]

    prices = result.find_all('div', attrs={'class':'price'})
    prices = [str(prices.text).strip() for prices in prices]
    
    locations = result.find_all('div', attrs={'class':'location'})
    locations = [str(locations.text).strip() for locations in locations]
    
    descriptions = result.find_all('div', attrs={'class':'description'})
    descriptions = [str(descriptions.text).strip() for descriptions in descriptions]
    
    records.append((titles, prices, locations, descriptions))
    
    df = pd.DataFrame(records, columns=({'titles': titles,
    'Price': prices,
     'location': locations,
     'description': descriptions}))



# create excel writer object
writer = pd.ExcelWriter('kijijidata1.xlsx')
# write dataframe to excel
df.to_excel(writer)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')