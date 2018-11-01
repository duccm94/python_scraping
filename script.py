from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/reasonwhy/workspace/python_scraping/chromedriver")
driver.get("https://medium.com/@dalewahl")
driver.quit
