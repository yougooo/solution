# python 2.7.6

class Converter(object):
    def __init__(self):
        self.roman_numbers = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        self.exception_numbers = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM', 1: 'I',
                                  2: 'II', 3: 'III', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII'}

    def level(self):
        """:return list with rank of inputted number
        numbers like 6, 60, 0, 2000"""
        temp = map(lambda x: self.num % 10**x, range(1, len(str(self.num))+1))
        rank = [temp[0]]
        rank.extend([temp[i+1]-temp[i] for i in range(len(temp) - 1)])
        return rank

    def roman_number(self, temp_num):
        """:param temp_num: one int number from list
           after function level()
           :return temp_num like roman number"""

        if temp_num in self.exception_numbers.keys():
            return self.exception_numbers[temp_num]
        elif temp_num == 0:
            return ''
        limit_min = temp_num/int(str(temp_num)[0])
        index = filter(lambda x: limit_min <= x <= temp_num, self.roman_numbers.keys())
        temp_roman = self.roman_numbers[max(index)]
        iterations = (temp_num-max(index)) / min(index)
        return temp_roman + ''.join(map(lambda x: self.roman_numbers[min(index)], range(iterations)))

    def convert(self, num):
        """:param num: arabic number
           :return num like roman nuber"""
        self.num = abs(num)
        ran_level = self.level()
        if any([self.num > 3999, self.num == 0]):
            return 'Your number out of range'
        res = map(lambda level_num: self.roman_number(level_num), ran_level)[::-1]
        return ''.join(res)
