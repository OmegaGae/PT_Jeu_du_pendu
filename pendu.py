# python 3.10.0
# -*-coding:utf-8 -*-
import pickle
import random


class Players:
    """...................."""

    def __init__(self) -> None:
        self.first_display = True
        self.first_open_file = False
        self.storage_player_letter = []

    def get_player_letter(self) -> str:
        """Get player letter"""
        
        while True:
            self.player_letter = input(
                f"Please enter an alphabetic letter: ").lower()
            if self.player_letter.isalpha() and (
                len(self.player_letter) > 0 and len(self.player_letter) < 2
            ):
                self.storage_player_letter.append(self.player_letter)
                return self.player_letter

    
    def players_history_scores(self) -> int:
        """Get the score of the current player \
            if he has already played this game"""
        try:
            self.first_open_file = False
            with open("HangingGame_Scores_Storage", "rb") as readable_file_scores:
                self.get_file_scores = pickle.Unpickler(readable_file_scores)
                self.history_scores = self.get_file_scores.load()

                if self._name_player in self.history_scores:
                    print("yoooooooooooooo\n")
                    return self.history_scores[self._name_player]
                return 0

        except (EOFError, FileNotFoundError) as notexist:
            self.first_open_file =True
            return 0
        except pickle.PicklingError as piPI:
            raise f"{piPI} error occurred, {self.get_file_scores} \
                object doesn't support pickling"
        except pickle.UnpicklingError as piUN:
            raise f"{piUN} error occurred, {self.get_file_scores} \
                file is corrupted"

    def write_on_file_history(self, record_score: int) -> None:
        """Write on the file, data player such as 'player_name":score'"""
        if self.first_open_file :
             with open("HangingGame_Scores_Storage", "a+b") as writing_file_scores:
                self.history_scores ={self._name_player:0}
                self.set_file_scores = pickle.Pickler(writing_file_scores)
                self.set_file_scores.dump(self.history_scores)
        else: 
            with open("HangingGame_Scores_Storage", "w+b") as writing_file_scores:
                self.history_scores[self._name_player] = record_score
                self.set_file_scores = pickle.Pickler(writing_file_scores)
                self.set_file_scores.dump(self.history_scores)

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
        
        data = f"Player {nameplayer}:\n"
        data2 = f"Current point:{playerscore}\n"
        if self.first_display:
            print(data,data2)
            self.first_display = False
        else:
            data3 = f"Yours letters:{self.storage_player_letter}"
            print(data,data2,data3)


class MysteryWord:
    def __init__(self, letter ='none') -> None:
        self._player_letter = letter
        self.first_display = True
        self.displayed_word = []
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

    
    def player_letter(self,letter_player):
        self._player_letter = letter_player

    def one_word_selection(self) -> str:
        self.mystery_word_index = random.randint(0, len(self.mystery_words)-1)

        return "".join(self.mystery_words[self.mystery_word_index])

    def display_mystery_word(self, word: str) -> str:
        """display state of mystery word and return \
            this state as a string type"""
        
        if self.first_display:
            for e in word:
                self.displayed_word.append('*')
            
            self.first_display = False
            return "".join(self.displayed_word)

        elif self.first_display is not True and self._player_letter =='none':
            egnima_word = "".join(self.displayed_word)
            print(f"Mystery word: {egnima_word}\n")
            return egnima_word

        else:
            for i, e in enumerate(list(word)):
                if self._player_letter == e:
                    self.displayed_word[i] = self._player_letter
            
            egnima_word = "".join(self.displayed_word)
            print(f"Mystery word: {egnima_word}\n")
            return egnima_word

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
        print("Welcome to Hanging Game !")
        name_player1 = player1.name_player()
        player1_score_record = player1.players_history_scores()
        select_secret_word = secret_word.one_word_selection()
        state_secret_word = secret_word.display_mystery_word(select_secret_word)
        current_player_score = player1.player_score(state_secret_word)
        
        while laps_number < 12:
            player1.displayed_data_player(name_player1,current_player_score)
            state_secret_word = secret_word.display_mystery_word(select_secret_word)
            current_player_score =player1.player_score(state_secret_word)
            
            if current_player_score == len(state_secret_word):
                print(f"Congratulation you've found the secret word : ")
                print(f"{select_secret_word} !")
                break
            
            player1_letter = player1.get_player_letter()
            secret_word.player_letter(player1_letter)
            laps_number+=1

        if laps_number == 12:
            print("Unfortunately you've lost, ")
            print(f"the secret word was :{select_secret_word} !")
            print(f"The next time may be your lucky egnima !")
        
        player1_score_record+=current_player_score
        print(f"here are your historical score:{player1_score_record}")
        player1.write_on_file_history(player1_score_record)
        play_game = state_of_game()
    
    print("Thank you for your time playing this game !\nGood bye !\n")
    

if __name__ == "__main__":
    main()
