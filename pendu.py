#python 3.10.0
#-*-coding:Latin-1 -*

import variable as var
import functions as func

print ("Welcome to the hanged man \n", "here are the rules:\n",\
        "-You have only 8 strikes to find the mystery word\n","-If you score reach 0 strikes, \
            you will be hanged\n","So choose well your letter and enjoy the game !")

while var.nb_luck > 0:

    #init phase
    if var.check_init == False: #on verifie que l on rendre dans la phase init une fois lors du lancement

        var.rand_word_j = func.randomWordSelect(var.liste_mots)

        var.myst_word_j = func.wordToMystWord_init_(var.rand_word_j)

        var.name_j1 = input ("Please player enter your name: ")

        var.score_j1,var.j_exist = func.manageScore(var.name_j1)

        func.functComment(var.name_j1,var.score_j1,var.myst_word_j)

        var.check_init=True
    else:
        pass
    #Enter a letter 
    print("\n Joueur {} veuillez entrer une lettre: ".format(var.name_j1))
    var.letter_j1 = input ().lower()
    var.myst_word_j, var.letter_find_j = func.wordToMystWord(var.myst_word_j,var.rand_word_j,var.letter_j1)

    if var.letter_find_j == True:
        var.nb_luck -= 1
        var.score_j1= var.score_j1
        func.functComment(var.name_j1,var.score_j1,var.myst_word_j)
        continue
    else:
        var.nb_luck -= 1
        var.score_j1 = var.nb_luck
        func.functComment(var.name_j1,var.score_j1,var.myst_word_j)
        continue

if var.score_j1 > 0:
    print("Bravo joueur {} vous avez gagne".format(var.name_j1))
    func.stockerScore(var.name_j1,var.score_j1)
else:
    print("Malheureusement joueur {} vous avez perdu".format(var.name_j1))
    func.stockerScore(var.name_j1,var.score_j1)


