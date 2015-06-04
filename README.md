# euler
This repository will contain projects related to the Euler Project

=====================================
LYCHREL - Problem 55
=====================================

class Lychrel :

Lychrel.py defines a class called Lychrel which will generate Lychrel numbers as defined in the Euler Project #55

--------
INSTANTIATION : 
--------

lychrelInstance = Lychrel(number)

lychrelInstance = Lychrel(number, debug=True) 

setting debug=True as shown above will output additional details as the Lychrel methods are executed

--------
STATIC METHODS
--------
isLychrelCount(fromNumber, toNumber)

returns the number of Lychrel numbers between fromNumber and toNumber inclusive

example : print 'Lychrel numbers from 5 to 10 : ', Lychrel.isLychrelCount(5, 10)
example : print 'Lychrel numbers 10 to 10 : ', Lychrel.isLychrelCount(10, 10)

--------
CLASS METHODS
--------

validNumber() : returns true if instance number is >= 1

isPalindrome() : returns true if the instance number is a palindrome.  

isLychrelAndPalindrome() : returns true if instance number is both a Lychrel number and additionally a palindrome

isLychrel() returns true if the instance number is a Lychrel number

----------

ADDITIONAL CLASSES and/or Functions

----------

class ReverseSum :

This class will store a number in the instance, store it's reverse, and store the sum of the number and it's reverse

Example : revInstance = ReverseSum(1234) will create an instance where by the instance stores the number 1234, it's reverse 4321 and their sum of 5555

instantiation : revInstance = ReverseSum(number)

method : getReverseSum() will return the reverseSum that is stored in the instance

example : print 'The reverse sum of 1234 is : ', revInstance.getReverseSum(1234)
> The reverse sum of 1234 is : 5555

----------

FUNCTION 

----------

isPalindrome(number) : 

returns True/False as to whether or not the argument number is a palindrome

example : print '123321 is a palindrome : ', isPalindrome(123321)
> 123321 is a palindrome ; True

----------

RUNNING LYCHREL

----------

MainLychrel.py contains the Main program that will run the stated problem as defined in the Euler Project
It will also test and show the 3 palindromes < 10,000 that are also Lychrel numbers and some misc samples

python MainLychrel.py

OUTPUT : 

Palindrome 4994 is also a Lychrel number     :  True
Palindrome 8778 is also a Lychrel number     :  True
Palindrome 9999 is also a Lychrel number     :  True
Palindrome 1551 is NOT also a Lychrel number :  True

Palindrome 1551 is NOT also a Lychrel number (debug on) 
Non Lychrel Number : 1551, Palindrome : 5115, Iterations : 2

978 is Lychrel number shown two ways :  True

Number of Lychrel numbers below 10,0000 :  249

=====================================

ReflexivePosition - Problem 305

=====================================

class ReflexivePosition : 

ReflexivePosition.py defines a class called ReflexivePosition which will generate Reflexive Positions as defined in the Euler Project #305

--------
INSTANTIATION : 
--------

refPoslInstance = ReflexivePosition()
refPosInstance = ReflexivePosition(debug=True) 

setting debug=True as shown above will output additional details as the ReflexivePosition methods are executed

--------
CLASS METHODS
--------

f(number) : returns the reflexive position of number

----------

ADDITIONAL CLASSES and/or Functions

----------

class InfiniteString :

This class will create a window into an infinite string.  The infinite string is composed of the integers from 1 to n concatenated into a string.
The window starts at the left of the string 1234...
Once you start searching through the infinite string, you no longer need the characters to the left, so they slide out of the window.
As you need more numbers/characters to the right, you can add more.  The purpose of such a class is to conserve memory because technically, you 
cannot really have an infinite string without running out of memory.

--------
INSTANTIATION : 
--------

bigString = InfiniteString()

bigString = InfiniteString(howmany)

bigString = InfiniteString(howmany, debug=True)

howmany will default to 10 if it is not in the argument list
debug will default to false if it is not in the argument list

howmany determines how many characters the string starts with.  It is also used to determine how many digits to add to the right of the string window.
setting debug=True as shown above will output additional details as the InfiniteString methods are executed

--------
CLASS METHODS
--------

toString() : returns the current window of integer characters as a string

keepLast(number) : keeps the last 'number' of characters in the infiniteString window.  Effectively, removing from the left
example : keelLast(6) with a string of 123456789101112 will update the bigString to 101112

addMoreDigits() : will concatenate 'howmany' integer digits onto the right of the string, increasing the window to the right.
example addMoreDigits() with a string of 101112 (assume howmany = 5) will expand the bigString window to 1011121314151617

----------

RUNNING REFLEXIVE POSITION

----------

MainReflexivePosition.py contains the Main program that will run the stated problem as defined in the Euler Project
It will also test and show various misc hint examples that were provided with the problem

python MainReflexivePosition.py

OUTPUT : 

reflexive position of 1, should equal 1            :  True
reflexive position of 5, should equal 81           :  True
reflexive position of 12, should equal 271         :  True
reflexive position of 7780, should equal 111111365 :  True
sum of reflexive positions of 3^k 1<=k<=13, after k =  1 , total =  37
sum of reflexive positions of 3^k 1<=k<=13, after k =  2 , total =  206
sum of reflexive positions of 3^k 1<=k<=13, after k =  3 , total =  2414
sum of reflexive positions of 3^k 1<=k<=13, after k =  4 , total =  7139
sum of reflexive positions of 3^k 1<=k<=13, after k =  5 , total =  168152
sum of reflexive positions of 3^k 1<=k<=13, after k =  6 , total =  1094821
sum of reflexive positions of 3^k 1<=k<=13, after k =  7 , total =  15294209
sum of reflexive positions of 3^k 1<=k<=13, after k =  8 , total =  67775814
sum of reflexive positions of 3^k 1<=k<=13, after k =  9 , total =  1728200395
sum of reflexive positions of 3^k 1<=k<=13, after k =  10 , total =  9632403779
sum of reflexive positions of 3^k 1<=k<=13, after k =  11 , total =  160686572624
sum of reflexive positions of 3^k 1<=k<=13, after k =  12 , total =  538034026086

----------

TESTING REFLEXIVE POSITION

----------

There are 2 tests where each test tests many different scenarios

Test1 focus is testing ReflexivePosition
Test2 focus is testing InfiniteString

python test_reflexive_position.py

OUTPUT : 

..
----------------------------------------------------------------------
Ran 2 tests in 13.535s

OK



















