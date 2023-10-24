import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = options)
driver.get('https://en.onepiece-cardgame.com/cardlist/?series=569104')

#Accepter les cookies
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

#Clique sur les sets
driver.find_element(By.CLASS_NAME, "selModalButton").click()

#Clique sur "All" pour selectioné toutes les sets
driver.find_element(By.CSS_SELECTOR, ".selModalClose:nth-of-type(2)").click()

#Lancer la rechercher pour avoir toutes les cartes de tout les sets
driver.find_element(By.CLASS_NAME, "submitBtn").click()
