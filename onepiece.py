import csv
import json
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

#print(card_name.text)
def get_data():
    cards = driver.find_elements(By.CLASS_NAME, "modalCol")
    data = []
    #effect, counter, cardTrigger, cardSet, color, rarity, type, attribute, cost.
    for card in cards:
        name = card.find_element(By.CLASS_NAME, "cardName")
        number = card.find_element(By.CSS_SELECTOR, ".infoCol span:nth-child(1)")
        image_url = card.find_element(By.CSS_SELECTOR, ".frontCol img")
        power = card.find_element(By.CSS_SELECTOR, ".power")
        effect = card.find_element(By.CSS_SELECTOR, ".text")
        counter = card.find_element(By.CSS_SELECTOR, ".counter")
        set = card.find_element(By.CSS_SELECTOR, ".getInfo")
        color = card.find_element(By.CSS_SELECTOR, ".color")
        rarity = card.find_element(By.CSS_SELECTOR, ".infoCol span:nth-child(3)")
        type = card.find_element(By.CSS_SELECTOR, ".feature")
        attribute = card.find_element(By.CSS_SELECTOR, ".attribute i")
        cost = card.find_element(By.CSS_SELECTOR, ".cost")
        
        try:
            trigger = card.find_element(By.CSS_SELECTOR, ".trigger")
            text_trigger = trigger.get_attribute("innerText")
        except:
            text_trigger = ''

        card_item = {
            'name': name.get_attribute("innerText"),
            'number': number.get_attribute("innerText"),
            'imageUrl': image_url.get_attribute("src"),
            'power': power.get_attribute("innerText"),
            'effect': effect.get_attribute("innerText"),
            'counter': counter.get_attribute("innerText"),
            'trigger': text_trigger,
            'set': set.get_attribute("innerText"),
            'color': color.get_attribute("innerText"),
            'rarity': rarity.get_attribute("innerText"),
            'type': type.get_attribute("innerText"),
            'attribute': attribute.get_attribute("innerText"),
            'cost': cost.get_attribute("innerText"),
        }
        data.append(card_item)

    return data

with open("data.json", "w") as outfile:
    json.dump(get_data(), outfile, indent = 4)
#print(get_data())
