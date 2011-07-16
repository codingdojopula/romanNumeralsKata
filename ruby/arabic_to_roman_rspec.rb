require "rubygems"
gem "rspec"

require_relative "arabic_to_roman"

describe "ArabicToRoman converter" do
  [
    [ 0, nil ],
    [ 1, 'I' ],
    [ 2, 'II' ],
    [ 3, 'III' ],
    [ 4, 'IV' ],
    [ 5, 'V' ],
    [ 6, 'VI' ],
    [ 9, 'IX' ],
    [ 10, 'X' ],
    [ 11, 'XI' ],
    [ 23, 'XXIII' ],
    [ 37, 'XXXVII' ],
    [ 46, 'XLVI' ],
    [ 50, 'L' ],
    [ 56, 'LVI' ],
    [ 100, 'C' ],
    [ 101, 'CI' ],
    [ 145, 'CXLV' ],
    [ 154, 'CLIV' ],
    [ 354, 'CCCLIV' ],
    [ 454, 'CDLIV' ],
    [ 500, 'D' ],
    [ 501, 'DI' ],
    [ 554, 'DLIV' ],
    [ 800, 'DCCC' ],
    [ 900, 'CM' ],
    [ 999, 'CMXCIX' ],
    [ 1000, 'M' ],
    [ 2000, 'MM' ],
    [ 2357, 'MMCCCLVII' ],
    [ 2537, 'MMDXXXVII' ],
    [ 2846, 'MMDCCCXLVI' ],
    [ 3497, 'MMMCDXCVII' ],
    [ 5497, 'MMMMMCDXCVII' ],
  ].each do | arabic, roman |
    it "It should romanize #{arabic}" do
      ArabicToRoman.convert( arabic ).should == roman
    end
  end
end