# -*- coding: utf-8 -*-

"""
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1,000
"""

ROMAN_1 = 'I'
ROMAN_5 = 'V'
ROMAN_10 = 'X'
ROMAN_50 = 'L'
ROMAN_100 = 'C'
ROMAN_500 = 'D'
ROMAN_1000 = 'M'

def __convert( number, q = 1, var_1 = ROMAN_1, var_5 = ROMAN_5, var_10 = ROMAN_10 ):
	n = number / q
	if n == 0:
		return ''
	elif n == 1:
		return var_1
	elif n == 2:
		return var_1 * 2
	elif n == 3:
		return var_1 * 3
	elif n == 4:
		return var_1 + var_5
	elif n == 5:
		return var_5
	elif n == 6:
		return var_5 + var_1
	elif n == 7:
		return var_5 + var_1 * 2
	elif n == 8:
		return var_5 + var_1 * 3
	elif n == 9:
		return var_1 + var_10
	return None

def __convert_simple_number( n ):
	""" "Simple numbers" are: n * 10^x ( n < 10 ) """
	if n < 10:
		return __convert( n )
	elif n < 100:
		return __convert( n, q = 10, var_1 = ROMAN_10, var_5 = ROMAN_50, var_10 = ROMAN_100 )
	elif n < 1000:
		return __convert( n, q = 100, var_1 = ROMAN_100, var_5 = ROMAN_500, var_10 = ROMAN_1000 )
	elif n < 3000:
		return __convert( n, q = 1000, var_1 = ROMAN_1000, var_5 = None, var_10 = None )
	
	return '?'

def convert( n ):
	parts = []
	temp = n
	while temp > 0:
		part = int( temp ) % 10
		part = part * 10 ** len( parts )
		parts.append( part )
		temp = int( temp ) / 10

	parts.reverse()

	result = ''
	for part in parts:
		result += __convert_simple_number( part )
	
	return result
