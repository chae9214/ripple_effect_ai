from ripple_effect_csp import *
from propagators import *
import time

#######################################################################
# Utility functions for printing                                      #
#######################################################################

def print_solution(var_array, puzzle):
	print (' ' + '--' * len(puzzle[0]) + '-')
	for ri in range(len(puzzle)):
		s = '[ '
		for i in range(len(puzzle[ri])):
			if ri % 2 == 0 and i % 2 == 0:
				s = s + str(var_array[int(ri/2)][int(i/2)].get_assigned_value()) + ' '
			else:
				if puzzle[ri][i] == '-': s = s[:-1] + '---' 
				else: s = s + puzzle[ri][i] + ' '
		s = s + ']'
		print(s)
	print (' ' + '--' * len(puzzle[0]) + '-')

def print_puzzle(puzzle):
	print (' ' + '--' * len(puzzle[0]) + '-')
	for ri in range(len(puzzle)):
		s = '[ '
		for item in puzzle[ri]:
			if ri % 2 == 0: s = s + str(item) + ' '
			else:
				if str(item) == '-': s = s[:-1] + '---' 
				else: s = s + str(item) + ' '
		s = s + ']'
		print(s)
	print (' ' + '--' * len(puzzle[0]) + '-')

def get_values(var_array):
	vlist = []
	for row in var_array:
		vlist.append([v.get_assigned_value() for v in row])
	return vlist

def print_correct(var_array, answer):
	if answer == get_values(var_array):
		print("Solution Correct!")
	else:
		print("Solution Incorrect!")

#######################################################################
# Different puzzle assignments                                        #
#######################################################################

'''
# 10 x 10 puzzle (empty board)
puzzleN = [[ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
		   [ 0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ' , 0 , ' ',  0 , ' ',  0 , ' ',  0 ]]
'''

# 8 x 8 puzzle (Sample 1 - small board)
puzzle1 = [[ 0 , ' ',  3 , '|',  0 , ' ',  0 , '|' , 0 , '|',  1 , ' ',  0 , '|',  0 ],
		   [' ', ' ', ' ', '|', '-', ' ', '-', ' ', ' ', ' ', '-', ' ', '-', '|', ' '],
		   [ 2 , ' ',  0 , '|',  0 , '|',  3 , ' ',  0 , ' ',  6 , ' ',  0 , '|',  1 ],
		   ['-', ' ', '-', '-', '-', ' ', '-', ' ', '-', ' ', '-', ' ', ' ', '|', ' '],
		   [ 0 , '|',  0 , ' ',  0 , ' ',  0 , ' ',  0 , ' ',  4 , '|',  0 , '|',  0 ],
		   ['-', '|', ' ', ' ', '-', ' ', '-', ' ', '-', ' ', '-', '|', '-', '|', ' '],
		   [ 3 , '|',  0 , '|',  2 , '|',  0 , '|',  0 , ' ',  0 , '|',  6 , '|',  3 ],
		   [' ', '|', '-', ' ', ' ', '|', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', '-'],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  3 , '|',  5 , ' ',  2 , ' ',  0 ],
		   [' ', '|', ' ', ' ', '-', '|', ' ', ' ', ' ', '|', '-', ' ', ' ', ' ', ' '],
		   [ 0 , '|',  3 , '|',  0 , '|',  5 , ' ',  0 , '|',  1 , '|',  0 , ' ',  0 ],
		   [' ', '|', '-', '|', ' ', '|', '-', ' ', '-', ' ', ' ', ' ', '-', ' ', '-'],
		   [ 0 , '|',  0 , '|',  0 , '|',  3 , ' ',  5 , ' ',  0 , ' ',  0 , '|',  0 ],
		   ['-', '|', ' ', '|', '-', ' ', '-', ' ', '-', ' ', '-', ' ', '-', '|', ' '],
		   [ 0 , '|',  0 , '|',  3 , ' ',  0 , ' ',  0 , ' ',  0 , '|',  0 , '|',  0 ]]

rooms1 = [[(0, 0), (0, 1), (1, 0), (1, 1), ], 
		  [(0, 2), (0, 3), ],
		  [(1, 2), ],
		  [(0, 4), (1, 3), (1, 4), (1, 5), (1, 6), (2, 6), ],
		  [(0, 5), (0, 6), ],
		  [(0, 7), (1, 7), (2, 7), (3, 7), ],
		  [(2, 0), ],
		  [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), ],
		  [(3, 0), (4, 0), (5, 0), (6, 0), ],
		  [(3, 2), (4, 1), (4, 2), (5, 1), ],
		  [(3, 3), ],
		  [(3, 4), (3, 5), (4, 3), (4, 4), (5, 3), (5, 4), ],
		  [(3, 6), (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), ],
		  [(5, 2), (6, 2), ],
		  [(6, 1), (7, 1), ],
		  [(7, 0), ],
		  [(5, 5), (6, 3), (6, 4), (6, 5), (6, 6), ],
		  [(7, 2), (7, 3), (7, 4), (7, 5), ],
		  [(7, 6), ],
		  [(6, 7), (7, 7), ]]

