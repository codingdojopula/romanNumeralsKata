# -*- coding: utf-8 -*-

import unittest as mod_unittest

import romannumerals as mod_roman

class Test( mod_unittest.TestCase ):

	def test_1( self ):
		self.assertTrue( mod_roman.convert( 1 ) == 'I' )

	def test_5( self ):
		self.assertTrue( mod_roman.convert( 5 ) == 'V' )

	def test_less_than_10( self ):
		self.assertTrue( mod_roman.convert( 2 ) == 'II' )
		self.assertTrue( mod_roman.convert( 3 ) == 'III' )
		self.assertTrue( mod_roman.convert( 4 ) == 'IV' )
		self.assertTrue( mod_roman.convert( 6 ) == 'VI' )
		self.assertTrue( mod_roman.convert( 7 ) == 'VII' )
		self.assertTrue( mod_roman.convert( 8 ) == 'VIII' )
		self.assertTrue( mod_roman.convert( 9 ) == 'IX' )

	def test_10( self ):
		self.assertTrue( mod_roman.convert( 10 ) == 'X' )

	def test_50( self ):
		self.assertTrue( mod_roman.convert( 50 ) == 'L' )

	def test_less_than_100_endind_with_0( self ):
		self.assertTrue( mod_roman.convert( 20 ) == 'XX' )
		self.assertTrue( mod_roman.convert( 30 ) == 'XXX' )
		self.assertTrue( mod_roman.convert( 40 ) == 'XL' )
		self.assertTrue( mod_roman.convert( 60 ) == 'LX' )
		self.assertTrue( mod_roman.convert( 70 ) == 'LXX' )
		self.assertTrue( mod_roman.convert( 80 ) == 'LXXX' )
		self.assertTrue( mod_roman.convert( 90 ) == 'XC' )

	def test_100( self ):
		self.assertTrue( mod_roman.convert( 100 ) == 'C' )

	def test_500( self ):
		self.assertTrue( mod_roman.convert( 500 ) == 'D' )

	def test_less_than_1000_endind_with_00( self ):
		self.assertTrue( mod_roman.convert( 200 ) == 'CC' )
		self.assertTrue( mod_roman.convert( 300 ) == 'CCC' )
		self.assertTrue( mod_roman.convert( 400 ) == 'CD' )
		self.assertTrue( mod_roman.convert( 600 ) == 'DC' )
		self.assertTrue( mod_roman.convert( 700 ) == 'DCC' )
		self.assertTrue( mod_roman.convert( 800 ) == 'DCCC' )
		self.assertTrue( mod_roman.convert( 900 ) == 'CM' )

	def test_sample_numbers( self ):
		self.assertTrue( mod_roman.convert( 15 ) == 'XV' )
		self.assertTrue( mod_roman.convert( 19 ) == 'XIX' )
		# TODO: More tests


if __name__ == '__main__':
	mod_unittest.main()
