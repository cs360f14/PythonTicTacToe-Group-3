#!/usr/bin/python3
##########################################
# File Name:unittestBoard.py
# Author:Group 3
# Date:10/24/14
# Class:360
# Assignment:Tic-Tac-Toe
# Purpose:Testing the Board class
########################################

"""
Unit tests for the Board class
"""
import unittest
import board
from board import *

class TestBoardFunctions(unittest.TestCase):
	
	def setUp(self) :
		"""
		creates the board
		"""
		self.board = Board()
	
	def tearDown(self):
		"""
		Nothing to tear down
		"""
		pass
		
	def test_printBoard(self) :
		"""
		Tests to see print
		"""
		self.board.printBoard()
	
	def test_insertMoveGood(self) :
		"""
		Tests to see if you can insert move
		"""
		board2 = Board()
		board2._gameBoard[0][0] = 'X'
		self.board.insertMove(Point(1,1), 'X')
		self.assertEqual(self.board._gameBoard[0][0], \
		 board2._gameBoard[0][0])
		
		
	def test_insertMoveBad(self) :
		"""
		Tests to see if a move can't be inserted
		"""
		self.board.insertMove(Point(4,4), 'X')
		
	def test_reset(self) :
		"""
		tests to reset board
		"""
		self.board.reset()
	
	def test_spotTakenYes(self) :
		"""
		Tests to see if a spot is taken
		"""
		self.board._gameBoard[0][0] = 'X'
		self.assertTrue(self.board.spotTaken(Point(1,1)))
	
	def test_spotTakenNo(self) :
		"""
		Tests to see if a spot isn't taken
		"""
		self.assertFalse(self.board.spotTaken(Point(1,1)))
	
		
	def test_isEmptyYes(self) :
		"""
		Tests an empty board
		"""
		self.assertTrue(self.board.isEmpty())
		
	def test_isEmptyNo(self) :
		"""
		Tests a board with stuff
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.assertFalse(self.board.isEmpty())
		
	def test_isFullNo(self) :
		"""
		tests and empty for full
		"""
		self.assertFalse(self.board.isFull())
		
	def test_isFullYes(self) :
		"""
		Fills board, then tests for full
		"""
		for x in range(0,3) :
			for y in range (0,3) :
				self.board._gameBoard[x][y] = 'X'
		self.assertFalse(self.board.isFull())
		
	def test_checkPointYes(self) :
		"""
		checks to see a point is there
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.assertTrue(self.board.checkPoint(0,0,'X'))
	
	def test_checkPointNo(self) :
		"""
		Checks to see if a point isn't there
		"""
		self.assertFalse(self.board.checkPoint(0,0,'X'))
		
	def test_checkWinHorizontal1(self) :
		"""
		Tests a horizontal case
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,1), 'X')
		self.board.insertMove(Point(3,1), 'X')
		self.assertTrue(self.board.checkWinHorizontal('X'))
		
	def test_checkWinHorizontal2(self) :
		"""
		Tests a horizontal case
		"""
		self.board.insertMove(Point(1,2), 'X')
		self.board.insertMove(Point(2,2), 'X')
		self.board.insertMove(Point(3,2), 'X')
		self.assertTrue(self.board.checkWinHorizontal('X'))
		
	def test_checkWinHorizontal3(self) :
		"""
		Tests a horizontal case
		"""
		self.board.insertMove(Point(1,3), 'X')
		self.board.insertMove(Point(2,3), 'X')
		self.board.insertMove(Point(3,3), 'X')
		self.assertTrue(self.board.checkWinHorizontal('X'))
		
	def test_checkWinHorizontalFail(self) :
		"""
		Tests a non horizontal case
		"""
		self.assertFalse(self.board.checkWinHorizontal('X'))
		
		
	def test_checkWinVertical1(self) :
		"""
		Tests a Vertical case
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(1,2), 'X')
		self.board.insertMove(Point(1,3), 'X')
		self.assertTrue(self.board.checkWinVertical('X'))
		
	def test_checkWinVertical2(self) :
		"""
		Tests a Vertical case
		"""
		self.board.insertMove(Point(2,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		self.board.insertMove(Point(2,3), 'X')
		self.assertTrue(self.board.checkWinVertical('X'))
		
	def test_checkWinVertical3(self) :
		"""
		Tests a Vertical case
		"""
		self.board.insertMove(Point(3,1), 'X')
		self.board.insertMove(Point(3,2), 'X')
		self.board.insertMove(Point(3,3), 'X')
		self.assertTrue(self.board.checkWinVertical('X'))
		
	def test_checkWinVerticalFail(self) :
		"""
		Tests a non Vertical case
		"""
		self.assertFalse(self.board.checkWinVertical('X'))
		
		
	def test_checkWinDiagonal1(self) :
		"""
		Tests a Diagonal win case
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		self.board.insertMove(Point(3,3), 'X')
		self.assertTrue(self.board.checkWinDiagonal('X'))
		
		
	def test_checkWinDiagonal2(self) :
		"""
		Tests a Diagonal win case
		"""
		self.board.insertMove(Point(3,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		self.board.insertMove(Point(1,3), 'X')
		self.assertTrue(self.board.checkWinDiagonal('X'))
		
	def test_checkWinDiagonalFail(self) :
		"""
		Tests a non Diagonal win case
		"""
		self.assertFalse(self.board.checkWinDiagonal('X'))
		
	def test_checkWin1(self) :
		"""
		Tests a horizontal case
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,1), 'X')
		self.board.insertMove(Point(3,1), 'X')
		self.assertTrue(self.board.checkWin('X'))
		
	def test_checkWin2(self) :
		"""
		Tests a horizontal case
		"""
		self.board.insertMove(Point(1,2), 'X')
		self.board.insertMove(Point(2,2), 'X')
		self.board.insertMove(Point(3,2), 'X')
		self.assertTrue(self.board.checkWin('X'))
		
	def test_checkWin3(self) :
		"""
		Tests a horizontal case
		"""
		self.board.insertMove(Point(1,3), 'X')
		self.board.insertMove(Point(2,3), 'X')
		self.board.insertMove(Point(3,3), 'X')
		self.assertTrue(self.board.checkWin('X'))
		
	def test_checkWin4(self) :
		"""
		Tests a Vertical case
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(1,2), 'X')
		self.board.insertMove(Point(1,3), 'X')
		self.assertTrue(self.board.checkWin('X'))
		
	def test_checkWin5(self) :
		"""
		Tests a Vertical case
		"""
		self.board.insertMove(Point(2,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		self.board.insertMove(Point(2,3), 'X')
		self.assertTrue(self.board.checkWin('X'))
		
	def test_check6(self) :
		"""
		Tests a Vertical case
		"""
		self.board.insertMove(Point(3,1), 'X')
		self.board.insertMove(Point(3,2), 'X')
		self.board.insertMove(Point(3,3), 'X')
		self.assertTrue(self.board.checkWin('X'))
		
	def test_checkWin7(self) :
		"""
		Tests a Diagonal win case
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		self.board.insertMove(Point(3,3), 'X')
		self.assertTrue(self.board.checkWin('X'))
		
		
	def test_checkWin8(self) :
		"""
		Tests a Diagonal win case
		"""
		self.board.insertMove(Point(3,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		self.board.insertMove(Point(1,3), 'X')
		self.assertTrue(self.board.checkWin('X'))
		
	def test_checkWinFail(self) :
		"""
		Tests a non win case
		"""
		self.assertFalse(self.board.checkWin('X'))
		
	def test_checkForRangeIn(self) :
		"""
		tests a inrange case
		"""
		self.assertTrue(self.board.checkForRange(Point(1,1)))
		
	def test_checkForRangeOut(self) :
		"""
		Tests a out of range case
		"""
		self.assertFalse(self.board.checkForRange(Point(60,-50)))

	def test_checkTwoHorizontalYes (self) :
		"""
		Tests to see if there are two pieces in a line
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,1), 'X')
		Point1 = (self.board.checkTwoHorizontal('X'))
		Point2  = Point(3,1)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
		
	def test_checkTwoHorizontalNo (self) :
		"""
		Checks to make sure it returns neg values. 
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		Point1 = (self.board.checkTwoHorizontal('X'))
		Point2  = Point(-1,-1)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
		
	def test_checkTwoVerticalYes (self) :
		"""
		Tests to see if there are two pieces in a line
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(1,2), 'X')
		Point1 = (self.board.checkTwoVertical('X'))
		Point2  = Point(1,3)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
		
	def test_checkTwoVerticalNo (self) :
		"""
		Tests to see if it gets back a neg
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		Point1 = (self.board.checkTwoVertical('X'))
		Point2  = Point(-1,-1)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
		
	def test_checkTwoLRDiagonalYes(self) :
		"""
		Tests to see if There is two piecs in a vertical row
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		Point1 = (self.board.checkTwoLRDiagonal('X'))
		Point2 = Point(3,3)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
		
	def test_checkTwoLRDiagonalNo(self) :
		"""
		Tests to make sure it is returning a negative
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(3,2), 'X')
		Point1 = (self.board.checkTwoLRDiagonal('X'))
		Point2 = Point(-1,-1)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
		
	def test_checkTwoLRDiagonalYes(self) :
		"""
		Tests to see if There is two piecs in a vertical row
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,2), 'X')
		Point1 = (self.board.checkTwoLRDiagonal('X'))
		Point2 = Point(3,3)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
		
	def test_checkTwoRLDiagonalYes(self) :
		"""
		Tests the other diagonal option
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(3,3), 'X')
		Point1 = (self.board.checkTwoLRDiagonal('X'))
		Point2 = Point(2,2)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)

	def test_checkTwoRLDiagonalNo(self) :
		"""
		Makes sure to reurn a negative
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(2,3), 'X')
		Point1 = (self.board.checkTwoLRDiagonal('X'))
		Point2 = Point(-1,-1)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)

	def test_checkTwoInRow (self) :
		"""
		Makes sure it returns point correctly
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(1,2), 'X')
		Point1 = self.board.checkTwoInRow('X')
		Point2 = Point(1,3)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
		
	def test_checkTwoInRowFail (self) :
		"""
		Makes sure it returns negative
		"""
		self.board.insertMove(Point(1,1), 'X')
		self.board.insertMove(Point(3,2), 'X')
		Point1 = self.board.checkTwoInRow('X')
		Point2 = Point(-1,-1)
		self.assertEqual(Point1.x, Point2.x)
		self.assertEqual(Point1.y, Point2.y)
