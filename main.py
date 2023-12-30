import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests

LINK = 'https://it.123rf.com/free-images/?gad_source=1&gclid=EAIaIQobChMI3vDqkoyPgwMVhYVoCR3t_AEkEAAYASABEgLsF_D_BwE&gclsrc=aw.ds#googtrackad17'
path = 'C:\\Users\\faouz\\Desktop\\output'
chrome_driver = ChromeDriverManager().install()

def ricercaimmagine(nome):
    driver = Chrome(service=Service(chrome_driver))
    driver.get(LINK)
    driver.find_element(By.ID, 'mainsearchbar-input').send_keys(nome)        
    driver.find_element(By.ID, 'mainsearchbar-submit').click()               
    time.sleep(1)                                                                  
    immagini = driver.find_elements(By.CLASS_NAME, "ImageThumbnail__image")    
    src = immagini[1].get_attribute('src')                                           
    driver.quit()                                                                   
    salvataggioimmagine(src, nome)

def salvataggioimmagine(url, nome):
    img_name = nome.strip().lower() + ".png"                                       
    file_path = os.path.join(path, img_name)                                       
    response = requests.get(url)                                                  
    if response.status_code == 200:
        with open(file_path, "wb") as file:                                        
            file.write(response.content)
        print(f"L'immagine è stata salvata con successo in: {file_path}")
    else:
        print(f"Errore nella richiesta. Codice di risposta: {response.status_code}")

def estrazionenome():
    with open('nomi.txt', 'r') as file:
        for riga in file:
            print(riga.strip())
            ricercaimmagine(riga.strip())

if __name__ == "__main__":
    estrazionenome()
