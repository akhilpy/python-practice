from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
"""Web scrapping using BS4:
        In this example we scrapped the description page of particular job as well navaigate the next pages(pagination)
  """


url="https://boston.craigslist.org/search/ofc?"
job_info={}
job_num=0
while True:
    res= requests.get(url)
    data=res.text
    soup=BeautifulSoup(data, "html.parser")

    jobs =soup.find_all("p", {"class":"result-info"})

    for job in jobs:
        title = job.find("a", {"class":"result-title"}).text
        location_tag= job.find("span", {"class":"result-hood"})
        location = location_tag.text if location_tag else "N/A"
        date= job.find("time", {"class":"result-date"}).text
        link=job.find("a", {"class":"result-title"}).get("href")
        job_res = requests.get(link)
        job_data=job_res.text
        # job_soup=BeautifulSoup(job_data, "html.parser")
        # job_description= job_soup.find('section', {"id":"postingbody"}).text
        # job_attr_tag=job_soup.find("p", {"class":"attrgroup"})
        # job_attr= job_attr_tag.text if job_attr_tag else "N/A"

        job_num+=1
        job_info[job_num]=[title, location, date, link]
        print("Job Title:", title)
        print("Job location:", location)
        print("Job date:", date)
        print("Job link:", link)

    url_tag = soup.find("a",{"title":"pager-last"})
    if url_tag.get("href"):
        url ="https://boston.craigslist.org"+url_tag.get("href")
        print(url)
       
    else:
        break

print("total jobs:",job_num)

job_info_df= pd.DataFrame.from_dict(job_info, orient="index", columns=["title", "location", "date", "link"])

job_info_df.to_csv("web_scrapping/jobs.csv")

print("Done")
    
