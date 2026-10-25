from random import *
from string import *
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Générer un mot de passe sécurisé.")
fenetre.geometry("400x300")


mon_texte = tk.Label(fenetre, text="Générateur de mot de passe")
mon_texte.pack()
mon_bouton = tk.Button(fenetre, text="Générer")
mon_bouton.pack()

var_minuscules = tk.BooleanVar(value=True)
var_majuscules = tk.BooleanVar(value=True)
var_chiffres = tk.BooleanVar(value=True)
var_ponctuations = tk.BooleanVar(value=True)

case_minuscules = tk.Checkbutton(fenetre, text="Minuscules", variable=var_minuscules)
case_minuscules.pack()
case_majuscules = tk.Checkbutton(fenetre, text="Majuscules", variable=var_majuscules)
case_majuscules.pack()
case_chiffres = tk.Checkbutton(fenetre, text="Chiffres", variable=var_chiffres)
case_chiffres.pack()
case_ponctuation = tk.Checkbutton(fenetre, text="Ponctuations", variable=var_ponctuations)
case_ponctuation.pack()

label_taille = tk.Label(fenetre, text="Longueur du mot de passe (min 8) :")
label_taille.pack()
champ_taille = tk.Entry(fenetre, width=10) 
champ_taille.insert(0, "12")
champ_taille.pack()

label_resultat = tk.Label(fenetre, text="Ton mot de passe apparaîtra ici", font=("Arial", 10, "bold"))
label_resultat.pack(pady=10)

#Fonction qui pose les questions
def poser_question(question):
    while True:
        choix = input(f"{question} (O/N) : \n").strip().upper()
        if choix == "O":
            return True
        elif choix == "N":
            return False
        print("Seulement le choix entre O et N.")

#Fonction qui génère le mot de passe
def generer_un_mdp(longueur, options):
    construction = ""
    mdp_list = []
    if options["minuscules"]:
        construction += ascii_lowercase
        mdp_list.append(choice(ascii_lowercase))
    if options["majuscules"]:
            construction += ascii_uppercase
            mdp_list.append(choice(ascii_uppercase))
    if options["chiffres"]:
            construction += digits
            mdp_list.append(choice(digits))
    if options["ponctuations"]:
            construction += punctuation
            mdp_list.append(choice(punctuation))

    if not construction:
        return "Impossible de générer un mot de passe sans aucun caractère !"

    reste = longueur - len(mdp_list)
    #Ajout des caractère manquant, mélange et regroupement
    mdp_list.extend(choices(construction, k=reste)) 
    shuffle(mdp_list)
    mdp = "".join(mdp_list)
    return mdp

#Foction qui gère et demande la longueur souhaitée
def demander_longueur():
    while True:
        try:
            longueur = int(input("Taille du mot de passe souhaitée : \n"))
            if longueur >= 8:
                return longueur
            else:
                print("La longueur doit être supérieure ou égale à 8.")
        except:
            print("Erreur : tu dois entrer un nombre entier (ex: 12).")


autre_choix = True
while autre_choix:
    garder_choix = False
    while not garder_choix:
        # Dictionnaire des choix utilisateur (ex: minuscules : True)
        options = {
            "minuscules": poser_question("Tu veux des minuscules"),
            "majuscules": poser_question("Tu veux des majuscules"),
            "chiffres": poser_question("Tu veux des chiffres"),
            "ponctuations": poser_question("Tu veux de la ponctuation")
        }

        # Récapitulatif des choix
        print("\n--- Récapitulatif de tes choix ---")
        for categorie, activee in options.items():
            if activee:
                statut = "OK"
            else:
                statut = "OK pas de"
            print(statut, categorie)
        print("----------------------------------\n")

        # Demander confirmation
        garder_choix = poser_question("Veux-tu garder ces choix")
        
        if not garder_choix:
            print("\nOK, refait tes choix.\n")

    print("\nChoix sauvegardés !")

    taille = demander_longueur()
    print("Voilà un mot de passe sécurisé : ", generer_un_mdp(taille, options))

    autre_choix = poser_question("Veux-tu un autre mot de passe sécurisé")
    if autre_choix:
         print("\n------- OK préparation ... -------")

print("\nMerci de votre visite.")

fenetre.mainloop()