answer1 = [[1, 3, 2, 1, 5, 1, 2, 4],
		   [2, 4, 1, 3, 2, 6, 4, 1],
		   [1, 2, 3, 6, 1, 4, 1, 2],
		   [3, 5, 2, 1, 4, 1, 6, 3],
		   [2, 1, 4, 2, 3, 5, 2, 1],
		   [1, 3, 1, 5, 6, 1, 3, 4],
		   [4, 1, 2, 3, 5, 2, 4, 1],
		   [1, 2, 3, 1, 2, 4, 1, 2]]

# 10 x 10 puzzle (Sample 4 - medium board, smaller rooms)
puzzle2 = [[ 0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , '|' , 0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 ],
		   [' ', '|', '-', ' ', ' ', '|', '-', '|', ' ', '|', '-', '-', '-', '-', '-', '-', '-', '|', '-'],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 ],
		   [' ', '|', '-', '-', '-', ' ', ' ', '|', ' ', '|', '-', '-', '-', ' ', ' ', '|', '-', ' ', ' '],
		   [ 0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 ],
		   ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-'],
		   [ 0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 ],
		   [' ', ' ', '-', '|', '-', '|', '-', '-', '-', '-', '-', '|', '-', ' ', ' ', '|', '-', '|', ' '],
		   [ 0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 ],
		   ['-', '|', '-', ' ', ' ', '|', '-', '-', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', '|', ' '],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 ],
		   ['-', '|', '-', '-', '-', '|', '-', '-', '-', '-', '-', '|', '-', '-', '-', '-', '-', '|', '-'],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 ],
		   [' ', '|', ' ', ' ', '-', '|', ' ', ' ', '-', '|', '-', '|', '-', '-', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  0 ],
		   [' ', '|', '-', '-', '-', '|', '-', '|', '-', ' ', ' ', '|', '-', '-', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 ],
		   ['-', '|', ' ', ' ', '-', '|', '-', '-', '-', '-', '-', '|', '-', '-', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  0 ]]

