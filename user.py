#!/usr/bin/python3
##########################################
# File Name:	user.py
# Author:		Group 3
# Date:			10/24/14
# Class:		360
# Assignment:	Tic-Tac-Toe
# Purpose:		user of the game
########################################

"""
The User Module
"""

from player import *
from board import *

# inherits from player
class user (player): 
	"""Represents a user player"""
	
	def __init__ (self, name, symbol, wins, losses, draws) :
		""" Initializes an object of user
		
		passes the name and symbol entered to the player initializer
		sets the wins, losses, and draws
		"""
		player.__init__(self, name, symbol)
		self._wins = wins
		self._losses = losses
		self._draws = draws
		
	def getWins (self) :
		""" returns the user's number of wins """
		return self._wins
		
	def getLosses (self) :
		""" returns the user's number of losses """
		return self._losses
		
	def getDraws (self) :
		""" returns the user's number of draws """
		return self._draws
		
	def printData (self) :
		""" prints the player data as well as the user's number of 
			wins, losses, and draws """
		self.printPlayer()
		print ("Wins:", self._wins, "Losses:", self._losses, \
				"Draws:", self._draws)
		
	def placement (self, board) :
		""" asks the user to place a symbol to the board
		
		if the place chosen is taken or invalid, keep on asking for 
		input until it is valid
		"""
		spotTaken = True
		
		while spotTaken : 
			print("")
			print ("X?")
			x = int(input(">>> "))
			while x < 0 and x > 4 : 
				x = int(input(">>> "))
			
			print("Y?")
			y = int(input(">>> "))
			while y < 0 and y > 4 :
				y = int(input(">>> "))
			
			point = Point(x,y)
			spotTaken = board.spotTaken(point)
		
		return Point(x,y)

	def incrementWins(self) :
		""" increases the user's number of wins by 1 """
		self._wins = self._wins + 1

	def incrementLosses(self) :
		""" increases the user's number of losses by 1 """
		self._losses = self._losses + 1
		
	def incrementDraws(self) :
		""" increases the user's number of draws by 1 """
		self._draws = self._draws + 1
