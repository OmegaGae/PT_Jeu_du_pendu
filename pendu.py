# python 3.10.0
# -*-coding:utf-8 -*-
import pickle
import random


class Players:
    """...................."""

    def __init__(self) -> None:
        self.first_display = True

    def get_player_letter(self) -> str:
        """Get player letter"""
        self.storage_player_letter = []
        while True:
            self.player_letter = input(f"Please enter \
                an alphabetic letter: ").lower()
            if self.player_letter.isalpha() and (
                len(self.player_letter) > 0 and len(self.player_letter) < 2
            ):
                self.storage_player_letter.append(self.player_letter)
                return self.player_letter

    @property
    def players_history_scores(self) -> int:
        """Get the score of the current player \
            if he has already played this game"""
        try:
            with open("HangingGame_Scores_Storage", "rb") as readable_file_scores:
                self.get_file_scores = pickle.Unpickler(readable_file_scores)
                history_scores = self.get_file_scores.load()

                if self._name_player in history_scores:
                    return history_scores[self._name_player]
                return 0

        except (EOFError, FileNotFoundError) as notexist:
            return 0
        except pickle.PicklingError as piPI:
            raise f"{piPI} error occurred, {self.get_file_scores} \
                object doesn't support pickling"
        except pickle.UnpicklingError as piUN:
            raise f"{piUN} error occurred, {self.get_file_scores} \
                file is corrupted"

    def write_on_file_history(self, player_information: dict) -> None:
        """Write on the file, data player such as 'player_name":score'"""
        with open("HangingGame_Scores_Storage", "a+b") as writing_file_scores:
            self.set_file_scores = pickle.Pickler(writing_file_scores)
            self.set_file_scores.dump(player_information)

    def player_score(self, mystery_word: str) -> int:
        """Return player score which is egal to the number of words found"""
        count = 0
        if self.first_display:
            return 0
        else:
            for i in mystery_word:
                if i == "*":
                    count += 1
            return len(mystery_word) - count

    def name_player(self) -> str:
        """Retrun the name of current player"""
        while True:
            self._name_player = input("Please Player enter your name: ")
            if self._name_player.isalpha():
                return self._name_player

    def displayed_data_player(self,nameplayer,playerscore) -> None:
        
        data = f"Player {nameplayer} :\n"
        data2 = f"Current point:{playerscore}\n"
        if self.first_display:
            print(data, data2)
            self.first_display = False
        else:
            data3 = f"You have already enter \
                those letters:{self.storage_player_letter}\n"
            print(data, data2, data3)


class MysteryWord:
    def __init__(self, player_letter ='none') -> None:
        self.player_letter = player_letter
        self.first_display = True
        self.mystery_words = [
            "banane",
            "papa",
            "ciel",
            "tisch",
            "kissen",
            "schrank",
            "stuttgart",
            "toulouse",
            "deuschland",
            "france",
        ]
    
    def player_letter(self,letter:str)-> None:
        self._player_letter = letter

    
    def one_word_selection(self) -> str:
        self.mystery_word_index = random.randint(0, len(self.mystery_words))

        return "".join(self.mystery_words[self.mystery_word_index])

    def display_mystery_word(self, word: str) -> str:
        """display state of mystery word and return \
            this state as a string type"""
        i = 0
        self.displayed_word = []
        if self.first_display:
            while i < len(word):
                self.displayed_word[i]= '*'
                i+=1
            print(f"Mystery word: {self.display_mystery_word}\n")
            self.first_display = False
            return "".join(self.displayed_word)
        else:
            while i < len(word):
                if self._player_letter is word[i]:
                    self.displayed_word[i] = self._player_letter
                self.displayed_word[i] = '*'
                i += 1
            print(f"Mystery word: {self.display_mystery_word}\n")
            return "".join(self.displayed_word)

def state_of_game()->bool:
    """Return the state of game based on the player, if he still want to play"""
    while True:
        play = input("Do you still want to play ? Y/N : \n").lower()
        if (play.isalpha() and len(play) == 1) and play =='y' :
            return True
        elif (play.isalpha() and len(play) == 1) and play =='n' :
            return False
        else:
            print("Please enter the specify input :\n")
            continue
            


def main():
    play_game =True
    while play_game == True:
        laps_number = 0
        player1 = Players()
        secret_word = MysteryWord()
        name_player1 = player1.name_player()
        player1_score_record = player1.players_history_scores(name_player1)
        select_secret_word = secret_word.one_word_selection()
        print("Welcome to Hanging Game !\n")
        
        while laps_number < 12:
            player1.displayed_data_player(name_player1,current_player_score)
            state_secret_word = secret_word.display_mystery_word(select_secret_word)
            current_player_score = Players.player_score(state_secret_word)
            player1_letter = player1.get_player_letter()
            secret_word.player_letter(player1_letter)
            laps_number+=1
            if current_player_score == len(state_secret_word):
                print(f"Congratulation you've \
                    found the secret word :{select_secret_word} !")
                break
        if laps_number == 12:
            print(f"Unfortunately you haven't \
                found the secret word :{select_secret_word} !")
            print(f"The next time may be your lucky egnima !")
        
        player1_score_record+=current_player_score
        data_player1 = {name_player1:player1_score_record}
        player1.write_on_file_history(data_player1)
        play_game = state_of_game()
    
    print("Thank you for your time playing this game !\nGood bye !\n")
    

if __name__ == "__main__":
    main()
