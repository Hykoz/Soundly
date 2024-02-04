from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import zipfile
import os

# Créer une session Firefox
driver = webdriver.Firefox()
driver.implicitly_wait(10)  # Utiliser un délai plus court si nécessaire
driver.maximize_window()

# Ouvrir la page
url = "https://downloadsound.cloud/playlist/?url=https://soundcloud.com/bplx/sets/guts"
driver.get(url)

# Localiser le premier bouton de téléchargement par son XPath
first_download_button = driver.find_element(By.XPATH, '//a[@class="button is-primary is-medium"]')

# Utiliser JavaScript pour déclencher le clic sur le premier bouton
driver.execute_script("arguments[0].click();", first_download_button)

# Attendre quelques secondes (ajustez selon vos besoins)
time.sleep(5)

# Localiser le deuxième bouton de téléchargement par sa classe
second_download_button = driver.find_element(By.XPATH, '//a[@class="button is-primary"]')

# Utiliser JavaScript pour déclencher le clic sur le deuxième bouton
driver.execute_script("arguments[0].click();", second_download_button)

# Attendre un court instant pour permettre le téléchargement du fichier
time.sleep(5)

# Spécifier le chemin du fichier ZIP téléchargé
zip_file_path = "C:\\Users\\GAMERWORLD\\Downloads\\ᶠᵘᶜᵏ ᵃˡˡ.zip"

# Spécifier le dossier où extraire le contenu du fichier ZIP
extracted_folder_path = "C:\\Users\\GAMERWORLD\\Downloads\\programation\\2. Logicels, Tests\\SoundyCloud\\downloaded songs"

# Extraire le fichier ZIP dans le dossier spécifié
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

# Supprimer le fichier ZIP après l'extraction
os.remove(zip_file_path)

# Fermer la fenêtre du navigateur
driver.quit()
