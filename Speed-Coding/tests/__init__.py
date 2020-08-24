import unittest
from testquestions import testquestions


class test_case(unittest.TestCase):
    def test1(self):
        result = testquestions().divide(1, 1)
        self.assertEqual(1, result)

    if __name__ == '__main__':
        unittest.main()

    def test2(self):
        string1 = "abcbea"
        result = testquestions().almost_palindrome(string1)
        self.assertEqual(result, 0)

    if __name__ == '__main__':
        unittest.main()

    def test3(self):

        result1 = testquestions().multiply_Strings("50", "4")
        self.assertEqual(result1, 99)
        result2 = testquestions().multiply_Strings("150", "2")
        self.assertEqual(result2, 99)

    if __name__ == '__main__':
        unittest.main()

    def test4(self):
        a1 = [1, 2, 8, 3, 11, 121, 300, 22]
        a = [2, 3, 11, 22]

        result1 = testquestions().Super_Palindrome(a1)
        self.assertEqual(result1, a)
        b1 = [101, 4, 8, 9, 111, 121, 300, 22]
        b = [101, 111, 121, 22]
        result2 = testquestions().Super_Palindrome(b1)
        self.assertEqual(result2, b)

    if __name__ == '__main__':
        unittest.main()

    def test5(self):

        result = testquestions().trueorfalse(13)
        self.assertEqual(result, 1)
        result = testquestions().trueorfalse(23)
        self.assertEqual(result, 1)

    if __name__ == '__main__':
        unittest.main()

    def test6(self):

        result = testquestions().find_gcd(12, 16)
        self.assertEqual(result, 99)
        result = testquestions().find_gcd(250, 1000)
        self.assertEqual(result, 99)

    #
    if __name__ == '__main__':
        unittest.main()

    def test7(self):

        a1 = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."
        a = [382, 7]
        result1 = testquestions().average_String(a1)
        self.assertEqual(result1, [])
        b1 = "The best things in an artist’s work are so much a matter of intuition, that there is much to be said for the point of view that would altogether discourage intellectual inquiry into artistic phenomena on the part of the artist. Intuitions are shy things and apt to disappear if looked into too closely. And there is undoubtedly a danger that too much knowledge and training may supplant the natural intuitive feeling of a student, leaving only a cold knowledge of the means of expression in its place. For the artist, if he has the right stuff in him ..."
        b = [448, 4]
        result2 = testquestions().average_String(b1)
        self.assertEqual(result2, [])

    if __name__ == '__main__':
        unittest.main()

    def test8(self):
        a1 = "HOW DO YOU DO?"
        a = "DO DO HOW YOU"
        result1 = testquestions().potential(a1)
        self.assertEqual(result1, a)
        b1 = "THE SKY IS THE LIMIT"
        b = "IS THE THE SKY LIMIT"
        result2 = testquestions().potential(b1)
        self.assertEqual(result2, b)

    if __name__ == '__main__':
        unittest.main()

    def test9(self):
        a = [0, 3, 8, 15, 24, 35]
        result1 = testquestions().series(6)
        self.assertEqual(result1,[])
        b = [0, 3, 8, 15, 24, 35, 48, 63, 80]
        result2 = testquestions().series(9)
        self.assertEqual(result2,[])

    if __name__ == '__main__':
        unittest.main()

    def test10(self):
        result1=testquestions().filename("helloworld.java")
        result1=result1.split('.')
        self.assertEqual(result1,".java" )
        result2=testquestions().filename("helloworld")
        self.assertEqual(result2,"Not a file name")

    if __name__ == '__main__':
        unittest.main()

    def test11(self):
        self.assertEqual(1, testquestions.disarium(89))
        self.assertEqual(0, testquestions.disarium(311))

    if __name__ == '__main__':
        unittest.main()

    def test12(self):
        testquestions
        self.assertEqual(1, testquestions.special(40585))
        self.assertEqual(0, testquestions.special(147))

    if __name__ == '__main__':
        unittest.main()

    def test13(self):
        testquestions
        a = [51, 42, 23, 74]
        b = [51, 42, 23, 74]
        self.assertEqual(1, testquestions.equalarr(a, b, 4, 4))
        c = [51, 42, 23, 74]
        d = [5, 2, 23, 4, 45, 98]
        self.assertEqual(0, testquestions.equalarr(c, d, 4, 6))

    if __name__ == '__main__':
        unittest.main()

    def test14(self):
        testquestions
        a = [2, 2, 2, 3]
        self.assertEqual(a, testquestions.prime(24))
        b = [2, 2, 5, 13]
        self.assertEqual(b, testquestions.prime(260))

    if __name__ == '__main__':
        unittest.main()

    def test15(self):
        testquestions
        self.assertEqual(1, testquestions.automorphic(76))
        self.assertEqual(0, testquestions.automorphic(147))

    if __name__ == '__main__':
        unittest.main()

    def test16(self):
        testquestions
        self.assertEqual(1, testquestions.alphabetical("abcdef"))
        self.assertEqual(0, testquestions.alphabetical("WCBAFGD"))

    if __name__ == '__main__':
        unittest.main()

    def test17(self):
        testquestions
        a = ['c', 'o', 'd', 'i', 'n', 'g']
        self.assertEqual("[c, o, d, i, n, g]", testquestions.arrtostr(a, 6))
        b = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
        self.assertEqual("[p, r, o, g, r, a, m, m, i, n, g]", testquestions.arrtostr(b, 11))

    if __name__ == '__main__':
        unittest.main()

    def test18(self):
        testquestions
        a = [2, 3, 4, 5, 8, 3, 10]
        self.assertEqual(1, testquestions.specialarr(a, 7))
        b = [2, 4, 5, 1, 9]
        self.assertEqual(0, testquestions.specialarr(b, 5))

    if __name__ == '__main__':
        unittest.main()

    def test19(self):
        testquestions
        self.assertEqual(127, testquestions.series1(6))
        self.assertEqual(511, testquestions.series1(8))

    if __name__ == '__main__':
        unittest.main()

    def test20(self):
        testquestions
        self.assertEqual(1, testquestions.anagram("school master", "the classroom"))
        self.assertEqual(0, testquestions.anagram("toss", "shot"))

    if __name__ == '__main__':
        unittest.main()

    def test21(self):
        testquestions
        self.assertEqual(560.0, testquestions.netbill(450.0), 0.00001)
        self.assertEqual(460.0, testquestions.netbill(350.0), 0.00001)

    if __name__ == '__main__':
        unittest.main()

    def test22(self):
        testquestions
        self.assertEqual(200, testquestions.parcel(320))
        self.assertEqual(280, testquestions.parcel(560))

    if __name__ == '__main__':
        unittest.main()

    def test23(self):
        testquestions
        self.assertEqual("oa", testquestions.vowels("programming", 2))
        self.assertEqual("eai", testquestions.vowels("learning", 3))

    if __name__ == '__main__':
        unittest.main()

    def test24(self):
        testquestions
        self.assertEqual('h', testquestions.maxfreq("hacakthon"))
        self.assertEqual('c', testquestions.maxfreq("cbbbbccc"))

    if __name__ == '__main__':
        unittest.main()

    def test25(self):
        testquestions
        self.assertEqual(8, testquestions.lastindex("0010010010"))
        self.assertEqual(9, testquestions.lastindex("1001000001"))

    if __name__ == '__main__':
        unittest.main()

    def test26(self):
        testquestions
        self.assertEqual("---", testquestions.dashes(3))
        self.assertEqual("-", testquestions.dashes(1))

    if __name__ == '__main__':
        unittest.main()

    def test27(self):
        testquestions
        a = ["ABC", "ACB", "BAC", "BCA", "CBA", "CAB"]
        self.assertEqual(a, testquestions.permutations("ABC"))
        b = ["AABC", "AACB", "ABAC", "ABCA", "ACAB", "ACBA", "BAAC", "BACA", "BCAA", "CAAB", "CABA", "CBAA"]
        self.assertEqual(b, testquestions.permutations("AABC"))

    if __name__ == '__main__':
        unittest.main()

    def test28(self):
        testquestions
        self.assertEqual('l', testquestions.repeat("legolas"))
        self.assertEqual("-", testquestions.repeat("abcdabcd"))

    if __name__ == '__main__':
        unittest.main()

    def test29(self):
        testquestions
        self.assertEqual(3, testquestions.singledigit(147))
        self.assertEqual(9, testquestions.singledigit(2880))

    if __name__ == '__main__':
        unittest.main()

    def test30(self):
        testquestions
        self.assertEqual(1, testquestions.happy(203))
        self.assertEqual(0, testquestions.happy(2880))

    if __name__ == '__main__':
        unittest.main()

    def test31(self):
        testquestions
        self.assertEqual(3702, testquestions.series2(4))
        self.assertEqual(370368, testquestions.series2(6))

    if __name__ == '__main__':
        unittest.main()

    def test32(self):
        testquestions
        a = [1, 2, 4, 6, 3, 7, 8]
        self.assertEqual(5, testquestions.missingnum(a, 8))
        b = [1, 2, 3, 4, 5, 7, 8, 9, 10]
        self.assertEqual(6, testquestions.missingnum(b, 10))

    if __name__ == '__main__':
        unittest.main()

    def test33(self):
        testquestions
        self.assertEqual(1, testquestions.apocalyptic(157))
        self.assertEqual(0, testquestions.apocalyptic(217))

    if __name__ == '__main__':
        unittest.main()

    def test34(self):
        testquestions
        a = [-1, 2, -4, 6, -3, 7, -8]
        self.assertEqual(1, testquestions.alternate(a, 7))
        b = [1, 2, -4, -6, 3, -7, -8]
        self.assertEqual(0, testquestions.alternate(b, 7))

    if __name__ == '__main__':
        unittest.main()

    def test35(self):
        testquestions
        a = [1, 3, 5, 9, 11, 8, 15, 33, 37, 41]
        self.assertEqual(1, testquestions.sorting(a, 10))
        b = [1, 3, 5, 2, 11, 8, 15, 3, 7, 41]
        self.assertEqual(0, testquestions.sorting(b, 10))

    if __name__ == '__main__':
        unittest.main()

    def test36(self):
        testquestions
        self.assertEqual("50lpp48aca", testquestions.encrypt("apple"))
        self.assertEqual("GN36KC32Haca", testquestions.encrypt("HACKING"))

    if __name__ == '__main__':
        unittest.main()

    def test37(self):
        testquestions
        a = [[2, 0], [0, 4]]
        self.assertEqual(1, testquestions.diagonalmatrix(a, 2))
        b = [[3, 1, 0], [1, 2, 4], [2, 5, 6]]
        self.assertEqual(0, testquestions.diagonalmatrix(b, 3))

    if __name__ == '__main__':
        unittest.main()

    def test38(self):
        testquestions
        self.assertEqual(1, testquestions.armstrong(153))
        self.assertEqual(0, testquestions.armstrong(1253))

    if __name__ == '__main__':
        unittest.main()

    def test39(self):
        testquestions
        self.assertEqual(5, testquestions.kempner(5))
        self.assertEqual(3, testquestions.kempner(3))

    if __name__ == '__main__':
        unittest.main()

    def test40(self):
        testquestions
        a = ['e', 't', 's', 't']
        b = [1, 3, 2, 0]
        self.assertEqual("test", testquestions.rearrange(a, b, 4))
        c = ['A', 'O', 'R', 'P', 'R', 'M', 'G']
        d = [5, 2, 4, 0, 1, 6, 3]
        self.assertEqual("PROGRAM", testquestions.rearrange(c, d, 7))

    if __name__ == '__main__':
        unittest.main()

    def test41(self):
        testquestions
        self.assertEqual(1, testquestions.ascending(114455777))
        self.assertEqual(0, testquestions.ascending(1433772))

    if __name__ == '__main__':
        unittest.main()

    def test42(self):
        testquestions
        self.assertEqual(1, testquestions.descending(998887755))
        self.assertEqual(0, testquestions.descending(1433772))

    if __name__ == '__main__':
        unittest.main()

    def test43(self):
        testquestions
        a = ["Delhi", "Bangalore", "Agra", "Mumbai"]
        b = ["Agra", "Bangalore", "Delhi", "Mumbai"]
        self.assertEqual(b, testquestions.alphasort(a, 4))
        c = ["speed", "coding", "can", "be", "solved", "in", "sixty", "minutes"]
        d = ["be", "can", "coding", "in", "minutes", "sixty", "solved", "speed"]
        self.assertEqual(d, testquestions.alphasort(c, 8))

    if __name__ == '__main__':
        unittest.main()

    def test44(self):
        testquestions
        self.assertEqual(4, testquestions.doubleletter("She was feeding the little rabbit with an apple"))
        self.assertEqual(2, testquestions.doubleletter("She broke her knee due to her fast speed"))

    if __name__ == '__main__':
        unittest.main()

    def test45(self):
        testquestions
        self.assertEqual("avehay", testquestions.doubleletter("have"))
        self.assertEqual("odingcay", testquestions.doubleletter("coding"))

    if __name__ == '__main__':
        unittest.main()

    def test46(self):
        testquestions
        self.assertEqual(1, testquestions.semiprime(49))
        self.assertEqual(0, testquestions.semiprime(24))

    if __name__ == '__main__':
        unittest.main()

    def test47(self):
        testquestions
        self.assertEqual(1, testquestions.balanced(5))
        self.assertEqual(0, testquestions.balanced(23))

    if __name__ == '__main__':
        unittest.main()

    def test48(self):
        testquestions
        a = [20, 22, 24, 3, 26, 2, 1]
        self.assertEqual(1, testquestions.even(a, 7))
        b = [21, 23, 27, 3, 29, 2, 1]
        self.assertEqual(0, testquestions.even(b, 7))

    if __name__ == '__main__':
        unittest.main()

    def test49(self):
        testquestions
        a = [[1, 2, 3, 4], [4, 3, 2, 1], [7, 8, 9, 6], [6, 5, 4, 3]]
        self.assertEqual(36, testquestions.diagonals(a, 4))
        b = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        self.assertEqual(30, testquestions.diagonals(b, 3))

    if __name__ == '__main__':
        unittest.main()

    def test50(self):
        testquestions
        self.assertEqual("gnimmargorP ssalC", testquestions.reverse("Programming Class"))
        self.assertEqual("snoitseuq 05 sah gnidoc deepS", testquestions.reverse("Speed coding has 50 questions"))

    if __name__ == '__main__':
        unittest.main()

    def test51(self):
        testquestions
        a = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        self.assertEqual(a, testquestions.triangular(10))
        b = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153]
        self.assertEqual(b, testquestions.triangular(17))

    if __name__ == '__main__':
        unittest.main()
# *******************************************************
