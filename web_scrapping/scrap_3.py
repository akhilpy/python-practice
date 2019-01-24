from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

""" Web scrapping example 3
"""
url= "https://www.programmableweb.com/apis/directory"
base_url="https://www.programmableweb.com"

api_info={}
api_no=0
while True:
    response= requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    api_data = soup.find_all('tr', {"class":"even", "class":"odd"})
    
    for api in api_data:
        api_name=api.find('a').text
        api_link=base_url+api.find('a').get("href")
        api_description=api.find('td',{"class":"views-field-field-api-description"}).text
        api_category_tag=api.find('td',{"class":"views-field-field-article-primary-category"})
        api_category=api_category_tag.text if api_category_tag else "N/A"
        
    
    api_no +=1
    api_info[api_no]=[api_name, api_link,api_description,api_category]

    url_tag = soup.find("a",{"title":"Go to next page"})
    if url_tag.get("href"):
        url ="https://www.programmableweb.com"+url_tag.get("href")
    else:
        break
    

print(api_info)

api_info_df= pd.DataFrame.from_dict(api_info, orient="index", columns=["name", "link", "description", "category"])

job_info_df.to_csv("web_scrapping/api_info.csv")

print("Done")