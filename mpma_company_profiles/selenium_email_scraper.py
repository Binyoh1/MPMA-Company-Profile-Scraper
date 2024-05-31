from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

# Read the links.txt file
with open("../docs/links.txt", "r") as file:
    lines = file.readlines()

# Write to a emails.csv file
with open("../export/emails.csv", mode="a", newline="") as f:
    writer = csv.writer(f)
    # Loop through each line
    for line in lines:
        # Navigate to the link on that line
        driver = webdriver.Firefox()
        driver.get(line)
        try:
            # Extract text from element
            link_path = "//joomla-hidden-mail/a"
            element = driver.find_element(
                By.XPATH,
                link_path,
            )
            text = element.text
            f.write(f"{text}\n")
        except Exception as e:
            f.write(f"null\n")

        # Close the browser
        driver.quit()
