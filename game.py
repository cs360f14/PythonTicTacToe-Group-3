#!/usr/bin/python3
##########################################
# File Name:game.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:to run the game
########################################

"""
The Game Module
"""

from user import *
from hai import *
from eai import *
from board import *

class game :
	""" the game class handles all functionality of the game"""
	
	def __init__ (self) :
		""" Initializes an object of game creating a new board, setting
		the user to go first, the number of games to 1, game running to
		true, and the user turn to true		
		"""
		self._board = Board()
		self._userFirst = True
		self._gameNum = 1
		self._gameRunning = True
		self._userTurn = True
		print("Tic-Tac-Toe Game 1")
		
	def nameUser (self) :
		"""
		asks the user for there name and a valid symbol
		"""
		print ("Enter name:")
		name = input(">>> ")
		print ("X or O?")
		symbol = input(">>> ")
		while ((symbol != "X") and (symbol != "O") ) :
			print ("X or O?")
			symbol = input(">>> ")
		
		self._user = user (name, symbol, 0, 0, 0)
		
	def userSymbolIsX (self) : 
		"""returns true if the user symbol is X	"""
		userIsX = False
		if (self._user.getSymbol() == "X" ) :
			userIsX = True
		return userIsX
	
	def printUserData (self) : 
		"""calls the user print Data function"""
		self._user.printData()
	
	def nameOpponent (self) :
		"""asks the user to name the AI oppenent and the difficulty"""
		print ("Enter opponent difficulty (Easy or Hard): E or H?")
		difficulty = input (">>> ")
		while ( (difficulty != "E") and (difficulty != "H") ) : 
			print ("E or H?")
			difficulty = input(">>> ")
		
		print("Enter opponent name: ")
		aiName = input(">>> ")
		
		if (self.userSymbolIsX()) :
			aiSymbol = "O"
		else :
			aiSymbol = "X"
			
		if (difficulty == "E") :
			self._ai = EAI (aiName, aiSymbol)
			
		if (difficulty == "H") :
			self._ai = HAI (aiName, aiSymbol)
			
	def printOpponentData (self) : 
		"""calls the AI print function """
		self._ai.printAI()
		
	def getTurn(self) : 
		""" returns the symbol of whose turn it is """
		if (self._userTurn ==  True) :
			return self._user.getSymbol()
		else :
			return self._ai.getSymbol()
			
	def getPlacement (self) :
		""" checks whose turn it is and calls their respective placement
			functions. """
		if (self._userTurn == True) :
			point = self._user.placement(self._board)
		else :
			print("")
			print ("Opponent's turn...")
			print ("")
			point = self._ai.placement(self._board)
		
		return point
		
	def turn (self, point) :
		"""
		accepts a point and places that point in the board
		then checks if anyone has won or if the board is full
		and the game is a tie. Then if either win or draw increment
		the correct info in the user. Then update the turn.
		"""
		symbol = self.getTurn()
		
		print ("Entered point is: (",point.x,",", point.y,")")
		print ("")
		
		self._board.insertMove(point, symbol)
		
		win = self._board.checkWin(symbol)
		draw = self._board.isFull()
		
		if win :
			self._gameRunning = False
			if symbol == self._user.getSymbol() :
				self._user.incrementWins()
			elif symbol == self._ai.getSymbol():
				self._user.incrementLosses()
		elif draw :
			self._user.incrementDraws()
			self._gameRunning = False
		else :
			self.updateTurn()
		
	def gameRunning (self) : 
		"""returns whether the game is running or not"""
		return self._gameRunning
	
	def updateTurn (self) :
		""" switches the turn between the ai and user"""
		if self._userTurn == True :
			self._userTurn = False
		else :
			self._userTurn = True
		
	def resetGame (self) : 
		""" resets the board, whether the user is first or not, and
			restart the game. Then print the  next game number and 
			new board"""
		self._board.reset()
		self._gameNum = self._gameNum + 1
		if self._userFirst :
			self._userFirst = False
			self._userTurn = False
		else :
			self._userFirst = True
			self._userTurn = True
		
		self._gameRunning = True
		print("")	
		print("Tic-Tac-Toe Game", self._gameNum)
		print("")
		self.draw()
		
		
	def draw(self) :
		""" prints the board"""
		self._board.printBoard()

