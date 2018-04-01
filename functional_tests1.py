from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost:9300')

assert 'Django' in browser.title