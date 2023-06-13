

with open("contenu.txt", "r") as fichier:
    contenu = fichier.read()




chemin_dossier = input("folder path: ")
fichier_chemin = chemin_dossier + "\\" + "index.py"
with open(fichier_chemin, "w") as f:
        f.write(contenu)
        f.close()
        print("projet create succefuly")



        

