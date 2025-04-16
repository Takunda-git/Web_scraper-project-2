# Job Scraper

## Overview

This project is a web scraper that extracts job listings from the Vacancy Mail website. The scraper collects data about job titles, companies, locations, expiry dates, and descriptions, then saves this information into a CSV file for easy access and analysis.

## How It Works

1. **Libraries Used**:
   - **`requests`**: For sending HTTP requests to the website and retrieving its content.
   - **`BeautifulSoup4`**: For parsing the HTML content and extracting relevant information.
   - **`pandas`**: For organizing the extracted data and saving it to a CSV file.

2. **Scraping Process**:
   - The scraper sends a GET request to the job listings page of Vacancy Mail.
   - It uses BeautifulSoup to parse the HTML and locate specific elements that contain job details.
   - The relevant information (job title, company, location, expiry date, and description) is extracted from the HTML structure.
   - The collected data is stored in a structured format and saved to a file named `scraped_data.csv`.

3. **Logging**:
   - The scraper includes logging functionality to track the scraping process. Any errors encountered during execution are recorded in a log file named `scraper.log`.

## Usage

1. **Run the Scraper**:
   - Execute the Python script `web_scraper.py` in a terminal. This will initiate the scraping process.

2. **Output**:
   - After execution, check the directory for the `scraped_data.csv` file, which will contain all extracted job listings.

3. **Error Handling**:
   - If the scraper does not find any job listings, it may be due to changes in the website's HTML structure. Review the `scraper.log` for any error messages.

## Conclusion

This job scraper provides a straightforward way to gather job listings from the Vacancy Mail website, making it easier for users to compile and analyze job data. It can be modified to scrape additional information or to work with different job listing websites as needed.
