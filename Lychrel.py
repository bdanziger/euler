# Lycrel numbers are defined as never becoming palindromes in less than 50 iterations of reversing the number and adding it back to itself
class Lychrel:
    def __init__(self, debug=False):
        self.debug = debug

    # Returns the number of Lychrel numbers between startNumber and endNumber
    def fromTo(self, startNumber, endNumber):

        lychrelNumbers = []
        lychrelNumsAlsoPal = []

        # setup to loop through the numbers startNumber through endNumber  to look for Lychrel numbers
        for index in range (startNumber, endNumber+1):
        
            iterations = 1
            done = False

            # setup the ReverseSum Object for this number
            revSumInstance = ReverseSum(index)

            # Lychrel numbers are defined to not have Palindromes of reverse sums for the first 49 iterations
            while (iterations < 50) and not done:
        
                # check to see if reverse sum is a palindrome
                if palindrome(revSumInstance.getReverseSum()):
                    done = True
                else:
                    # if not a palindrome, setup another ReverseSum Object of the Reverse sum of the current number
                    revSumInstance = ReverseSum(revSumInstance.getReverseSum())
    
                    iterations += 1

            # print any found NON lychrel numbers and their palindromes and iterations
            if done:
                if self.debug:
                    print ('Number : ' + str(index) + ', Palindrome : ' + str(revSumInstance.getReverseSum()) + ', Iterations : ' + str(iterations))

            else:
                # Found a lychrel number
                # check to see if this lychrel number is also a Palindrome and if so, add to lychrel numbers that are also palindromes list
                if palindrome(index):
                    lychrelNumsAlsoPal.append(index)

                # add this lychrel number to the lychrel numbers list
                lychrelNumbers.append(index)

        # Print Lycrhel Numbers
        if self.debug:
            print ('')
            print (str(len(lychrelNumbers)) + ' LYCHREL NUMBERS LESS THAN 10,000')
            print lychrelNumbers


            # Print Lychrel Numbers that are themselves Palindromes
            print ('')
            print (str(len(lychrelNumsAlsoPal)) + ' LYCHREL NUMBERS THAT ARE THEMSELVES PALINDROMES')
            print lychrelNumsAlsoPal

        return len(lychrelNumbers)

# setup object to contain some number, it's reverse and the sum of the number and it's reverse
class ReverseSum:
    def __init__(self, paramNumber):

        self.number = paramNumber
        self.reverseNumber = str(paramNumber)[::-1]
        self.reverseSum = int(self.number) + int(self.reverseNumber)

    def getReverseSum(self):
        return self.reverseSum

# see if an integer number passed in is the same as the reverseof that nubmer
def palindrome(intNumber):
    return str(intNumber) == str(intNumber)[::-1]
