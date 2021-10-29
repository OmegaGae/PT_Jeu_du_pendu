import pickle
import os




def pin(name_j):
    dict_score = {name_j: 8,}
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
            dict_score_get= dict_depickler.load()

            for cle in dict_score_get.keys():
                if cle == name_j:#le joueur est present dans le dict et on recup le score 
                    score_j1= dict_score_get[cle] #variable globale 
                    j1_exist=True
                else:
                    pass
        
    if j1_exist == False:
        score_j1=8
        dict_score_none={name_j:score_j1}
        with open("hangingGame", "wb") as fichier_score_wb :    
            #le joueur n existe pas ds le dict 
                
                dict_pickler_2 =pickle.Pickler(fichier_score_wb)
                dict_pickler_2.dump(dict_score_none)
    else:
        pass
        

    return score_j1,j1_exist


