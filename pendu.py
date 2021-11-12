# Python3.10.0
# -*-coding:utf-8 -*-
import random
import pickle
import typing


class Player:
    def __init__(self):
        pass

    def get_name(self) -> str:
        """The player need to enter his name.
        This methode will return player_name.
        The player can enter only an alphabetic character"""

        while True:
            self.player_name = input("Please player enter your name: ").lower()
            if self.player_name.isalpha():
                print("\n")
                return self.player_name

    def get_letter(self) -> str:
        """The player need to enter an alphabetic letter.
        It will return his letter as output."""

        while True:
            self.player_letter = input("Please enter an alphabetic letter: ").lower()
            if self.player_letter.isalpha() and (
                len(self.player_letter) > 0 and len(self.player_letter) < 2
            ):
                print("\n")
                return self.player_letter

    def score(self, secret_word_identified: str) -> int:
        """Take as input a secret word identified.
        The player score will be the difference between the word length
        and the number of letter which is still hid, and return player_score."""

        count = secret_word_identified.count("*")
        return len(secret_word_identified) - count


class ScoreRecording:
    def __init__(self):
        pass

    def import_score_from_file(self, player_name: str) -> int:
        """Take player_name as input, and return recording_score of the following player name"""

        try:
            with open("HangingGame_Scores_Storage", "r+b") as read_file_scores:
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

    def export_score_to_file(self, player_name: str, player_score: int) -> None:
        """take as input player_name and player_score.
        Those parameters will be store inside a file as dictionnary type
        with player_name as key and player_score as value."""

        with open("HangingGame_Scores_Storage", "w+b") as write_file_scores:
            self.get_recording_scores[player_name] = player_score
            self.set_file_scores = pickle.Pickler(write_file_scores)
            self.set_file_scores.dump(self.get_recording_scores)


class SecretWord:
    def __init__(self):
        self.secret_word_identified = []

    def select_secret_word(self) -> None:
        """Randomly selection of one word among a list of words.
        That word will be store in attribut secret_word"""

        self.liste_secret_word = [
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
        indice_random = random.randint(0, len(self.liste_secret_word) - 1)
        self.secret_word = self.liste_secret_word[indice_random]

    def identify_letter_in_word(
        self, player_letter: typing.Optional[str] = None
    ) -> str:
        """take player letter as input, check if player letter
        is inside secret word, and return secret word regarding the identification"""

        if type(player_letter) == str:
            for i, e in enumerate(list(self.secret_word)):
                if player_letter == e:
                    self.secret_word_identified[i] = e
            return "".join(self.secret_word_identified)
        else:
            for e in self.secret_word:
                self.secret_word_identified.append("*")

            return "".join(self.secret_word_identified)

    def display_secret_word(self) -> None:
        str_secret_word_identified = "".join(self.secret_word_identified)
        print(f"Secret word: {str_secret_word_identified}")


class Game(Player, SecretWord, ScoreRecording):
    def __init__(self):
        self.play_game = True

    def score_control(self, recording_score: int, player_score: int) -> int:
        """Computing the new player recording score and return it"""
        recording_score += player_score
        return recording_score

    def display_player_information(
        self,
        player_name: str,
        player_score: int,
        player_letter: typing.Optional[str] = None,
    ) -> None:
        """print name_player:str score_player:int and last_player_letter:list"""

        if type(player_letter) == str:
            self.storage_player_letter.append(player_letter)
            print(
                f" Player name: {player_name}\n",
                f"Current point: {player_score}\n",
                f"Last letters enter: {self.storage_player_letter}",
            )
        else:
            print(f"Player name: {player_name}\n", f"Current point: {player_score}\n")

    def game_launcher(self) -> int:
        """Launch all init state of the game and return player recording score"""
        self.laps_number = 0
        self.storage_player_letter = []
        self.secret_word_identified = []
        self.get_recording_scores = {}

        print("Welcome To Hanging Game !\n")
        self.game_player_name = self.get_name()
        recording_score = self.import_score_from_file(self.game_player_name)
        self.select_secret_word()
        secret_word = self.identify_letter_in_word()
        current_player_score = self.score(secret_word)
        self.display_player_information(self.game_player_name, current_player_score)
        self.display_secret_word()

        return recording_score

    def game_stopper(self):
        """Return the state of game based on the player, if he still wants to play"""

        while True:
            play = input("Do you still want to play ? Y/N : \n").lower()
            if (play.isalpha() and len(play) == 1) and play == "y":
                return True
            elif (play.isalpha() and len(play) == 1) and play == "n":
                return False
            else:
                print("Please enter the specify input :\n")
                continue

    def game(self) -> None:
        """main function; handle all the game by calling respectively
        each method needed"""

        while self.play_game:
            recording_score = self.game_launcher()
            while self.laps_number < 10:
                player_letter = self.get_letter()
                secret_word = self.identify_letter_in_word(player_letter)

                current_player_score = self.score(secret_word)
                if current_player_score == len(secret_word):
                    print(
                        f"Congratulation you've found the secret word : {self.secret_word}!\n"
                    )
                    break
                self.laps_number += 1
                if self.laps_number == 10:
                    print(
                        "Unfortunately you've lost !\n",
                        f"the secret word was :{self.secret_word} !\n",
                        "The next time may be your lucky egnima !",
                    )
                    break

                self.display_player_information(
                    self.game_player_name, current_player_score, player_letter
                )
                self.display_secret_word()

            recording_score = self.score_control(recording_score, current_player_score)
            print(f"here is your historical score:{recording_score}")
            self.export_score_to_file(self.game_player_name, recording_score)
            self.play_game = self.game_stopper()

        print("Thank you for your time playing this game !\nGood bye !\n")


if __name__ == "__main__":
    game = Game()
    game.game()
