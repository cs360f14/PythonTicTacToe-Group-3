#!/usr/bin/python3
##########################################
# File Name:main.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:to run the game
########################################

from game import *
"""
The Main Module
"""

def main() :
	""""initiliaze a new game and set the name of user and opponent
		then draw the board and enter the loop for the game. For each 
		game get a move then draw and continue until a win or draw. 
		After a game is over print the user data and ask the user if 
		they want to continue or stop playing
		"""
	gameQuit = False

	Game = game()
	Game.nameUser()
	print("")
	Game.printUserData()
	print("")
	Game.nameOpponent()
	print("")0
	Game.printOpponentData()
	print("")
	Game.draw()
	
	while not gameQuit :
		
		while Game.gameRunning() :
			point = Game.getPlacement()
			Game.turn (point)
			Game.draw()
		
		print()
		Game.printUserData()
		
		print("Continue playing (Yes or No)? : Y or N")
		choice = input (">>> ")
		while ( (choice != "Y") and (choice != "N") ) : 
			print ("Y or N?")
			choice = input(">>> ")
			
		if choice == "Y" :
			gameQuit = False
			Game.resetGame()
		else :
			gameQuit = True

if __name__=="__main__" :
	main()

