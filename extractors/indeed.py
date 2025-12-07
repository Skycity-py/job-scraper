# BLUEPRINT | DONT EDIT

import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://berlinstartupjobs.com/engineering/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

skills = ["python", "typescript", "javascript", "rust"]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
Scraped_jobs = []

def scrape_page(keyword):
    Scraped_jobs = []
    url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    print(f"Scrapping {url}...")
    response = requests.get(
    url,
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    soup = BeautifulSoup(response.content,"html.parser")

    jobs  = soup.find("ul", class_ = "jobs-list-items") 

    if jobs:
        jobs = jobs.find_all("li")
    else:
        Scraped_jobs.clear()
        print("No jobs :(")
        return
    
    for job in jobs:
        title = job.find("h4", class_="bjs-jlid__h").text 
        company = job.find("a", class_="bjs-jlid__b").text 
        info = job.find("div", class_="bjs-jlid__description").text.strip() 
        link_job = job.find("a")["href"]

        job_data={
            "company":company,
            "title":title,
            "info":info,
            "link_job":link_job 
        }
        Scraped_jobs.append(job_data)
    return Scraped_jobs


class my_urls: 
    def __init__(self,url):
        self.url = url

    def show_info(self):
        scrape_page(self.url)
        job_num = 0     
        for potato in Scraped_jobs:
            print(f"job_num[{job_num+1}] > \ncompany : {potato["company"]}\ntitle : {potato["title"]}\ninfo_job : {potato["info"]}\nlink : {potato["link_job"]}\n")
            job_num = job_num+1
    def show_len(self):
        scrape_page(self.url)   
        print(len(Scraped_jobs),"jobs found.")

#scrape_page("python")
