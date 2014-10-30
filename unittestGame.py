#!/usr/bin/python3
##########################################
# File Name:unittestGame.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:Testing the game class
########################################
"""
Unit tests for the game class
"""
import unittest
from game import *


class TestGameFunctions (unittest.TestCase):

	
	def setUp (self) :
		""" setup for the tests to run"""
		self.game = game ()
		self.game._user = user ("Bob", 'X', 0, 0, 0)
		self.game._ai = EAI ("Gary", 'O')
		self.point1 = Point (1,1)
		self.point2 = Point (1,2)
		self.point3 = Point (1,3)
		self.point4 = Point (2,1)
		self.point5 = Point (2,2)
		self.point6 = Point (2,3)
		self.point7 = Point (3,1)
		self.point8 = Point (3,2)
		self.point9 = Point (3,3)
		
	def tearDown(self) :	
		"""nothing to tear down"""
		pass
	
	def test_userSymbolIsX (self) :
		"""tests the function userSymbolIsX """
		self.assertTrue(self.game.userSymbolIsX ())
		
	def test_getTurn (self) :
		"""tests that it is the user's turn"""
		self.assertTrue(self.game.getTurn ())
	
	
	def test_turn (self) :
		"""testing that inserting only one point and it is the user"""
		self.game.turn (self.point1)
		self.assertTrue(self.game._board.checkPoint \
			(self.point1.x - 1, self.point1.y - 1, 'X'))
		self.assertTrue(self.game.gameRunning ())
		self.assertEqual(self.game._user.getWins (), 0)
		self.assertEqual(self.game._user.getLosses (), 0)
		self.assertEqual(self.game._user.getDraws (), 0)
		
		
	
	def test_turn_Win (self) :
		"""testing that the user wins and increases the correct score
		and that the game ends
		"""
		self.game.turn (self.point1) #User
		self.game.turn (self.point4) #AI
		self.game.turn (self.point2) #User
		self.game.turn (self.point5) #AI
		self.game.turn (self.point3) #User
		self.assertTrue(self.game._board.checkPoint \
			(self.point1.x - 1, self.point1.y - 1, 'X')) #User
		self.assertTrue(self.game._board.checkPoint \
			(self.point4.x - 1, self.point4.y - 1, 'O')) #AI
		self.assertTrue(self.game._board.checkPoint \
			(self.point2.x - 1, self.point2.y - 1, 'X')) #User
		self.assertTrue(self.game._board.checkPoint \
			(self.point5.x - 1, self.point5.y - 1, 'O')) #AI	
		self.assertTrue(self.game._board.checkPoint \
			(self.point3.x - 1, self.point3.y - 1, 'X')) #User
		self.assertFalse(self.game.gameRunning ())
		self.assertEqual(self.game._user.getWins (), 1)
		self.assertEqual(self.game._user.getLosses (), 0)
		self.assertEqual(self.game._user.getDraws (), 0)
		
	def test_turn_Lose (self) :
		"""testing that the user loses and increases the correct score
		and that the game ends
		"""
		self.game.turn (self.point4) #User
		self.game.turn (self.point1) #AI
		self.game.turn (self.point5) #User
		self.game.turn (self.point2) #AI
		self.game.turn (self.point8) #User
		self.game.turn (self.point3) #AI
		self.assertTrue(self.game._board.checkPoint \
			(self.point4.x - 1, self.point4.y - 1, 'X')) #User
		self.assertTrue(self.game._board.checkPoint \
			(self.point1.x - 1, self.point1.y - 1, 'O')) #AI
		self.assertTrue(self.game._board.checkPoint \
			(self.point5.x - 1, self.point5.y - 1, 'X')) #User
		self.assertTrue(self.game._board.checkPoint \
			(self.point2.x - 1, self.point2.y - 1, 'O')) #AI	
		self.assertTrue(self.game._board.checkPoint \
			(self.point8.x - 1, self.point8.y - 1, 'X')) #User
		self.assertTrue(self.game._board.checkPoint \
			(self.point3.x - 1, self.point3.y - 1, 'O')) #AI			
		self.assertFalse(self.game.gameRunning ())
		self.assertEqual(self.game._user.getWins (), 0)
		self.assertEqual(self.game._user.getLosses (), 1)
		self.assertEqual(self.game._user.getDraws (), 0)


	def test_updateTurn (self) :
		"""tests that update turn works"""
		self.assertTrue(self.game._userTurn)
		self.game.updateTurn ()
		self.assertFalse(self.game._userTurn)
		self.game.updateTurn ()
		self.assertTrue(self.game._userTurn)
		
	def test_resetGame (self) :
		self.assertTrue(self.game._userFirst)
		self.game._gameRunning = False
		self.game.resetGame ()
		self.assertTrue(self.game._gameRunning)
		self.assertFalse(self.game._userFirst)
