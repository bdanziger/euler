# Lyhcrel numbers are defined as never becoming palindromes in less than 50 iterations of reversing the number and adding it back to itself
class Lychrel:
    def __init__(self, number, debug=False):
        self.debug = debug
        self.number = number

    # valid instance number check
    def validNumber(self):

        return self.number >= 1

    # see if the instance number is the same as the reverseof of that nubmer.
    # method is provided as a minor convenience of not having to pass in a number to the palindome function
    def isPalindrome(self):

        return isPalindrome(self.number)

    # see if the instance number is both a palindome itself and a lychrel number
    def isLychrelAndPalindrome(self):

        return self.isPalindrome() and self.isLychrel()

    # return the number of lychrel numbers between fromNumber and toNumber inclusive - static method, does not require an instance.
    # Kept with the class because it is a convenience method that makes use of this class
    @staticmethod
    def isLychrelCount(fromNumber, toNumber):

        count = 0;

        for number in range(fromNumber, toNumber + 1):
            
            if Lychrel(number).isLychrel():
                count += 1

        return count

    def isLychrel(self):

        # validate instance number, 0 and negative numbers will return false by definition
        if not self.validNumber():
            return False

        #initialize variables
        found = False
        iterations = 1

        # create the ReverseSum instance
        revSumInstance = ReverseSum(self.number)

        # loop through 49 iterations to see if a reverseSum is also a palindome
        while (iterations < 50) and not found:

            if isPalindrome(revSumInstance.getReverseSum()):
                found = True

            else:
                iterations += 1
                revSumInstance = ReverseSum(revSumInstance.getReverseSum())

        # print if found NON lychrel numbers and its palindrome and after how many iterations
        if found:
            if self.debug:
                print ('Non Lychrel Number : ' + str(self.number) + ', Palindrome : ' + str(revSumInstance.getReverseSum()) + ', Iterations : ' + str(iterations))
        else:
            if self.debug:
                print ('Lychrel Number : ' + str(self.number))

        # if Palindome found, this is NON Lychrel, if Palindrome not found, then it is a lychrel.
        return (not found)

# setup object to contain some number, it's reverse and the sum of the number and it's reverse
class ReverseSum:
    def __init__(self, paramNumber):

        self.number = paramNumber
        self.reverseNumber = str(paramNumber)[::-1]
        self.reverseSum = int(self.number) + int(self.reverseNumber)

    # getter
    def getReverseSum(self):
        return self.reverseSum

    # getter
    def getNumber(self):
        return self.number

    # getter
    def getReverseNumber(self):
        return self.reverseNumber

# see if an integer number passed in is the same as the reverseof that nubmer.  Negative numbers will be defined as not palindomes
def isPalindrome(intNumber):

    if intNumber < 0:
        return False

    return str(intNumber) == str(intNumber)[::-1]
