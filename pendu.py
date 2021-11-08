# python 3.10.0
# -*-coding:utf-8 -*-
import pickle
import random



class Players:
    """...................."""

    def __init__(self, name_player="None")->None:
        self.name_player = name_player
    
    def get_player_letter(self)->str:
        while True:
            self.player_letter = input(
                f"Please enter an alphabetic letter: "
                ).lower()
            if self.player_letter.isalpha() and (len(self.player_letter)>0 and len(self.player_letter)<2):
                return self.player_letter

    @property
    def players_history_scores(self) -> int:
        try:
            with open("HangingGame_Scores_Storage", "rb") as readable_file_scores:
                self.get_file_scores = pickle.Unpickler(readable_file_scores)
                history_scores = self.get_file_scores.load()

                if self.name_player in history_scores:
                    return history_scores[self.name_player]
                return 0

        except (EOFError, FileNotFoundError) as notexist:
            return 0
        except pickle.PicklingError as piPI:
            raise f"{piPI} error occurred, {self.get_file_scores} object doesn't support pickling"
        except pickle.UnpicklingError as piUN:
            raise f"{piUN} error occurred, {self.get_file_scores} file is corrupted"

    def write_on_file_history(self, player_information: dict) -> None:

        with open("HangingGame_Scores_Storage", "a+b") as writing_file_scores:
            self.set_file_scores = pickle.Pickler(writing_file_scores)
            self.set_file_scores.dump(player_information)
    
    def player_score(self, mystery_word:str)->int:
        count=0
        for i in mystery_word:
            if i == "*":
                count+=1
        return len(mystery_word) - count
    

class MysteryWord:
    
    def __init__(self,player_letter:str)->None:
        self.player_letter = player_letter
        self.mystery_words = ["banane","papa","ciel","tisch","kissen","schrank","stuttgart","toulouse","deuschland","france"]
    
    def one_word_selection(self)->str:
        self.mystery_word_index = random.randint(0,len(self.mystery_words))
        
        return "".join(self.mystery_words[self.mystery_word_index])
    
    def display_mystery_word(self,word:str)->None:
        i=0
        self.displayed_word = []
        while i < len(word):
            if self.player_letter is word[i]:
                self.displayed_word[i] = self.player_letter
            self.displayed_word[i] = "*"
            i+=1
        print(f"Mystery word: {self.display_mystery_word}")


    
    

        


def main():
    print("hello")
    # 1:The player gives his name ( class Player)
    # 2:We check if this player already exist if yes we get is old score
    # if no we add it as "player":<score>
    # 3:Selct the mystery word( class MysteryWord)
    # Current information display (class GameInformationDisplay)
    # Get the player letter (Player)
    # Check if the player letter == mystery word
    # Manage the score


if __name__ == "__main__":
    main()
