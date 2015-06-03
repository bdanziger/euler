# euler
This repository will contain projects related to the Euler Project

=====================================
LYCHREL - Problem 55
=====================================

class Lychrel :

Lychrel.py defines a class called Lychrel which will generate Lychrel numbers as defined in the Euler Project

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

Class ReverseSum :

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

ReflexivePosition.py defines a class called ReflexivePosition which will generate Reflexive Positions as defined in the Euler Project

instantiation : refPoslInstance = ReflexivePosition()
or              refPosInstance = ReflexivePosition(debug=True) 

setting debug=True as shown above will output additional details as the ReflexivePosition methods are executed

methods : fromTo(startNumber, endNumber)
