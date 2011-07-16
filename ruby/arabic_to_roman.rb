class ArabicToRoman
  def self.convert( number )
	result = ''
    {
		1000 => 'M',
		900 => 'CM',
		500 => 'D',
		400 => 'CD',
		100 => 'C',
		90 => 'XC',
		50 => 'L',
		40 => 'XL',
		10 => 'X',
		9 => 'IX',
		5 => 'V',
		4 => 'IV',
		1 => 'I',
	}.each do | arabic, roman |
		while number >= arabic
			result += roman
			number -= arabic
		end
	end
	
	result unless result.empty?
  end
end