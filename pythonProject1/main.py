from multiprocessing.connection import answer_challenge
""" premier programme 
python 
apprendre la programmation """
def demander_age():
    age_input = 0
    while age_input == 0:
        age_str = input("quel est votre age?")

        try:
            age_input = int(age_str)
        except:
            print("ERREUR: vous devez rentrer un nombre pour l age ")
def demander_nom():
    reponse_nom = input("Quel est votre nom ?")

    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ?")
        try:
            reponse_nom = int(nom)
        except:
            print("ERREUR: veuillez entrer un nom ")
    return reponse_nom

nom=input("Quel est votre nom ?")

while nom=="":
    nom = input("Quel est votre nom ?")
    try:
        nom=int(nom)
    except:
        print("ERREUR: veuillez entrer un nom ")



age = 0
while age == 0 :
    age_str=input("quel est votre age?")

    try:
        age= int (age_str)
    except:
     print("ERREUR: vous devez rentrer un nombre pour l age ")
#print("fin de la boucle")
else:
    print("vous vous appelez" + nom , "vous avez " +str(age)  + "ans")
    print("l an prochain vous aurez " + str(age+1) + " ans" )
#
#
