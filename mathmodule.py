### MATH MODULE
# Math class:
class Math:

    def module3(number):
        return number % 3 == 0

    def module5(number):
        return number % 5 == 0

    def module(number, modulenumber):
        return number % modulenumber == 0

    def checkFizzBuzz(number):
        stringfinal = ""
        if Math.module3(number):
            stringfinal = stringfinal + "Fizz"
        if Math.module5(number):
            stringfinal = stringfinal + "Buzz"
        if not (Math.module3(number) or Math.module5(number)):
            return str(number)
        return stringfinal
