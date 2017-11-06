#!/usr/bin/python

UPPER_THRESHOLD = 10000


class Convert2Roman(int):
    """ This is one of the possible solutions, uses the class special methods to logically split the workload.
    
        New instance - validation
        Constructor - arabic to roman mapping
        Iterator - generator - performance efficient, reverses and slices the number, mapping it to basic decimal system to be used by 
        the C'tor to do further mapping.
        
        There are several ways and different algorithms to solve this problem (divmod ...), this one, in my opinion, 
        being the most in 'the parsing', as we have the mapping and values to be mapped...
        Performance-wise, it executes with a very small memory footprint and is pretty simple with just three execution steps.
        There is a graphical code representation in the repo root, REPR.PNG
     """
    def __new__(cls, number):

        if number > UPPER_THRESHOLD:
            raise ValueError('ONLY VALUES TO 10K (10000) ARE SUPPORTED: '.format(number))
        if number < 0:
            raise ValueError('NEGATIVE VALUES NOT SUPPORTED!')

        return super(Convert2Roman, cls).__new__(cls, number)

    def __init__(self, number):
        to_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
                    20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
                    200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
                    1000: 'M', 2000: 'MM', 3000: 'MMM', 4000: '~IV', 5000: '~V', 6000: '~VI', 7000: '~VII',
                    8000: '~VIII', 9000: '~IX', 10000: '~X'}
        self.roman = ''.join([to_roman.get(num) for num in self][::-1])

    def __iter__(self):
        number = self.__str__()
        count = 1
        for digit in number[::-1]:
            if digit != '0':
                yield int(digit) * count
            count *= 10


def roman_parse(number):
    if isinstance(number, int):
        num = Convert2Roman(number)
        return num.roman
