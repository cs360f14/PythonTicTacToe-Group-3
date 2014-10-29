#!/usr/bin/python3
##########################################
# File Name:board.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:board of the game
########################################


class Point:
	""" an object containing an x and a y """
	
	def __init__(self, x, y) :
		""" initializes a Point object setting the passed in values
			as the x and y """
		self.x = x
		self.y = y

class Board :
	"""A single game board"""
	
	def __init__(self) :
		""" Initializes a Board object 
	
		the Board is initialized as a 3x3 2D array of the character *
		"""
		self._gameBoard = [[0 for x in range(3)] for x in range(3)]
		for x in range(0,3) :
			for y in range (0,3) :
				self._gameBoard[y][x] = '*'
		self._numMoves = 0
	
	def printBoard(self) :
		""" prints Board object 
	
		prints in the form
			  1 2 3 x
			1 * * *
			2 * * *
			3 * * *
			y
		"""
		print("  1 2 3 x")
		for x in range(0,3) :
			print (x + 1, end=" ")
			for y in range (0,3) :
				print(self._gameBoard[x][y], end=" ")
			print()
		print("y")
		
	def insertMove(self, move, symbal) :
		""" Inserts a move (a point object containing an  
	
		the Board is initialized as a 3x3 2D array of the character *
		"""
		if(self.checkForRange(move) == True) :
			if (self.spotTaken(move) == False) :
				self._gameBoard[move.y - 1][move.x - 1] = symbal
				self._numMoves = self._numMoves + 1
				return True
			else :
				return False
		else :
			return False
		
	def reset (self) :
		""" resets the board back to the initial setting """
		self.__init__()

	def spotTaken (self, move) :
		""" checks if the point passed in has already been used
	
		The function returns true if the point passed in (which
		corresponds to an index of the 2D array) does not contain *.
		Otherwise, return false.
		"""
		taken = False
		if ('*' is not self._gameBoard[move.y -1][move.x -1]) :
			taken = True
		return taken
		
	def isEmpty (self) :
		""" checks if the board is empty
	
		If the number of moves is equal to zero, the board is empty,
		and return true. If not, return false.
		"""
		if (self._numMoves == 0) :
			return True
		else :
			return False
		
	def isFull (self) : 
		""" checks if the board is full
	
		If the number of moves is equal to nine, the board is full,
		and return true. If not, return false.
		"""
		if (self._numMoves == 9) :
			return True
		else :
			return False
			
	def checkPoint (self, x, y, symbol) : 
		""" checks if the symbol is at the coordinated passed in
	
		If symbol of the point passed in is equal to the symbol passed
		in, return true. Otherwise, return false.
		"""
		if self._gameBoard[y][x] == symbol :
			return True
		else :
			return False
			
	def checkWinHorizontal (self, symbol) :
		""" checks if there is a horizontal win
	
		If the symbol passed in is seen 3 in a row in any of the rows
		of the board, return true. Otherwise, return false.
		"""
		for y in range (0,3) :
			count = 0
			for x in range (0,3) :
				if self.checkPoint(x,y,symbol) : 
					count = count + 1
			if count == 3 :
				return True
		return False

	def checkWinVertical (self, symbol) :
		""" checks if there is a vertical win
	
		If the symbol passed in is seen 3 in a row in any of the columns
		of the board, return true. Otherwise, return false.
		"""
		for x in range (0,3) :
			count = 0
			for y in range (0,3) :
				if self.checkPoint(x,y,symbol) : 
					count = count + 1
			if count == 3 :
				return True
		return False	
	
	def checkWinDiagonal(self, symbol) : 
		""" checks if there is a diagonal win
	
		If the symbol passed in is seen 3 in a row in a left to right
		diagonal of the board, return true. Otherwise, return false.
		"""
		count1 = 0 #Left-Right
		count2 = 0 #Right-Left
		for value in range(0,3) :
			if self.checkPoint(value, value, symbol) :
				count1 += 1
			if self.checkPoint(value, (2 - value), symbol) :
				count2 += 1
		if count1 == 3 or count2 == 3 :
			return True
		else :
			return False
			
	def checkWin(self, symbol) :
		""" checks if there is a win on the board
	
		If the symbol passed in is seen 3 in a row either horizontally,
		vertically, or diagonally, return true. Otherwise, return false.
		"""
		if (self.checkWinDiagonal(symbol) or \
		self.checkWinHorizontal(symbol) or \
		self.checkWinVertical(symbol)):
			return True
		else :
			return False
			
	def checkForRange (self, move) :
		""" checks if a given move is able to be placed in board
	
		if the move is greater than three or less than one, its no good
		"""
		if (move.y > 0 and move.y < 4 and move.x > 0 and move.x < 4) :
			return True
		else :
			return False
		
	def checkTwoHorizontal (self, symbol) :
		""" checks if there is 2 of the same symbol on a row
	
		If the symbol passed in is seen twice in a row, and the third
		spot in that row is unused (is a *), return the coordinates
		of the unused point. Otherwise, return the point (-1,-1).
		"""
		for y in range (0,3) :
			count = 0
			for x in range (0,3) :
				if self.checkPoint(x,y,symbol) : 
					count = count + 1
				elif self.checkPoint(x,y, '*') :
					point = Point (x + 1,y + 1)
				else:
					count =	count - 1
			if count == 2:
				return point
		return Point (-1, -1)	
		
	def checkTwoVertical (self, symbol) :
		""" checks if there is 2 of the same symbol on a column
	
		If the symbol passed in is seen twice in a column, and the third
		spot in that column is unused (is a *), return the coordinates
		of the unused point. Otherwise, return the point (-1,-1).
		"""
		for x in range (0,3) :
			count = 0
			for y in range (0,3) :
				if self.checkPoint(x,y,symbol) : 
					count = count + 1
				elif self.checkPoint(x,y, '*') :
					point = Point (x + 1,y + 1)
				else :	
					count = count - 1	
			if count == 2 :
				return point
		return Point (-1, -1)			
		
		
	def checkTwoLRDiagonal(self, symbol) : 
		""" checks if there is 2 of the same symbol on LRDiagonal
	
		If the symbol passed in is seen twice in a LRDiagonal, and the
		third spot in that diagonal is unused (is a *), return the 
		coordinates	of the unused point. Otherwise, return the 
		point (-1,-1).
		"""
		count = 0 
		for value in range(0,3) :
			if self.checkPoint(value, value, symbol) :
				count += 1
			elif self.checkPoint(value,value, '*') :
				point = Point (value + 1,value + 1)	
			else :	
				count = count - 1			
		if count == 2 :
			return point
		else :	
			return Point (-1, -1)	
		
	def checkTwoRLDiagonal(self, symbol) :
		""" checks if there is 2 of the same symbol on RLDiagonal
	
		If the symbol passed in is seen twice in a RLDiagonal, and the
		third spot in that diagonal is unused (is a *), return the 
		coordinates	of the unused point. Otherwise, return the 
		point (-1,-1).
		""" 
		count = 0 

		for value in range(0,3) :
			if self.checkPoint(value, (2 - value), symbol) :
				count += 1
			elif self.checkPoint(value,(2 - value), '*') :
				point = Point (value + 1, (2 - value + 1))
			else :	
				count = count - 1			
		if count == 2 :
			return point
		else :	
			return Point (-1, -1)			
			
	def checkTwoInRow (self, symbol) :
		""" checks if there is 2 of the same symbol in a row
	
		If the symbol passed in is seen twice in a RLDiagonal, 
		LRDiagonal, horizontal, or vertical, return the 
		coordinates	of the unused point. Otherwise, return the 
		point (-1,-1).
		""" 
		badPoint = Point (-1, -1)
		point = badPoint
		if point.x == badPoint.x and point.y == badPoint.y   :
			point = self.checkTwoHorizontal (symbol)
		if point.x == badPoint.x and point.y == badPoint.y   :
			point = self.checkTwoVertical (symbol)
		if point.x == badPoint.x and point.y == badPoint.y  :
			point = self.checkTwoLRDiagonal (symbol)
		if point.x == badPoint.x and point.y == badPoint.y  :	
			point = self.checkTwoRLDiagonal (symbol)
		return point		
