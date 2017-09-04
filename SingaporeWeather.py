
# coding: utf-8

# In[15]:

import requests
from bs4 import BeautifulSoup as BS
import pandas as pd 
import os

# In[2]:

link = "http://www.weather.gov.sg/weather-forecast-4dayoutlook/"


# In[3]:

#does requests on the link 
page = requests.get(link).content

#apply bs4
content = BS(page, "lxml")


# In[4]:

#find the data 
div_finder = content.find(class_= "row table-container")


# In[11]:

def extract_data(div_finder):
    DATE_list         = []
    temp_HIGH_list    = []
    temp_LOW_list     = []
    wind_heading_list = []
    description_list  = []
    
    
    
    for day in range (1,5):
        day_n = div_finder.find_all('tr')[day]
        date  = day_n.find('td').get_text()

        temp_HIGH    = day_n.find_all('span')[0].get_text()
        temp_LOW     = day_n.find_all('span')[1].get_text()
        wind_heading = day_n.find_all('span')[2].get_text()
        description  = day_n.find_all('span')[3].get_text()
        
        DATE_list.append(date)
        temp_HIGH_list.append(temp_HIGH)
        temp_LOW_list.append(temp_LOW)
        wind_heading_list.append(wind_heading)
        description_list.append(description)
        
        print("DATE        : ", date)
        print("temp_HIGH   : ",temp_HIGH)
        print("temp_LOW    : ",temp_LOW)
        print("wind heading: ",wind_heading)
        print("description : ",description)
        print("==========================================================================")
        
    return DATE_list, temp_HIGH_list,temp_LOW_list, wind_heading_list, description_list


# In[16]:

date, temp_high, temp_low, wind_heading, description = extract_data(div_finder)

#DATE_list
#[i for i in extract_data(div_finder)]

os.system("pause")