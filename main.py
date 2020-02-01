import mathmodule
def main():
    maxNumber=100
    fizzbuzzcalculator = mathmodule.Math
    for current in range(1,maxNumber):
        outputstring = fizzbuzzcalculator.checkFizzBuzz(current)
        print(outputstring)

if __name__  == "__main__":
    main()