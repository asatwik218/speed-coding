import unittest
import test
import math


class testquestions(unittest.TestCase):

    def divide(self, integer1, integer2):
        x = integer1 / integer2
        return x

    def almost_palindrome(self, string):
        

        return 0

    def multiply_Strings(self, string1, string2):
        return (int(string1) * int(string2))

    def Super_Palindrome(self, array1):

        return array1

    def trueorfalse(self, integer):
        r=0
        n=integer
        while(integer !=0):
            d=integer%10
            integer=integer//10
            r=r*10+d
        f=0
        f1=0
        for i in range(2,n):
            if n%i == 0:
                f=1
                break
        
        for i in range(2,r):
            if r%i == 0:
                f1=1
                break
        if(f==0 and f1==0):
            return 1
        else:
            return 0
        
        

    def find_gcd(self, integer1, integer2):
        if integer1 > integer2: 
            small = integer2 
        else: 
            small = integer1
        for i in range(1, small+1): 
            if((integer1 % i == 0) and (integer2 % i == 0)): 
                gcd = i               
        return gcd


    def average_String(self, string):
        array1=[]
        return array1  # returns an array

    def potential(self, string):
        m = ''
        # l = string.split("")
        # for i in l:
        #     asc=0
        #     for j in i :
        #         asc = asc+ord(j)

        return m

    def series(self, interger):
        array=[]
        for i in range(1,interger+1):
            array.append(i*i-1)
        return array  # returns an array

    def filename(self, string):
        m = ''
        return m

    def disarium(self, integer):
        n=integer
        c=0
        sum=0
        while(integer!=0):
            integer=integer/10
            c+=1
        integer=n
        while(n!=0):
            d=n%10
            n=n/10
            sum+=math.pow(d,c)
            c-=1
        if sum==integer:
            return 1
        else:
            return 0

    def factorial(self,integer):
        fact=1
        for i in range(1,integer+1):
            fact=fact*i
        return fact

    def special(self, integer):
        n=integer
        sum=0
        while(integer!=0):
            d=integer%10
            integer=integer/10
            sum+=self.factorial(d)
        if sum==n:
            return 1
        else:
            return 0

    def equalarr(self, array1, array2, integer1, integer2):
        if integer1!=integer2:
            return 0
        array1.sort() 
        array2.sort()
  
        for i in range(0, integer1 - 1): 
            if (array1[i] != array2[i]): 
                return 0  
        return 1; 
        

    def prime(self, integer):
        return array  # returns an array

    def automorphic(self, integer):
        return False

    def alphabetical(self, string):
        for i in range(0,len(string)-1):
            if ord(i) > ord(i+1) :
                return 0
            return 1

    def arrtostr(self, character):
        m = ''
        for i in character:
            m=m+i
        return m

    def specialarr(self, array, integer):
        return False

    def series1(self, integer):
        return 0

    def anagram(self, string1, string2):
        return False

    def netbill(self, double1):
        return 0.0

    def parcel(self, integer):
        return 0

    def vowels(self, string, integer):
        m = ''
        string =string.lower()
        for i in string:
            if(i == 'a' or i == 'o' or i == 'i' or i == 'e' or i == 'u'):
                m=m+i

        return m[0:integer-1]

    def maxfreq(self, string):
        ch = ''
        return ch  # returns a character

    def lastindex(self, string):
        return 0

    def dashes(self, integer):
        string = ""
        return string

    def permutations(self, string):
        string1 = []
        return string1  # returns an array

    def repeat(self, string):
        ch = ''
        return ch  # returns a character

    def singledigit(self, integer):
        return 0

    def happy(self, integer):
        return False

    def series2(self, integer):
        return 0

    def missingnum(self, array, integer):
        return 0

    def apocalyptic(self, integer):
        return False

    def alternate(self, array, integer):
        return 0

    def sorting(self, array, integer):
        return False

    def encrypt(self, string):
        a = ""
        return a  # returns a string

    def diagonalmatrix(self, array, integer):
        return False

    def armstrong(self, integer):
        return False

    def kempner(self, integer):
        return 0

    def rearrange(self, character, array):
        string = ""
        return string  # returns a string

    def ascending(self, integer):
        return False

    def descending(self, integer):
        return False

    def alphasort(self, array):
        array1 = []
        return array1  # returns an array

    def doubleletter(self, string):
        return 0

    def piglatin(self, string):
        a = ""
        return a

    def semiprime(self, integer):
        return False

    def balanced(self, integer):
        return False

    def even(self, array):
        return False

    def diagonals(self, array, integer):
        return 0

    def reverse(self, string):
        a = ""
        return a

    def triangular(self, integer):
        a = []
        return a  # returns an array
