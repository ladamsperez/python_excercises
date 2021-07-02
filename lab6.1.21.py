#Create an empty list on line 3 and assign its type on line 4

gift_list= ()

answer_1= ()


print(answer_1)

====

from unittest.gui import TestCaseGui

class myTests(TestCaseGui):
    def testOne(self):
        self.assertEqual(gift_list,[],"gift_list checks")
        self.assertEqual(answer_1,type(gift_list),"answer_1 checks")
myTests().main()