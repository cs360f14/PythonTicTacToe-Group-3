#!/usr/bin/python3
##########################################
# File Name:	unittestUser.py
# Author:		Group 3
# Date:			10/28/14
# Class:		360
# Assignment:	Tic-Tac-Toe
# Purpose:		Testing the User class
########################################
"""
Unit tests for the user class
"""
import unittest
from user import *

class TestUserFunctions (unittest.TestCase) :
	
	def setUp (self) :
		""" setup for the tests to run"""
		self.user = user("Bob", "X", 1, 1, 1)
		self.board = Board()
		self.point = Point(1,2)
		
	def tearDown(self) :	
		"""nothing to tear down"""
		pass
		
	def test_getWins (self) :
		"""checks that getWins returns the correct number of wins"""
		self.assertEqual (self.user.getWins(), 1)
		
	def test_getLosses (self) :
		"""checks that getLosses returns the correct number of losses"""
		self.assertEqual (self.user.getLosses(), 1)
		
	def test_getDraws (self) :
		"""checks that getWDraws returns the correct number of draws"""
		self.assertEqual (self.user.getDraws(), 1)
		
	def test_verifyInput_good (self) :
		"""test a point that is not taken on the board"""
		self.assertTrue(self.user.verifyInput(self.point, self.board))
	
	def test_verifyInput_bad (self) :
		"""test a point that is taken on the board"""
		self.board.insertMove(self.point, "X")
		self.assertFalse(self.user.verifyInput(self.point, self.board))	
		
	def test_incrementWins (self) :
		"""checks that incrementWins increases the number of wins by 1"""
		self.user.incrementWins()
		self.assertEqual (self.user.getWins(), 2)
		
	def test_incrementLosses (self) :
		"""checks that incrementLosses increases the number of losses by 1"""
		self.user.incrementLosses()
		self.assertEqual (self.user.getLosses(), 2)
		
	def test_incrementDraws (self) :
		"""checks that incrementDraws increases the number of draws by 1"""
		self.user.incrementDraws()
		self.assertEqual (self.user.getDraws(), 2)

