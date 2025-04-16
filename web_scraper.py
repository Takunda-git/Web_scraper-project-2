import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_jobs():
    try:
        print("Starting the scraping process...")
        url = 'https://vacancymail.co.zw/jobs/'
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')

        # Select job listings using the correct class
        job_cards = soup.find_all('a', class_='job-listing')

        print(f"Found {len(job_cards)} job cards.")

        jobs = []
        for job in job_cards:
            title = job.find('h3', class_='job-listing-title').get_text(strip=True) if job.find('h3', class_='job-listing-title') else 'N/A'
            company = job.find('h4', class_='job-listing-company').get_text(strip=True) if job.find('h4', class_='job-listing-company') else 'N/A'
            location = job.find('i', class_='icon-material-outline-location-on').find_next().get_text(strip=True) if job.find('i', class_='icon-material-outline-location-on') else 'N/A'
            expiry_date = job.find('i', class_='icon-material-outline-access-time').find_next().get_text(strip=True) if job.find('i', class_='icon-material-outline-access-time') else 'N/A'
            description = job.find('p', class_='job-listing-text').get_text(strip=True) if job.find('p', class_='job-listing-text') else 'N/A'
            
            jobs.append({
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Expiry Date': expiry_date,
                'Description': description
            })

        # Create a DataFrame
        df = pd.DataFrame(jobs)

        # Check if DataFrame is empty
        if df.empty:
            print("No jobs found to write to CSV.")
        else:
            df.to_csv('scraped_data.csv', index=False)
            print("Data written to scraped_data.csv successfully.")
            logging.info('Scraping completed successfully.')

    except requests.exceptions.RequestException as e:
        logging.error(f'Request failed: {e}')
        print(f'Request failed: {e}')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    scrape_jobs()