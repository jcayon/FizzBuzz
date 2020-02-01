import mathmodule
def main():
    initNumber = int(input("Escribe numero inicial: "))
    maxNumber = int(input("Escribe numero final: "))
    fizzbuzzcalculator = mathmodule.FizzBuzzChecker
    for current in range(initNumber,maxNumber):
        outputstring = fizzbuzzcalculator.checkFizzBuzz(current)
        print(outputstring," - ", end='')

if __name__  == "__main__":
    main()