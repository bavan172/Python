# Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. 
# A factor is a number that evenly divides into another number, leaving no remainder.

# The rules of raindrops are that if a given number:
# has 3 as a factor, add 'Pling' to the result.
# has 5 as a factor, add 'Plang' to the result.
# has 7 as a factor, add 'Plong' to the result.
# does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

def convert(number):
    msg = ''.join(drop for divisor, drop in {3: "Pling", 5: "Plang",
                  7: "Plong"}.items() if number % divisor == 0)
    return msg if msg != '' else str(number)
