import requests
from bs4 import BeautifulSoup
import pandas as pd

jobs = []
for i in range(1, 192):
    url = f"https://www.zangia.mn/job/list/pg.{i}"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')

    list = soup.find('div', class_='list')
    job_lists = list.find_all('div', class_='ad')


    

    for job in job_lists:
        job_title = job.find('b').text
        salary = job.find('span', class_='fsal').text
        jobs.append([job_title, salary])

df = pd.DataFrame(jobs, columns=['job_title', 'salary'])


df.to_csv('jobs.csv')
