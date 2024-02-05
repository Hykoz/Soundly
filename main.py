from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import zipfile
import os
import shutil
import schedule
from tqdm import tqdm

def run_script():
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
    extracted_folder_path = "C:\\Users\\GAMERWORLD\\Downloads\\programation\\2. Logicels, Tests\\Soundly\\Soundly\\downloads"

    # Supprimer récursivement le contenu du dossier
    shutil.rmtree(extracted_folder_path, ignore_errors=True)

    # Extraire le fichier ZIP dans le dossier spécifié
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder_path)

    # Supprimer le fichier ZIP après l'extraction
    os.remove(zip_file_path)

    # Fermer la fenêtre du navigateur
    driver.quit()

        # Définir la durée totale en secondes
    duree_totale = 600  # 10 minutes

    # Créer une barre de progression avec tqdm
    barre_progression = tqdm(total=duree_totale, desc="Progression")

    # Boucle pour simuler une tâche prenant du temps
    while barre_progression.n < barre_progression.total:
        # Simuler une petite tâche
        time.sleep(1)
        # Mettre à jour la barre de progression
        barre_progression.update(1)

    # Fermer la barre de progression à la fin
    barre_progression.close()

    os.system("cls")


# Exécuter le script immédiatement la première fois
run_script()
 

# Planifier l'exécution toutes les 10 minutes
schedule.every(1).seconds.do(run_script)

# Exécuter le script indéfiniment
while True:
    schedule.run_pending()
    time.sleep(1)