rooms2 = [[(0, 0), (1, 0), (2, 0)],
		  [(0, 1)],
		  [(0, 2), (1, 1), (1, 2)],
		  [(0, 3)],
		  [(0, 4), (1, 4), (2, 4)],
		  [(0, 5)],
		  [(0, 6), (0, 7), (0, 8)],
		  [(0, 9)],
		  [(1, 3), (2, 2), (2, 3)],
		  [(1, 5), (1, 6)],
		  [(1, 7), (2, 6), (2, 7)],
		  [(1, 8)],
		  [(1, 9), (2, 8), (2, 9)],
		  [(2, 1)],
		  [(2, 5)],
		  [(3, 0), (3, 1), (4, 0)],
		  [(3, 2)],
		  [(3, 3), (3, 4), (3, 5)],
		  [(3, 6)],
		  [(3, 7), (4, 6), (4, 7)],
		  [(3, 8)],
		  [(3, 9), (4, 9), (5, 9)],
		  [(4, 1)],
		  [(4, 2), (5, 1), (5, 2)],
		  [(4, 3), (4, 4)],
		  [(4, 5)],
		  [(4, 8), (5, 7), (5, 8)],
		  [(5, 0)],
		  [(5, 3), (5, 4), (5, 5)],
		  [(5, 6)],
		  [(6, 0), (7, 0), (8, 0)],
		  [(6, 1), (6, 2), (7, 1)],
		  [(6, 3), (6, 4), (7, 3)],
		  [(6, 5)],
		  [(6, 6), (6, 7), (6, 8)],
		  [(6, 9)],
		  [(7, 2)],
		  [(7, 4)],
		  [(7, 5), (8, 4), (8, 5)],
		  [(7, 6)], 
		  [(7, 7), (7, 8), (7, 9)],
		  [(8, 1), (8, 2), (9, 1)],
		  [(8, 3)],
		  [(8, 6), (8, 7), (8, 8)],
		  [(8, 9)],
		  [(9, 0)],
		  [(9, 2)],
		  [(9, 3), (9, 4), (9, 5)],
		  [(9, 6)],
		  [(9, 7), (9, 8), (9, 9)]]

answer2 = [[2, 1, 3, 1, 2, 1, 3, 1, 2, 1],
		   [1, 2, 1, 3, 1, 2, 1, 3, 1, 2], 
		   [3, 1, 2, 1, 3, 1, 2, 1, 3, 1], 
		   [1, 3, 1, 2, 1, 3, 1, 2, 1, 3],
		   [2, 1, 3, 1, 2, 1, 3, 1, 2, 1],
		   [1, 2, 1, 3, 1, 2, 1, 3, 1, 2],
		   [3, 1, 2, 1, 3, 1, 2, 1, 3, 1],
		   [1, 3, 1, 2, 1, 3, 1, 2, 1, 3],
		   [2, 1, 3, 1, 2, 1, 3, 1, 2, 1],
		   [1, 2, 1, 3, 1, 2, 1, 3, 1, 2]]

