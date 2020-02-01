### MATH MODULE
# Math class:
BUZZ = "Buzz"
FIZZ = "Fizz"


class FizzBuzzChecker:
    def isDivisible(number, modulenumber):
        if number == 0:
            return False
        else:
            return number % modulenumber == 0
    def isFizz(number):
        return FizzBuzzChecker.isDivisible(number,3) or "3" in str(number)

    def isBuzz(number):
        return FizzBuzzChecker.isDivisible(number,5) or "5" in str(number)

    def checkFizzBuzz(number):
        stringfinal = ""
        if FizzBuzzChecker.isFizz(number):
            stringfinal = stringfinal + FIZZ
        if FizzBuzzChecker.isBuzz(number):
            stringfinal = stringfinal + BUZZ
        if not (FizzBuzzChecker.isFizz(number) or FizzBuzzChecker.isBuzz(number)):
            return str(number)
        return stringfinal
