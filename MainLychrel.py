#!/usr/bin/python

from Lychrel import Lychrel

if __name__ == '__main__':

    # if you want to see debug info including which lychrel numbers are also themselves palindromes use debug=true
    #lychrel = Lychrel(debug=True)
    lychrel = Lychrel();

    # Lychrel.fromTo returns the number of lychrel numbers between two numbers
    # So, if you use only a number itself, it will return 1 if it is a lychrel number
    print 'Palindrome 4994 that is also a Lychrel number',  lychrel.fromTo(4994, 4994) == 1
    print 'Palindrome 8778 that is also a Lychrel number',  lychrel.fromTo(8778, 8778) == 1
    print 'Palindrome 9999 that is also a Lychrel number',  lychrel.fromTo(9999, 9999) == 1

    print 'number of Lychrel numbers below 10,0000 : ', lychrel.fromTo(0, 9999)


