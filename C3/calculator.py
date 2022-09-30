import string

class Calculator:
    def eval(self, expression):
        valid = True
        result = 0

        #tests for missing or duplicate addition symbols
        if len(expression.split("+")) == 2:
            a, b, isValid = self.numParse(expression.split("+"))
            result = a + b
            valid = isValid
        else:
            valid = False

        #return value is printed, so type does not matter
        if valid == False:
            return "Invalid input, please check your value and try again"
        return result

    def run(self):
        # Run until the user cancels, ctl + C
        while True:
            expression = input('Enter an infix addition statement: ')
            result = self.eval(expression)
            print(' = ', result)

    def numParse(self, numStr):
        valid = True
        num1 = 0
        num2 = 0

        #removes cases of where whitespace characters occur
        str1 = self.rmSpace(numStr[0])
        str2 = self.rmSpace(numStr[1])

        iter = 0
        for cleanStr in str1, str2:
            #set flags for loop
            isNeg = False
            isFloat = False

            #check for negative sign
            if cleanStr[0] == "-":
                isNeg = True
                cleanStr = cleanStr[1:]

            #calculate magnitude
            newDig = 0
            total = 0
            decPlace = 0
            isDigit = True
            for digit in cleanStr:
                #parses string digit to int or float digit

                #note: while it would be possible to parse spelled out numbers ex. "three"
                #most languages do not recognize these as valid expression values, so this
                #has not been implemented
                if digit == '0':
                    newDig = 0
                elif digit == '1':
                    newDig = 1
                elif digit == '2':
                    newDig = 2
                elif digit == '3':
                    newDig = 3
                elif digit == '4':
                    newDig = 4
                elif digit == '5':
                    newDig = 5
                elif digit == '6':
                    newDig = 6
                elif digit == '7':
                    newDig = 7
                elif digit == '8':
                    newDig = 8
                elif digit == '9':
                    newDig = 9
                elif digit == '.' or digit == ',': #comma may replace decimal in keeping with international conventions
                    isDigit = False
                    if not isFloat:
                        isFloat = True
                        decPlace = -1
                    else:
                        valid = False
                        #returns early to prevent unnecessary code from running
                        return (num1, num2, valid)
                else:
                    valid = False
                    return (num1, num2, valid)

                #adds current character/digit to total sum (if applicable)
                if (not isFloat) and isDigit:
                    total = total*10 + newDig
                elif isDigit:
                    total = total + newDig*(10**decPlace)
                    decPlace -= 1
                isDigit = True

            #check for negativity
            if isNeg == True:
                total = total*(-1)

            #checks which number to assign result to
            if iter == 0:
                num1 = total
            elif iter == 1:
                num2 = total

            iter += 1

        return (num1, num2, valid)

    def rmSpace(self, strIn):
        "Removes all whitespace in string"
        result = strIn
        for space in string.whitespace:
            result = result.replace(space, "")
        return result

if __name__ == "__main__":
    # If this file is run directly from the command line, run the calculator
    c = Calculator()
    c.run()