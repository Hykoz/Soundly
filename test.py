import time
from tqdm import tqdm

# Définir la durée totale en secondes
duree_totale = 40  # 10 minutes

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

print("Tâche terminée!")
