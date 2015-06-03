# euler
This repository will contain projects related to the Euler Project

=====================================
LYCHREL - Problem 55
=====================================

Lychrel.py defines a class called Lychrel which will generate Lychrel numbers as defined in the Euler Project

instantiation : lychrelInstance = Lychrel()
or              lychrelInstance = Lychrel(debug=True) 

setting debug=True as shown above will output additional details as the Lychrel methods are executed

methods : fromTo(startNumber, endNumber)
fromTo will return the sum of Lychrel numbers from startNumber through endNumber inclusive

example : print 'Lychrel numbers from 5 to 10 : ', lychrelInstance(5, 10)
example : print 'Lychrel numbers 10 to 10 : ', lychrelInstance(10,10)

----------

Supporting methods and Classes in Lychrel.py 

Class ReverseSum :

This class will store a number in the instance, store it's reverse, and store the sum of the number and it's reverse

Example : revInstance = ReverseSum(1234) will create an instance where by the instance stores the number 1234, it's reverse 4321 and their sum of 5555

instantiation : revInstance = ReverseSum(number)

methods : getReverseSum() will return the reverseSum that is stored in the instance

example : print 'The reverse sum of 1234 is : ', revInstance.getReverseSum(1234)
> The reverse sum of 1234 is : 5555

----------
methods palindrome : 

This method returns whether or not the argument is a palindrome

example : print '123321 is a palindrome : ', palindrome(123321)
> 123321 is a palindrome ; True

Running the Lychrel project : 
MainLychrel.py contains the Main program that will run the stated problem as defined in the Euler Project
It will also test and show the 3 palindromes < 10,000 that are also Lychrel numbers

python MainLychrel.py

Output : 

Palindrome 4994 that is also a Lychrel number True
Palindrome 8778 that is also a Lychrel number True
Palindrome 9999 that is also a Lychrel number True
number of Lychrel numbers below 10,0000 :  249

=====================================

ReflexivePosition - Problem 305

=====================================

ReflexivePosition.py defines a class called ReflexivePosition which will generate Reflexive Positions as defined in the Euler Project

instantiation : refPoslInstance = ReflexivePosition()
or              refPosInstance = ReflexivePosition(debug=True) 

setting debug=True as shown above will output additional details as the ReflexivePosition methods are executed

methods : fromTo(startNumber, endNumber)
