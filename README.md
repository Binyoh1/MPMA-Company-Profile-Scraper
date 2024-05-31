# MPMA Industry Directory Company Profile Scraper

## Project Summary

This project utlizes Scrapy and Selenium with Python to scrape business profiles from the [MPMA Industry Directory](https://www.mpmadirectory.org.my/all-members).

First, the scrapy spider crawls through each page of the website, extracts the each company's profile link, saving it to a *links.txt* file in the *docs* folder, then collects the following information for each company and saves to a *profiles.csv* file:
- Company Name
- Business Registration Number
- Year of Incorporation
- Chief Executive
- CEO Position
- Business Enquiry (Contact Person)
- Business Contact Person's Position
- Office Address
- Postal Code
- City/Town
- State
- Country
- Phone Number
- Fax Number
- Website
- Production Process
- Products Manufactured
- Current Export Markets

The major challenge with this project was extracting the company email since each one was masked using JavaScript. So I wrote a Python Selenium script (**selenium_email_scraper.py**) that would navigate to each company profile using the aforementioned *links.txt* file in a web browser (I used Mozilla Firefox with its Selenium driver), extract the company emails and save to an *emails.csv* file.

Thereafter, using pandas in a Jupyter Notebook (**parse.ipynb**), I merged the *profiles.csv* and *email.csv* files to obtain the complete company profile information available on the website.

The *requirements.txt* file contains the list of all Python libraries and dependencies used for this project.

All the relevant web crawling scripts are found in the *mpma_company_profiles* folder/directory.