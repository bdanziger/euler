#!/usr/bin/python

from Lychrel import Lychrel

if __name__ == '__main__':

    # if you want to see debug info while using the Lychrel class include debug=True when instantiating 
    # Lychrel(number, debug=True)

    print 'Palindrome 4994 is also a Lychrel number     : ',  Lychrel(4994).isLychrelAndPalindrome()
    print 'Palindrome 8778 is also a Lychrel number     : ',  Lychrel(8778).isLychrelAndPalindrome()
    print 'Palindrome 9999 is also a Lychrel number     : ',  Lychrel(9999).isLychrelAndPalindrome()

    print 'Palindrome 1551 is NOT also a Lychrel number : ',  not Lychrel(1551).isLychrelAndPalindrome()

    print ('')
    print 'Palindrome 1551 is NOT also a Lychrel number (debug on) '
    Lychrel(1551, debug=True).isLychrelAndPalindrome()

    print('')
    print '978 is Lychrel number shown two ways : ',  (Lychrel(978).isLychrel()) and (Lychrel.isLychrelCount(978, 978) == 1)

    print ('')
    print 'Number of Lychrel numbers below 10,0000 : ', Lychrel.isLychrelCount(0, 9999)


