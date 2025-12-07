import cloudscraper
from bs4 import BeautifulSoup

Scraped_jobs = []

def scrape_wwr(keyword):
    Scraped_jobs = []
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    print(f"Scrapping {url}...")
    
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    sections = soup.find_all("section", class_="jobs")
    
    if not sections:
        Scraped_jobs.clear()
        print("No jobs :(")
        return

    for section in sections:
        jobs = section.find_all("li")
        
        for job in jobs:
            if "view-all" in job.get("class", []):
                continue
            
            link_tag = job.find("a", class_="listing-link--unlocked")
            
            if link_tag:
                title = job.find("h3", class_="new-listing__header__title").text.strip()
                company = job.find("p", class_="new-listing__company-name").text.strip()
                info = job.find("p", class_="new-listing__company-headquarters").text.strip()
                link_job = link_tag["href"]
                
                if not link_job.startswith("http"):
                    link_job = f"https://weworkremotely.com{link_job}"

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
        scrape_wwr(self.url)
        job_num = 0     
        for potato in Scraped_jobs:
            print(f"job_num[{job_num+1}] > \ncompany : {potato['company']}\ntitle : {potato['title']}\ninfo_job : {potato['info']}\nlink : {potato['link_job']}\n")
            job_num = job_num + 1
            
    def show_len(self):
        scrape_wwr(self.url)   
        print(len(Scraped_jobs), "jobs found.")