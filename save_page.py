# save_page.py
from selenium import webdriver
import time

# URL of the local Dash app
app_url = "http://localhost:8050"

# Start a browser session
browser = webdriver.Chrome()
browser.get(app_url)

# Wait for the page to load
time.sleep(5)  # Adjust time as needed for your app to load completely

# Save the rendered HTML to a file
with open("output.html", "w") as file:
    file.write(browser.page_source)

# Close the browser
browser.quit()