import requests
from bs4 import BeautifulSoup

Scraped_jobs = []

def scrape_web3(keyword):
    Scraped_jobs = []
    url = f"https://web3.career/{keyword}-jobs"
    print(f"Scrapping {url}...")
    
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://web3.career/",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        }
    )
    
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find_all("tr", class_="table_row")

    if not jobs:
        Scraped_jobs.clear()
        print("No jobs :(")
        return

    for job in jobs:
        title_tag = job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary")
        if not title_tag:
            continue
            
        title = title_tag.text.strip()
        
        company_tag = job.find("h3")
        company = company_tag.text.strip() if company_tag else "N/A"
        
        link_tag = title_tag.find_parent("a")
        link_job = link_tag["href"] if link_tag else "#"
        if not link_job.startswith("http"):
            link_job = f"https://web3.career{link_job}"

        location_tag = job.find("td", class_="job-location-mobile")
        location = location_tag.text.strip() if location_tag else "Remote"
        
        salary_tag = job.find("p", class_="text-salary")
        salary = salary_tag.text.strip() if salary_tag else ""
        
        info = f"{location} • {salary}" if salary else location

        job_data = {
            "company": company,
            "title": title,
            "info": info,
            "link_job": link_job
        }
        Scraped_jobs.append(job_data)
    
    return Scraped_jobs


class my_urls: 
    def __init__(self, url):
        self.url = url

    def show_info(self):
        scrape_web3(self.url)
        job_num = 0     
        for potato in Scraped_jobs:
            print(f"job_num[{job_num+1}] > \ncompany : {potato['company']}\ntitle : {potato['title']}\ninfo_job : {potato['info']}\nlink : {potato['link_job']}\n")
            job_num = job_num + 1
            
    def show_len(self):
        scrape_web3(self.url)   
        print(len(Scraped_jobs), "jobs found.")