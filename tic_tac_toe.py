import random
import time
import sys
import os


class TicTacToe:
    board = ['_', '|', '_', '|', '_', '_', '|', '_', '|', '_', ' ', '|', ' ', '|', ' ']
    remaining_choices = ['1', ' ', '2', ' ', '3', ' ', '4', ' ', '5', ' ', '6', ' ', '7', ' ', '8', ' ', '9']
    player_game_piece = str
    comp_game_piece = str
    valid_board_choices = {1:0, 2:2, 3:4, 4:5, 5:7, 6:9, 7:10, 8:12, 9:14}
    valid_remaining_choices = {1:0, 2:2, 3:4, 4:6, 5:8, 6:10, 7:12, 8:14, 9:16}
    won_game = False
    players = int
    coin_toss = int

    def number_of_players(self):
        """
        Choose number of players. If only 1 player is selected, pc_choice is called to be opponent.
        """
        self.players = int(input("1 or 2 players? "))

        while self.players != 1 and self.players != 2:
            self.players = int(input("Please select 1 or 2 players: "))

        if self.players == 1:
            self.player_game_piece = input("Would you like to be X or O? ").upper()
            if self.player_game_piece == "X":
                self.comp_game_piece = "O"
            else:
                self.comp_game_piece = "X"

        elif self.players == 2:
            self.player_game_piece = input("Which piece would Player_1 like to be? X or O ").upper()
            if self.player_game_piece == "X":
                self.comp_game_piece = "O"
            else:
                self.comp_game_piece = "X"

        while self.player_game_piece.upper() != "X" and self.player_game_piece.upper() != "O":
            self.player_game_piece = input("Please choose between X or O ").upper()
        return self.players, self.player_game_piece

    def draw_board(self):
        """
        Draws the actual board, but also the remaining valid choices in a quantitative format
        so that it's a bit easier to know what your options are.
        """
        print("".join(self.board[:5]), end="  ")
        print("".join(self.remaining_choices[:6]))

        print("".join(self.board[5:10]), end="  ")
        print("".join(self.remaining_choices[6:12]))

        print("".join(self.board[10:15]), end="  ")
        print("".join(self.remaining_choices[12:]))

    def player_choice(self, game_piece):
        """
        Asks player for an input from 1 to 9 (possible locations where
        a piece can be put are in self.valid_choices defined in __init__ method)
        and then removes that choice from self.remaining_choices.
        """
        self.draw_board()

        choice = int(input("Please select a number from 1 to 9 "))
        print()
        while choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            choice = int(input("Please select a number from 1 to 9 "))
            print()
        if self.board[self.valid_board_choices[choice]] == game_piece or self.board[self.valid_board_choices[choice]] == self.comp_game_piece:
            choice = int(input("That space is already occupied,\n please select another number 1 to 9 "))
            print()
        else:
            self.remaining_choices.remove(str(choice))
            self.board[self.valid_board_choices[choice]] = game_piece
            self.remaining_choices.insert(self.valid_remaining_choices[choice], game_piece)
        return choice

    def pc_choice(self):
        """
        Method called if only one player is selected. pc_choice randomly selects one of the available locations
        from self.valid_remaining_choices
        """
        choice = random.randrange(1,10)
        if self.board[self.valid_board_choices[choice]] == " " or self.board[self.valid_board_choices[choice]] == "_":
            self.board[self.valid_board_choices[choice]] = self.comp_game_piece
            self.remaining_choices.remove(str(choice))
            self.remaining_choices.insert(self.valid_remaining_choices[choice], self.comp_game_piece)
        else:
            while self.board[self.valid_board_choices[choice]] != " " and self.board[self.valid_board_choices[choice]] != "_":
                choice = random.randrange(1, 10)
            self.board[self.valid_board_choices[choice]] = self.comp_game_piece
            self.remaining_choices.remove(str(choice))
            self.remaining_choices.insert(self.valid_remaining_choices[choice], self.comp_game_piece)
        return choice

    def game_over(self):
        """
        Checks self.board to see if a win condition (3 game pieces in a row) has been met.
        """
        if self.remaining_choices[0:5:2] == [self.player_game_piece] * 3:
            print("Player_1 Wins!")
            self.draw_board()
            self.won_game = True

        elif self.remaining_choices[0:5:2] == [self.comp_game_piece] * 3:
            print("Player_2 Wins!")
            self.draw_board()
            self.won_game = True

        elif self.remaining_choices[5:10:2] == [self.player_game_piece] * 3:
            print("Player_1 Wins!")
            self.draw_board()
            self.won_game = True
        elif self.remaining_choices[5:10:2] == [self.comp_game_piece] * 3:
            print("Player_2 Wins!")
            self.draw_board()
            self.won_game = True

        elif self.remaining_choices[10::2] == [self.player_game_piece] * 3:
            print("Player_1 Wins!")
            self.draw_board()
            self.won_game = True
        elif self.remaining_choices[10::2] == [self.comp_game_piece] * 3:
            print("Player_2 Wins!")
            self.draw_board()
            self.won_game = True

        elif self.remaining_choices[0:13:6] == [self.player_game_piece] * 3:
            print("Player_1 Wins!")
            self.draw_board()
            self.won_game = True
        elif self.remaining_choices[0:13:6] == [self.comp_game_piece] * 3:
            print("Player_2 Wins!")
            self.draw_board()
            self.won_game = True

        elif self.remaining_choices[2:14:6] == [self.player_game_piece] * 3:
            print("Player_1 Wins!")
            self.draw_board()
            self.won_game = True
        elif self.remaining_choices[2:14:6] == [self.comp_game_piece] * 3:
            print("Player_2 Wins!")
            self.draw_board()
            self.won_game = True

        elif self.remaining_choices[4::6] == [self.player_game_piece] * 3:
            print("Player_1 Wins!")
            self.draw_board()
            self.won_game = True
        elif self.remaining_choices[4::6] == [self.comp_game_piece] * 3:
            print("Player_2 Wins!")
            self.draw_board()
            self.won_game = True

        elif self.remaining_choices[0::8] == [self.player_game_piece] * 3:
            print("Player_1 Wins!")
            self.draw_board()
            self.won_game = True
        elif self.remaining_choices[0::8] == [self.comp_game_piece] * 3:
            print("Player_2 Wins!")
            self.draw_board()
            self.won_game = True

        elif self.remaining_choices[4:13:4] == [self.player_game_piece] * 3:
            print("Player_1 Wins!")
            self.draw_board()
            self.won_game = True
        elif self.remaining_choices[4:13:4] == [self.comp_game_piece] * 3:
            print("Player_2 Wins!")
            self.draw_board()
            self.won_game = True

    def play_game(self):
        """
        Flips coin to decide who goes first. Will continue loop until self.won_game = True
        """
        self.number_of_players()
        self.coin_toss = random.randint(1,2)

        ## Loop for if there is 1 player.
        if self.players == 1:
            if self.coin_toss == 1:
                print("Player_1 goes first.")
                time.sleep(2)
                while not self.won_game:
                    self.player_choice(self.player_game_piece)
                    self.game_over()
                    if self.won_game:
                        play_again = input("Would you like to play again? (Y/N) ").upper()
                        if play_again == "Y":
                            os.system("cls")
                            start_game = TicTacToe()
                            start_game.play_game()
                        else:
                            sys.exit()
                    self.pc_choice()
                    self.game_over()
                    if self.won_game:
                        play_again = input("Would you like to play again? (Y/N) ").upper()
                        if play_again == "Y":
                            start_game = TicTacToe()
                            start_game.play_game()
                        else:
                            sys.exit()

            else:
                print("Player_2 goes first.")
                time.sleep(2)
                while not self.won_game:
                    self.pc_choice()
                    self.game_over()
                    if self.won_game:
                        play_again = input("Would you like to play again? (Y/N) ").upper()
                        if play_again == "Y":
                            os.system("cls")
                            start_game = TicTacToe()
                            start_game.play_game()
                        else:
                            sys.exit()
                    else:
                        pass

                    self.player_choice(self.player_game_piece)
                    self.game_over()
                    if self.won_game:
                        play_again = input("Would you like to play again? (Y/N) ").upper()
                        if play_again == "Y":
                            os.system("cls")
                            start_game = TicTacToe()
                            start_game.play_game()
                        else:
                            sys.exit()
                    else:
                        pass

        ## Loop for if there are 2 players.
        elif self.players == 2:
            if self.coin_toss == 1:
                print("Player_1 goes first")
                while not self.won_game:
                    self.player_choice(self.player_game_piece)
                    self.game_over()
                    if self.won_game:
                        play_again = input("Would you like to play again? (Y/N) ").upper()
                        if play_again == "Y":
                            os.system("cls")
                            start_game = TicTacToe()
                            start_game.play_game()
                        else:
                            sys.exit()
                    print("Player_2's turn.")
                    self.player_choice(self.comp_game_piece)
                    self.game_over()
                    if self.won_game:
                        play_again = input("Would you like to play again? (Y/N) ").upper()
                        if play_again == "Y":
                            os.system("cls")
                            start_game = TicTacToe()
                            start_game.play_game()
                        else:
                            sys.exit()
                    print("Player_1's turn.")

            elif self.coin_toss == 2:
                print("Player_2 goes first")
                while not self.won_game:
                    self.player_choice(self.comp_game_piece)
                    self.game_over()
                    if self.won_game:
                        play_again = input("Would you like to play again? (Y/N) ").upper()
                        if play_again == "Y":
                            os.system("cls")
                            start_game = TicTacToe()
                            start_game.play_game()
                        else:
                            sys.exit()
                    print("Player_1's turn.")
                    self.player_choice(self.player_game_piece)
                    self.game_over()
                    if self.won_game:
                        play_again = input("Would you like to play again? (Y/N) ").upper()
                        if play_again == "Y":
                            os.system("cls")
                            start_game = TicTacToe()
                            start_game.play_game()
                        else:
                            sys.exit()
                    print("Player_2's turn.")


if __name__ == "__main__":
    start_game = TicTacToe()
    start_game.play_game()
