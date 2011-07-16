class ArabicToRoman
  ROMAN_NUMBERS = {
    1 => 'I', # 1 is not really needed, but is kept for simpler symbol extraction
    5 => 'V',
    10 => 'X',
    50 => 'L',
    100 => 'C',
    500 => 'D',
    1000 => 'M'
  }

  def self.convert( arabic )
    roman = ''

    numbers = ROMAN_NUMBERS.keys.to_a.reject{ | number | number == 1 }.reverse
    numbers.each_with_index do | number, index |
      # take care of multipliers of number
      multiplier = arabic / number
      roman += ROMAN_NUMBERS[ number ] * multiplier
      arabic -= multiplier * number

      # take care of the remainder
      # which can be calculated as subtraction from the current number by the previous number
      # see if current arabic value is within number - 1st or 2nd previous number
      # 1st is used only for 50 and 500, otherwise 2nd is used
      previous = numbers[ index + ( number == 50 || number == 500 ? 1 : 2 ) ]
      previous = 1 if !previous
      if arabic >= number - previous
        roman += ROMAN_NUMBERS[ previous ] + ROMAN_NUMBERS[ number ]
        arabic -= number - previous
      end
    end

    # take care of primitives ( 1 .. 3 )
    roman += 'I' * arabic

    return roman unless roman.empty?
  end
end