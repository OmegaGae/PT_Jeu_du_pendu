#python 3.10.0
#-*-coding:Latin-1 -*
import os
import random
import pickle


"""Creation of all functions for the jeu du pendu game"""

def manageScore(name_j):
    """Function for score management thanks to an object file \
        and it return the last score of the player"""
    score_j1=8
    dict_score = {name_j: score_j1}
    j1_exist=False
    file_empty = False
    inside_file_empty = False
    #check if file exist
    f_exist= os.path.exists("hangingGame")

    if f_exist == False:
        file_empty = True
    else:
        pass
    
    if file_empty ==True: #init file

        with open("hangingGame", "wb") as fichier_score_w :
            dict_pickler =pickle.Pickler(fichier_score_w)
            dict_pickler.dump(dict_score)
    else: 
        with open("hangingGame", "rb") as fichier_score_rb :   
            #on lit objt dict contenu dnas le fichier score
            dict_depickler =pickle.Unpickler(fichier_score_rb)
            dict_score= dict_depickler.load()
            
            for cle in dict_score.keys():
                if cle == name_j:#le joueur est present dans le dict et on recup le score 
                    score_j1= dict_score[cle] #variable globale 
                    j1_exist=True
                    break
                else:
                    pass
        
    if j1_exist == False:
        dict_score[name_j]=score_j1
        with open("hangingGame", "wb") as fichier_score_wb :    
            #le joueur n existe pas ds le dict 
                
                dict_pickler_2 =pickle.Pickler(fichier_score_wb)
                dict_pickler_2.dump(dict_score)
    else:
        pass
        

    return score_j1,j1_exist

def stockerScore(name_j, score_j):
    """Function for score storage in a file taking a dictionnary as object"""
    with open("hangingGame", "rb") as fichier_score_r :
        
        #on lit objt dict contenu dans le fichier score
        dict_depickler =pickle.Unpickler(fichier_score_r)
        dict_score_get= dict_depickler.load()

        #on stocke la valeur score_j dans ce dict
        dict_score_get[name_j]=score_j
       


    #on ouvre a nouveau le fichier en ecriture pour stocker le nouveau dict modifier precedemment
    with open("hangingGame", "wb") as fichier_score_w :
        
        dict_pickler_2 =pickle.Pickler(fichier_score_w)
        dict_pickler_2.dump(dict_score_get)
       


def randomWordSelect(list_words):
    """Function for word random selection"""
    n_word=len(list_words)
    num_selct=random.randrange(0,n_word)

    return list_words[num_selct]

def wordToMystWord_init_ (rand_word):
    """initialisation of the mystery word"""
    nb_letter=len(rand_word)
    myst_word=""
    i=0
    #mystery word init
    while i<nb_letter:
        myst_word +="*"
        i+=1
    
    return myst_word

def wordToMystWord (myst_word, rand_word,lettre_j):
    """adaptation of the mystery word according to the letter given by the player, \
        and return the mystery word """
    i=0
    letter_find=False
    list_myst_word= list(myst_word)
    list_rand_word= list(rand_word)
    for i,not_used in enumerate(list_rand_word):

        if list_rand_word[i] == lettre_j:
            list_myst_word[i]=lettre_j
            letter_find = True
            break
        else:
            pass
    myst_word="".join(list_myst_word)
    return myst_word, letter_find


def functComment (name_j, score_j,myst_word):
    """Function for displaying the current player information"""
    print("Joueur {0} \n Score = {1} \n Mot mystere : {2}.".format(name_j,score_j,myst_word))












