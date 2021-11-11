#Python3.10.0
#-*-coding:utf-8 -*-
import random
import pickle

class Player:
    
    def __init__(self):
        pass

    def get_name(self)->str:
        """The player need to enter his name. \
            This methode will return player_name. \
                The player can enter only an alphabetic character"""
        while True:
            self.player_name = input("Please enter an alphabetic letter:").lower()
            if self.player_name.isalpha():
                return self.player_name


    def get_letter(self)->str:...

    def score(self,secret_word_identified:str)->int:...


class ScoreRecording:

    def __init__(self):...
    
    def import_score_from_file(self,player_name:str)->int:...

    def export_score_to_file(self,player_name:str,player_score:int)->None:...


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