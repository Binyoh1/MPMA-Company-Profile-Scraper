from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to a web page
driver.get("https://www.mpmadirectory.org.my/members/a-a-plastic-industries-sdn-bhd")

# Locate the element containing the text you want to copy
element = driver.find_element(
    By.XPATH,
    "//joomla-hidden-mail/a",
)


# Open a file in write mode
with open("./docs/file.txt", "w") as file:
    # Write the text content to the file
    file.write(element.text)

# Close the file
file.close()

# Close the browser
driver.quit()
