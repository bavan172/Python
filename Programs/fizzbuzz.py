#Write a program that outputs the string representation of numbers from 1 to n.
#But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
#For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n):
        ans = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            if num % 3 == 0 and num % 5 == 0:
                ans.append("FizzBuzz")
            elif num % 3 == 0:
                ans.append("Fizz")
            elif num % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(num))

        return ans
