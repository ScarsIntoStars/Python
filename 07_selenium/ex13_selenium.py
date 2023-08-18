from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

# javascript로 현재 페이지 높이값 가져오기
# exe