# 10 x 10 puzzle (Sample 5 - medium board, bigger rooms)
puzzle3 = [[ 0 , ' ',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ' , 0 , '|',  2 , ' ',  0 , ' ',  0 , ' ',  0 ],
		   ['-', '-', '-', '-', '-', '|', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 ],
		   [' ', ' ', '-', '-', '-', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', '-', ' ', ' '],
		   [ 0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 ],
		   ['-', '-', '-', ' ', '-', '|', '-', '-', '-', '|', '-', '-', '-', '-', '-', '|', '-', '|', ' '],
		   [ 0 , '|',  0 , ' ',  0 , '|',  2 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  3 , '|',  0 , '|',  0 ],
		   [' ', '|', '-', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', '-', ' ', ' ', '|', ' ', '|', '-'],
		   [ 0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 ],
		   [' ', '|', ' ', ' ', '-', '|', '-', '-', '-', '|', '-', ' ', ' ', ' ', '-', '|', '-', '|', ' '],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 , '|',  0 ],
		   ['-', '|', ' ', ' ', ' ', '|', ' ', ' ', '-', '|', ' ', ' ', ' ', ' ', '-', ' ', ' ', '|', '-'],
		   [ 0 , '|',  0 , ' ',  1 , '|',  0 , '|',  0 , '|',  0 , ' ',  5 , '|',  0 , ' ',  0 , '|',  0 ],
		   ['-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' '],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 ],
		   [' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , ' ',  0 , ' ',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  0 ],
		   [' ', '|', ' ', ' ', '-', '-', '-', '-', '-', '|', '-', '-', '-', '|', ' ', ' ', ' ', ' ', '-'],
		   [ 0 , '|',  0 , '|',  0 , ' ',  2 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 ]]

rooms3 = [[(0, 0), (0, 1), (0, 2), ],
		  [(0, 3), (0, 4), (0, 5), ],
		  [(0, 6), (0, 7), (0, 8), (0, 9)],
		  [(1, 0), (2, 0), (2, 1)],
		  [(1, 1), (1, 2)],
		  [(1, 3), (1, 4), (2, 3), (2, 4)],
		  [(1, 5), (1, 6), (2, 5), (2, 6)],
		  [(1, 7), (2, 7)],
		  [(1, 8), (1, 9), (2, 9), (3, 9)],
		  [(2, 2)],
		  [(2, 8)],
		  [(3, 0), (4, 0), (5, 0)],
		  [(3, 1), (3, 2), (4, 2)],
		  [(3, 3), (3, 4), (4, 3), (4, 4)],
		  [(3, 5), (3, 6), (3, 7), (4, 5), (4, 7)],
		  [(3, 8), (4, 8)],
		  [(4, 1), (5, 1), (5, 2), (6, 1), (6, 2)],
		  [(4, 6), (5, 5), (5, 6), (5, 7), (6, 5), (6, 6)],
		  [(4, 9), (5, 9)],
		  [(5, 3), (5, 4), (6, 3)],
		  [(5, 8), (6, 7), (6, 8)],
		  [(6, 0)],
		  [(6, 4)],
		  [(6, 9), (7, 8), (7, 9)],
		  [(7, 0), (8, 0), (9, 0)],
		  [(7, 1), (7, 2), (8, 1), (8, 2), (9, 1)],
		  [(7, 3), (7, 4), (8, 3), (8, 4)],
		  [(7, 5), (7, 6), (8, 5), (8, 6)],
		  [(7, 7)],
		  [(8, 7), (8, 8), (8, 9), (9, 7), (9, 8)],
		  [(9, 2), (9, 3), (9, 4)],
		  [(9, 5), (9, 6)],
		  [(9, 9)]]

answer3 = [[2, 3, 1, 2, 1, 3, 2, 4, 1, 3],
		   [3, 1, 2, 1, 3, 2, 4, 1, 3, 2],
		   [1, 2, 1, 4, 2, 1, 3, 2, 1, 4],
		   [2, 1, 3, 2, 1, 4, 1, 3, 2, 1],
		   [1, 5, 2, 3, 4, 2, 6, 5, 1, 2],
		   [3, 2, 4, 1, 3, 1, 2, 4, 3, 1],
		   [1, 3, 1, 2, 1, 3, 5, 2, 1, 3],
		   [2, 1, 3, 4, 2, 1, 3, 1, 2, 1],
		   [1, 2, 5, 3, 1, 2, 4, 3, 5, 2],
		   [3, 4, 1, 2, 3, 1, 2, 1, 4, 1]]

# 10 x 10 puzzle (Sample 9 - medium board, hard difficulty)
puzzle4 = [[ 0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ' , 0 , '|',  5 , ' ',  0 , ' ',  0 , '|',  0 ],
		   ['-', '|', ' ', '|', ' ', ' ', '-', '|', ' ', ' ', '-', '|', ' ', ' ', ' ', ' ', '-', ' ', ' '],
		   [ 0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 ],
		   [' ', '|', '-', '|', ' ', ' ', '-', '|', ' ', '|', '-', '|', ' ', ' ', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , '|',  5 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 ],
		   [' ', '|', ' ', ' ', '-', '-', '-', '-', '-', '-', ' ', '|', '-', '|', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  0 ],
		   ['-', '|', '-', '-', '-', '|', '-', '-', '-', '-', '-', '|', ' ', '|', '-', '-', '-', ' ', ' '],
		   [ 0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 ],
		   [' ', ' ', '-', ' ', ' ', '|', ' ', '|', ' ', ' ', '-', ' ', ' ', '|', ' ', ' ', ' ', '|', '-'],
		   [ 0 , ' ',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 ],
		   ['-', '-', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', ' ', ' ', '-', '|', '-'],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 ],
		   [' ', '|', ' ', ' ', ' ', '|', ' ', ' ', '-', '|', '-', '-', '-', '-', '-', '-', '-', '|', ' '],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  3 , ' ',  0 , '|',  0 ],
		   ['-', '|', '-', '-', '-', '|', ' ', ' ', '-', '|', '-', '-', '-', '-', '-', '-', ' ', '|', ' '],
		   [ 0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 , '|',  0 ],
		   ['-', ' ', ' ', '|', ' ', '|', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', '|', '-', '-', '-'],
		   [ 0 , ' ',  0 , '|',  0 , '|',  1 , ' ',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 ]]

rooms4 = [[(0, 0)],
		  [(0, 1), (1, 1)],
		  [(0, 2), (0, 3), (1, 2), (2, 2), (2, 3)],
		  [(0, 4), (0, 5), (1, 4), (2, 4)],
		  [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (2, 6)],
		  [(0, 9), (1, 8), (1, 9)],
		  [(1, 0), (2, 0), (3, 0)],
		  [(1, 3)],
		  [(1, 5)],
		  [(2, 1), (3, 1), (3, 2)],
		  [(2, 5), (3, 3), (3, 4), (3, 5)],
		  [(2, 7), (2, 8)],
		  [(2, 9)],
		  [(3, 6), (4, 6), (5, 5), (5, 6)],
		  [(3, 7), (3, 8), (3, 9), (4, 9)],
		  [(4, 0), (4, 2), (5, 0), (5, 1), (5, 2)],
		  [(4, 1)],
		  [(4, 3), (5, 3)],
		  [(4, 4), (4, 5), (5, 4)],
		  [(4, 7), (4, 8), (5, 7), (5, 8), (6, 6), (6, 7)],
		  [(5, 9)],
		  [(6, 0), (7, 0)],
		  [(6, 1), (6, 2), (7, 1), (7, 2)],
		  [(6, 3), (6, 4), (7, 3), (8, 3), (8, 4)],
		  [(6, 5)],
		  [(6, 8)],
		  [(6, 9), (7, 9), (8, 9)],
		  [(7, 4)],
		  [(7, 5), (7, 6), (7, 7), (7, 8), (8, 8)],
		  [(8, 0)],
		  [(8, 1), (9, 0), (9, 1)],
		  [(8, 2), (9, 2)],
		  [(8, 5), (8, 6), (8, 7), (9, 6), (9, 7)],
		  [(9, 3), (9, 4), (9, 5)],
		  [(9, 8), (9, 9)]]

answer4 = [[1, 2, 1, 3, 1, 2, 5, 1, 3, 2],
		   [2, 1, 4, 1, 3, 1, 2, 4, 1, 3],
		   [1, 3, 5, 2, 4, 3, 6, 1, 2, 1],
		   [3, 2, 1, 4, 1, 2, 1, 3, 1, 2],
		   [2, 1, 3, 1, 2, 1, 3, 2, 5, 4],
		   [4, 5, 1, 2, 3, 4, 2, 1, 3, 1],
		   [1, 3, 2, 1, 5, 1, 4, 6, 1, 2],
		   [2, 1, 4, 3, 1, 5, 1, 3, 2, 1],
		   [1, 2, 1, 4, 2, 3, 5, 2, 4, 3],
		   [3, 1, 2, 1, 3, 2, 1, 4, 1, 2]]

# 18 x 10 puzzle (Sample 10 - large board, hard difficulty)
puzzle5 = [[ 1 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  1 , '|' , 0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|' , 0 , '|',  3 , ' ',  0 , ' ',  0 ],
		   [' ', ' ', ' ', '|', ' ', ' ', '-', '-', '-', ' ', ' ', '|', ' ', ' ', '-', '-', '-', '|', '-', '-', '-', '-', '-', '-', '-', '-', '-', '|', '-', '|', ' ', ' ', ' ', ' ', '-'],
		   [ 0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , '|' , 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|' , 0 , '|',  0 , ' ',  0 , '|',  0 ],
		   ['-', ' ', ' ', '|', '-', '|', ' ', ' ', '-', '|', ' ', ' ', '-', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '-', ' ', ' ', '|', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , '|',  0 , ' ' , 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ' , 0 , '|',  0 , '|',  0 , ' ',  0 ],
		   ['-', '-', '-', ' ', ' ', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', ' ', '|', ' ', ' ', ' '],
		   [ 0 , ' ',  5 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ' , 0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ' , 0 , '|',  0 , '|',  0 , ' ',  0 ],
		   ['-', '-', '-', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', '-', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', '-', '|', ' ', '|', '-', '-', '-'],
		   [ 0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ' , 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|' , 0 , '|',  0 , '|',  0 , ' ',  0 ],
		   [' ', ' ', ' ', '|', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', ' ', '|', ' ', ' ', '-'],
		   [ 0 , ' ',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ' , 4 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ' , 0 , '|',  0 , '|',  0 , '|',  0 ],
		   ['-', '-', '-', ' ', ' ', '|', ' ', ' ', '-', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', '-', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', '-', '-', '-', '|', '-', '-', '-'],
		   [ 0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , ' ' , 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|' , 0 , ' ',  0 , '|',  0 , ' ',  0 ],
		   ['-', '-', '-', '-', '-', '-', '-', '|', '-', '-', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
		   [ 0 , ' ',  4 , ' ',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|' , 0 , '|',  0 , ' ',  0 , '|',  2 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|' , 0 , ' ',  0 , '|',  0 , ' ',  0 ],
		   ['-', '-', '-', '-', '-', '-', '-', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', '-', '-', '-', '|', '-', '|', '-', '-', '-', '-', '-', '-', '-'],
		   [ 0 , '|',  0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  5 , '|' , 0 , '|',  0 , ' ',  0 , '|',  0 , ' ',  0 , '|',  0 , '|',  0 , '|',  0 , '|' , 0 , ' ',  0 , ' ',  0 , '|',  1 ],
		   ['-', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', '-', '|', ' ', '|', '-', '-', '-', '-', '-', '-', '-', '|', ' ', ' ', '-', ' ', ' ', '|', ' ', ' ', ' ', ' ', '-', ' ', ' '],
		   [ 0 , ' ',  0 , '|',  0 , ' ',  2 , '|',  0 , '|',  0 , '|' , 0 , '|',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|',  0 , ' ',  0 , ' ',  0 , '|' , 1 , ' ',  0 , '|',  0 , ' ',  0 ]]

rooms5 = [[(0, 0), (0, 1), (1, 0), (1, 1), (2, 1)],
		  [(0, 2), (0, 3), (1, 2)],
		  [(0, 4), (0, 5), (1, 5), (2, 5), (2, 6)],
		  [(0, 6), (0, 7), (1, 6)],
		  [(0, 8)],
		  [(0, 9), (0, 10), (0, 11)],
		  [(0, 12), (0, 13)],
		  [(0, 14)],
		  [(0, 15), (0, 16), (0, 17), (1, 15), (1, 16)],
		  [(1, 3), (1, 4), (2, 3)],
		  [(1, 7), (1, 8), (2, 7), (2, 8)],
		  [(1, 9), (1, 10), (2, 9), (2, 10)],
		  [(1, 11), (1, 12), (1, 13), (2, 11), (2, 12)],
		  [(1, 14), (2, 13), (2, 14)],
		  [(1, 17)],
		  [(2, 0)],
		  [(2, 2), (3, 0), (3, 1), (3, 2), (4, 2)],
		  [(2, 4)],
		  [(2, 15), (3, 15), (4, 15), (5, 15)],
		  [(2, 16), (2, 17), (3, 16), (3, 17)],
		  [(3, 3), (3, 4), (4, 3), (4, 4)],
		  [(3, 5), (3, 6), (4, 5), (4, 6)],
		  [(3, 7)],
		  [(3, 8), (4, 7), (4, 8)],
		  [(3, 9), (3, 10), (4, 9), (4, 10)],
		  [(3, 11), (3, 12), (4, 11), (4, 12)],
		  [(3, 13), (3, 14), (4, 13)],
		  [(4, 0), (4, 1), (5, 0), (5, 1)],
		  [(4, 14)],
		  [(4, 16), (4, 17), (5, 16)],
		  [(5, 2), (6, 1), (6, 2)],
		  [(5, 3), (5, 4), (6, 3)],
		  [(5, 5), (5, 6), (6, 5), (6, 6)],
		  [(5, 7), (5, 8), (6, 7), (6, 8)],
		  [(5, 9)],
		  [(5, 10), (6, 9), (6, 10)],
		  [(5, 11), (5, 12), (6, 11), (6, 12)],
		  [(5, 13), (5, 14), (6, 13)],
		  [(5, 17)],
		  [(6, 0)],
		  [(6, 4)],
		  [(6, 14), (6, 15), (7, 14), (7, 15)],
		  [(6, 16), (6, 17), (7, 16), (7, 17)],
		  [(7, 0), (7, 1), (7, 2), (7, 3)],
		  [(7, 4), (7, 5), (8, 4), (8, 5), (9, 4)],
		  [(7, 6), (8, 6), (9, 6)],
		  [(7, 7), (7, 8), (8, 7), (8, 8)],
		  [(7, 9), (7, 10), (8, 9), (8, 10)],
		  [(7, 11), (7, 12)],
		  [(7, 13)],
		  [(8, 0)],
		  [(8, 1), (9, 0), (9, 1)],
		  [(8, 2), (8, 3), (9, 2), (9, 3)],
		  [(8, 11), (8, 13), (9, 11), (9, 12), (9, 13)],
		  [(8, 12)],
		  [(8, 14), (8, 15), (8, 16), (9, 14), (9, 15)],
		  [(8, 17), (9, 16), (9, 17)],
		  [(9, 5)], 
		  [(9, 7)],
		  [(9, 8), (9, 9), (9, 10)]]

answer5 = [[1, 2, 1, 3, 4, 1, 2, 3, 1, 2, 1, 3, 1, 2, 1, 3, 2, 4],
		   [5, 4, 2, 1, 3, 2, 1, 4, 3, 1, 2, 1, 3, 4, 2, 1, 5, 1],
		   [1, 3, 4, 2, 1, 3, 5, 2, 1, 3, 4, 2, 5, 3, 1, 2, 4, 3],
		   [2, 5, 3, 4, 2, 1, 3, 1, 2, 4, 3, 1, 2, 1, 3, 4, 2, 1],
		   [4, 2, 1, 3, 1, 4, 2, 3, 1, 2, 1, 3, 4, 2, 1, 3, 1, 2],
		   [3, 1, 2, 1, 3, 2, 4, 1, 3, 1, 2, 4, 3, 1, 2, 1, 3, 1],
		   [1, 3, 1, 2, 1, 3, 1, 2, 4, 3, 1, 2, 1, 3, 4, 2, 1, 3],
		   [2, 4, 3, 1, 2, 1, 3, 4, 1, 2, 3, 1, 2, 1, 3, 1, 2, 4],
		   [1, 2, 1, 3, 4, 5, 1, 3, 2, 4, 1, 3, 1, 5, 2, 3, 4, 1],
		   [3, 1, 4, 2, 3, 1, 2, 1, 3, 1, 2, 1, 4, 2, 1, 5, 3, 2]]

#######################################################################
# Run test cases                                                      #
#######################################################################

csp1, var_array1 = ripple_effect_csp_model(puzzle1, rooms1)
csp2, var_array2 = ripple_effect_csp_model(puzzle2, rooms2)
csp3, var_array3 = ripple_effect_csp_model(puzzle3, rooms3)
csp4, var_array4 = ripple_effect_csp_model(puzzle4, rooms4)
csp5, var_array5 = ripple_effect_csp_model(puzzle5, rooms5)

method = input("Choose propagation method (FC, GAC, both):\t")
print("")
while not (method == 'FC' or method == 'GAC' or method == 'both'):
	method = input('Input valid propagation method (FC, GAC, both):\t')
	print("")

print("==================================================")

print("\t< PUZZLE 1 >")
print("")
print_puzzle(puzzle1)
print("")

solver1 = BT(csp1)

if method == 'FC' or method == 'both':
	print("*** Backtracking with FC Propagation")
	solver1.bt_search(prop_FC)
	print("")
	print("\t< FC SOLUTION >")
	print("")
	print_solution(var_array1, puzzle1)
	print("")
	print_correct(var_array1, answer1)
	print("")

if method == 'GAC' or method == 'both':
	print("*** Backtracking with GAC Propagation")
	solver1.bt_search(prop_GAC)
	print("")
	print("\t< GAC SOLUTION >")
	print("")
	print_solution(var_array1, puzzle1)
	print("")
	print_correct(var_array1, answer1)
	print("")

print("==================================================")

print("\t< PUZZLE 2 >")
print("")
print_puzzle(puzzle2)
print("")

solver2 = BT(csp2)

if method == 'FC' or method == 'both':
	print("*** Backtracking with FC Propagation")
	solver2.bt_search(prop_FC)
	print("")
	print("\t< FC SOLUTION >")
	print("")
	print_solution(var_array2, puzzle2)
	print("")
	print_correct(var_array2, answer2)
	print("")

if method == 'GAC' or method == 'both':
	print("*** Backtracking with GAC Propagation")
	solver2.bt_search(prop_GAC)
	print("")
	print("\t< GAC SOLUTION >")
	print("")
	print_solution(var_array2, puzzle2)
	print("")
	print_correct(var_array2, answer2)
	print("")

print("==================================================")

print("\t< PUZZLE 3 >")
print("")
print_puzzle(puzzle3)
print("")

solver3 = BT(csp3)

if method == 'FC' or method == 'both':
	print("*** Backtracking with FC Propagation")
	solver3.bt_search(prop_FC)
	print("")
	print("\t< FC SOLUTION >")
	print("")
	print_solution(var_array3, puzzle3)
	print("")
	print_correct(var_array3, answer3)
	print("")

if method == 'GAC' or method == 'both':
	print("*** Backtracking with GAC Propagation")
	solver3.bt_search(prop_GAC)
	print("")
	print("\t< GAC SOLUTION >")
	print("")
	print_solution(var_array3, puzzle3)
	print("")
	print_correct(var_array3, answer3)
	print("")

print("==================================================")

print("\t< PUZZLE 4 >")
print("")
print_puzzle(puzzle4)
print("")

solver4 = BT(csp4)

if method == 'FC' or method == 'both':
	print("*** Backtracking with FC Propagation")
	solver4.bt_search(prop_FC)
	print("")
	print("\t< FC SOLUTION >")
	print("")
	print_solution(var_array4, puzzle4)
	print("")
	print_correct(var_array4, answer4)
	print("")

if method == 'GAC' or method == 'both':
	print("*** Backtracking with GAC Propagation")
	solver4.bt_search(prop_GAC)
	print("")
	print("\t< GAC SOLUTION >")
	print("")
	print_solution(var_array4, puzzle4)
	print("")
	print_correct(var_array4, answer4)
	print("")

print("==================================================")

print("\t< PUZZLE 5 >")
print("")
print_puzzle(puzzle5)
print("")

solver5 = BT(csp5)

if method == 'FC' or method == 'both':
	print("*** Backtracking with FC Propagation")
	solver5.bt_search(prop_FC)
	print("")
	print("\t< FC SOLUTION >")
	print("")
	print_solution(var_array5, puzzle5)
	print("")
	print_correct(var_array5, answer5)
	print("")

if method == 'GAC' or method == 'both':
	print("*** Backtracking with GAC Propagation")
	solver5.bt_search(prop_GAC)
	print("")
	print("\t< GAC SOLUTION >")
	print("")
	print_solution(var_array5, puzzle5)
	print("")
	print_correct(var_array5, answer5)
	print("")

print("==================================================")




