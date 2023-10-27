import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
#options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options = options)
#driver.maximize_window()
#driver.implicitly_wait(20)
driver.get('https://en.onepiece-cardgame.com/cardlist/?series=569104')

#Accepter les cookies
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

#Clique sur les sets
#driver.find_element(By.CLASS_NAME, "selModalButton").click()

#Clique sur "All" pour selectioné toutes les sets
#driver.find_element(By.CSS_SELECTOR, ".selModalClose:nth-of-type(2)").click()

#Lancer la rechercher pour avoir toutes les cartes de tout les sets
#driver.find_element(By.CSS_SELECTOR, ".submitBtn input").click()

#Récupération des data
def get_data():
    cards = driver.find_elements(By.CLASS_NAME, "modalCol")
    data = []
    
    for card in cards:
        name_element = card.find_element(By.CLASS_NAME, "cardName")
        number_element = card.find_element(By.CSS_SELECTOR, ".infoCol span:nth-child(1)")
        image_url_element = card.find_element(By.CSS_SELECTOR, ".frontCol img")
        power_element = card.find_element(By.CSS_SELECTOR, ".power")
        effect_element = card.find_element(By.CSS_SELECTOR, ".text")
        counter_element = card.find_element(By.CSS_SELECTOR, ".counter")
        set_element = card.find_element(By.CSS_SELECTOR, ".getInfo")
        color_element = card.find_element(By.CSS_SELECTOR, ".color")
        rarity_element = card.find_element(By.CSS_SELECTOR, ".infoCol span:nth-child(2)")
        type_element = card.find_element(By.CSS_SELECTOR, ".feature")
        attribute_element = card.find_element(By.CSS_SELECTOR, ".attribute i")
        cost_element = card.find_element(By.CSS_SELECTOR, ".cost")

        name = name_element.get_attribute("innerText")
        number = number_element.get_attribute("innerText")
        image_url = image_url_element.get_attribute("src")
        power = power_element.get_attribute("innerText")
        effect = effect_element.get_attribute("innerText")
        counter = counter_element.get_attribute("innerText")
        set = set_element.get_attribute("innerText")
        color = color_element.get_attribute("innerText")
        rarity = rarity_element.get_attribute("innerText")
        type = type_element.get_attribute("innerText")
        attribute = attribute_element.get_attribute("innerText")
        cost = cost_element.get_attribute("innerText")

        
        #Si il y a un trigger on l'ajoute, sinon le trigger est vide
        try:
            trigger = card.find_element(By.CSS_SELECTOR, ".trigger")
            text_trigger = trigger.get_attribute("innerText")
        except:
            text_trigger = ''


        #Filtrage des string pour return un number
        def get_int(string):
            resultat = re.search(r'\d+', string)
            if resultat:
                return int(resultat.group())
            return 0

        power_int = get_int(power)
        counter_int = get_int(counter)
        cost_int = get_int(cost)


        #Définir si une "card" et "alternate" ou pas
        if "_p" in image_url:
            alternate = 1
        else:
            alternate = 0  

        
        #Color string to array
        color_clear = color[5:]
        color_array = color_clear.split("/")
        color_array.remove("")


        #Type string to array
        type_clear = type[4:]
        type_array = type_clear.split("/")

        card_item = {
            'name': name,
            'number': number,
            'imageUrl': image_url,
            'alternate' : alternate,
            'power': power_int,
            'effect': effect, #array ou pas?
            'counter': counter_int,
            'trigger': text_trigger,
            'set': set,
            'color': color_array,#array
            'rarity': rarity,
            'type': type_array,#array
            'attribute': attribute,
            'cost': cost_int,
        }
        data.append(card_item)

    return data

#with open("data.json", "w") as outfile:
    #json.dump(get_data(), outfile, indent = 4)
print(get_data())