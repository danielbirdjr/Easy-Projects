from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Define the URL for 90/10 ground beef
url = 'https://fdc.nal.usda.gov/fdc-app.html#/food-details/174030/nutrients'

# Set up the Selenium WebDriver (ensure you have the Chrome WebDriver installed)
driver_service = Service('path_to_chromedriver.exe')  # Replace with the path to your chromedriver executable
driver = webdriver.Chrome(service=driver_service)

# Open the webpage
driver.get(url) 

# Wait for the nutrient information to load (you may need to adjust the timeout)
nutrient_elements = driver.find_elements(By.XPATH, '//div[@class="nutrient-title"]')

# Create a dictionary to store nutritional information
nutritional_info = {}

# Define a list of nutrient titles to scrape
nutrient_titles = ["Protein", "Carbohydrate, by difference", "Total lipid (fat)"]

for nutrient_title in nutrient_titles:
    nutrient_element = None
    for element in nutrient_elements:
        if nutrient_title in element.text:
            nutrient_element = element
            break

    if nutrient_element:
        nutrient_value_element = nutrient_element.find_element(By.XPATH, './following-sibling::div[@class="nutrient-value"]')
        nutrient_value = float(nutrient_value_element.text.strip())
        nutritional_info[nutrient_title] = nutrient_value

# Print the nutritional information
for nutrient_title, nutrient_value in nutritional_info.items():
    print(f"{nutrient_title}: {nutrient_value} grams")

# Close the browser
driver.quit()
