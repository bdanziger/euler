# Reflexive Position is defined as : S is an infinite string of positive integers concatenated together starting at 1
#                                    f(n) is the starting position of the nth occurrence of n in S.
class ReflexivePosition:
    def __init__(self, howManyToAdd = 10, debug=False):
        self.howManyToAdd = howManyToAdd
        self.debug = debug

    def f(self, number):

        # validate input parameters
        if number <= 0:
            return 0;

        # This will be the position in the infinite string.  We have to keep track of the total based on each search and
        # the result of that search
        indexCount = 0

        # initialize how many matches you found so far (foundCount)
        foundCount = 0

        # initialize the infinite string
        bigString = InfiniteString();

        # this is the string number that we are looking for, number times
        pattern = str(number)

        if self.debug: 
            print 'looking for pattern : ', pattern, 'in bigString : ', bigString.toString()

        # we have to look until we found the string pattern 'number' times
        while foundCount <> number:

            # look for the pattern in the current window of the infinite string
            index = bigString.toString().find(pattern)

            # while we haven't found it yet, we have to do a few thing
            # 1) determine how many characters you need to keep around in the infinite string for the next search.
            #    a) if your pattern is bigger than your infinite string window, then you cannot get rid of anything
            #    b) otherwise, you have to keep around the size of the pattern you are looking for -1.  This is because
            #       it doesn't make sense to keep around the size of the entire pattern since you already didn't find it.
            #       So, the next best thing you can do is to keep around 1 less than that pattern size in case you missed 
            #       the match by 1 character
            # 2) We will need to add an additional set of digits to the end so we haven't matched yet on what we have
            # 3) Maintain the position count by adding what we are shifting away and no longer using
            # 4) search again with the new infinite string
            while index == -1:

                if self.debug: 
                    print 'not found'

                lookingToKeep = min(len(pattern) - 1, len(bigString.toString()))
                indexCount += (len(bigString.toString()) - lookingToKeep)
                bigString.keepLast(lookingToKeep)
                bigString.addMoreDigits()

                if self.debug: 
                    print 'bigString adjust due to not found : ', bigString.toString()

                index = bigString.toString().find(pattern)

            if self.debug: 
                print 'FOUND pattern', pattern, ' at index : ', index

            # Now that we matched the pattern we will need to 
            # 1) Maintain the position count by adding the find index (+1 because index starts at 0)
            # 2) Maintain hoow many times you found a match by adding one more
            # 3) Get rid what you no longer need which is everything up to and including the first found character
            # 4) There is no reason to add more digits yet since we don't really know yet if we actually need to
            indexCount += (index + 1)
            foundCount += 1
            bigString.keepLast(len(bigString.toString()) - (index + 1))

            if self.debug: 
                print 'bigString adjust due to found : ', bigString.toString()

        # at this point, we have found the pattern the correct number of times
        if self.debug: 
            print 'FOUND complete pattern', pattern, ' for number = ', number, ' at index : ', index, ' indexCount : ', indexCount

        return indexCount

# This class provides an infinite string of numbers from 1 to infinity, but only keeps around a window of the string that is being worked on.  Basically, the 
# string is designed to shift the numbers to the left off as you no longer need them and add more on to the right as you need them.
# This class is important to working with searching through infinite strings where you really cannot have infinite memory.
#
# So, for example, you can start with 12345678910, then decide you are finished with the first 6, so you keep 78910, then you might determine
# you need more numbers so you add more on 789101112131415...and so on.

class InfiniteString:
    def __init__(self, howManyToAdd=10):
        self.lastNumber = 0
        self.bigString = ""
        self.howManyToAdd = howManyToAdd
        self.addMoreDigits()

    # Return the current infinite string window
    def toString(self):
        return str(self.bigString)

    # retain the rightmost characters of the infinite string.  Basically sliding left and shifting off the left most numbers (out of the window)
    def keepLast(self, amountToKeep):
        # have to protect against 0 or less than 0
        if amountToKeep <= 0:
            self.bigString = ""
        else:
            self.bigString = self.bigString[-amountToKeep:]

    # add additional numbers to the window.  Realize, you start where you last left off adding.
    def addMoreDigits(self):

        #initialize to 0 in case you don't make it into the for loop. ie. for negative numbers in howManyToAdd
        index = 0

        for index in range (self.lastNumber + 1, self.lastNumber + 1 + self.howManyToAdd):
            self.bigString += str(index)

        self.lastNumber = index
