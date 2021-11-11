#Python3.10.0
#-*-coding:utf-8 -*-
import random
import pickle

class Player:
    
    def __init__(self):
        pass

    def get_name(self)->str:
        """The player need to enter his name. This methode will return player_name. The player can enter only an alphabetic character"""
        
        while True:
            self.player_name = input("Please player enter your name:").lower()
            if self.player_name.isalpha():
                return self.player_name

    def get_letter(self)->str:
        """The player need to enter an alphabetic letter. It will return his letter as output."""
        
        while True:
            self.player_letter = input("Please enter an alphabetic letter: ").lower()
            if self.player_letter.isalpha() and (len(self.player_letter) > 0 and len(self.player_letter) < 2):
                return self.player_letter
        
    def score(self,secret_word_identified:str)->int:
        """Take as input a secret word identified.The player score will be the difference between the word length and the number of letter which is still hid, and return player_score.""" 
        
        count = secret_word_identified.count("*")
        return len(secret_word_identified) - count



class ScoreRecording:

    def __init__(self):
        pass
    
    def import_score_from_file(self,player_name:str)->int:
        """Take player_name as input, and return recording_score of the following player name"""
        
        try:
            with open("HangingGame_Scores_Storage","r+b") as read_file_scores:
                self.unpickle_file_scores = pickle.Unpickler(read_file_scores)
                self.get_recording_scores = self.unpickle_file_scores.load()

                if player_name in self.get_recording_scores:
                    return self.get_recording_scores[player_name]
            return 0
        except (EOFError, FileNotFoundError):
            return 0
        except pickle.PicklingError as p:
            raise f"{p} error occurred, {self.unpickle_file_scores} object doesn't support pickling"
        except pickle.UnpicklingError as e:
            raise f"{e} error occurred, {self.unpickle_file_scores} file is corrupted"


    def export_score_to_file(self,player_name:str,player_score:int)->None:
        """take as input player_name and player_score. Those parameters will be store inside a file as dictionnary type with player_name as key and player_score as value."""											Before storing, it checks if the name already exist if yes it will replace the old score, if not it adds the key and his value at the end of the file

        with open("HangingGame_Scores_Storage", "w+b") as write_file_scores:
            self.get_recording_scores[player_name] = player_score
            self.set_file_scores = pickle.Pickler(write_file_scores)
            self.set_file_scores.dump(self.get_recording_scores)


class SecretWord:

    def __init__(self):...
    
    def select_secret_word(self)->None:...

    def identify_letter_in_word(self,player_letter:str)->str:...

    def display_secret_word(self)->None:...


class Game(Player,SecretWord):

    def __init__(self):...
    
    def score_control(self,recording_score,player_score)->int:...
    
    def display_player_information(self,player_name:str,player_score:int)->None:...

    def game(self)->None:...


if __name__ == "__main__":
    ...