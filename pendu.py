# Python3.10.0
# -*-coding:utf-8 -*-
import random
import pickle
import typing


class Player:
    def __init__(self):
        self._player_name = None
        self.score = 0

    def get_name(self) -> str:
        """The player need to enter his name.
        This methode will return player_name.
        The player can enter only an alphabetic character"""

        if self._player_name is not None:
            return self._player_name

        while True:
            self._player_name = input("Please player enter your name: ").lower()
            if self._player_name.isalpha():
                print("\n")
                return self._player_name

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


class ScoreRecording:
    def __init__(self, file: str = "HangingGame_Scores_Storage"):
        self.file = file
        self.scores = self._import_score_from_file()

    def get_player_score(self, player_name: str) -> int:
        return self.scores.get(player_name, 0)

    def _import_score_from_file(self) -> typing.Dict[str, int]:
        """Take player_name as input, and return recording_score of the following player name"""

        try:
            with open(self.file, "r+b") as f:
                return pickle.Unpickler(f).load()
        except (EOFError, FileNotFoundError):
            print(f"File {self.file} not found")
        except pickle.PicklingError as e:
            print(
                f"{e} error occurred, object contained on {self.file} doesn't support pickling"
            )
        except pickle.UnpicklingError as e:
            print(f"{e} error occurred, object contained on {self.file} is corrupted")
        return {}

    def update_player_score_and_export_to_file(
        self, player_name: str, player_score: int
    ) -> None:
        """take as input player_name and player_score.
        Those parameters will be store inside a file as dictionnary type
        with player_name as key and player_score as value."""

        self.scores[player_name] = player_score

        with open(self.file, "w+b") as f:
            self.set_file_scores = pickle.Pickler(f).dump(self.scores)


class SecretWord:
    def __init__(self):
        self.identified_letters = []
        self.secret_word = self._select_secret_word()

    def _select_secret_word(self) -> str:
        """Randomly selection of one word among a list of words.
        That word will be store in attribut secret_word"""

        liste_secret_word = [
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
        indice_random = random.randint(0, len(liste_secret_word) - 1)
        return liste_secret_word[indice_random]

    @property
    def identified_word(self):
        return "".join(
            [
                letter if letter in self.identified_letters else "*"
                for letter in self.secret_word
            ]
        )

    def identify_letter_in_word(
        self, player_letter: typing.Optional[str] = None
    ) -> bool:
        """take player letter as input, check if player letter
        is inside secret word, and return secret word regarding the identification"""

        if player_letter is not None and player_letter in self.secret_word:
            self.identified_letters.append(player_letter)
            return True
        return False


class Game:
    def __init__(self):
        self._reset_game()

    def _reset_game(self):
        self.play_game = True
        self.player = Player()
        self.word = SecretWord()
        self.score_recording = ScoreRecording()
        self.laps_number = 0

    def display_player_information(
        self,
        player_name: str,
        player_score: int,
        player_letter: typing.Optional[str] = None,
    ) -> None:
        """print name_player:str score_player:int and last_player_letter:list"""

        if type(player_letter) == str:
            print(
                f" Player name: {player_name}\n",
                f"Current point: {player_score}\n",
                f"Last letters enter: {self.word.identified_letters}",
            )
        else:
            print(f"Player name: {player_name}\n", f"Current point: {player_score}\n")

    def game_launcher(self) -> int:
        """Launch all init state of the game and return player recording score"""
        self._reset_game()

        print("Welcome To Hanging Game !\n")
        self.player.score = self.score_recording.get_player_score(
            self.player.get_name()
        )
        self.display_player_information(self.player.get_name(), self.player.score)
        print(self.word.identified_word)

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
            self.game_launcher()
            while self.laps_number < 10:
                player_letter = self.player.get_letter()

                if self.word.identify_letter_in_word(player_letter):
                    self.player.score += 1
                if self.word.identified_word == self.word.secret_word:
                    print(
                        f"Congratulation you've found the secret word : {self.word.secret_word}!\n"
                    )
                    break
                self.laps_number += 1
                if self.laps_number == 10:
                    print(
                        "Unfortunately you've lost !\n",
                        f"the secret word was :{self.word.secret_word} !\n",
                        "The next time may be your lucky egnima !",
                    )
                    break

                self.display_player_information(
                    self.player.get_name(), self.player.score, player_letter
                )
                print(self.word.identified_word)

            print(f"here is your score: {self.player.score}")
            self.score_recording.update_player_score_and_export_to_file(
                self.player.get_name(), self.player.score
            )
            self.play_game = self.game_stopper()

        print("Thank you for your time playing this game !\nGood bye !\n")


if __name__ == "__main__":
    game = Game()
    game.game()
