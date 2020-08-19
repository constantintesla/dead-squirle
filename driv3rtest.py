import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.vl.ru/');
time.sleep(5) # Let the user actually see something!
latest_news = driver.find_elements_by_class_name('news__latest-post-link')

time.sleep(5) # Let the user actually see something!
driver.quit()

