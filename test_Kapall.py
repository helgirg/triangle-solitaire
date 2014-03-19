import unittest
from Kapall import *


class test(unittest.TestCase):  

    def test_newdeckandshuffle(self):#athugar hvort ad listinn er stokkadur med tvi ad bera saman vid ostokkadan lista. Testar newdeck fallid i klasanum Deck og shuffle fallid i klasanum Deck
        lst = Kapall() # Byr til nyjan ostokkadan lista
        lst.newdeck
        lstshuffled = Kapall() #Byr til nyjan lista og stokkar hann
        lstshuffled.newdeck
        self.assertNotEqual(lstshuffled.shuffle(), lst)
        #Skilar OK ef ad stokkadi listinn og ostokkadi listinn eru olikir

if __name__== '__main__':
    unittest.main(verbosity=3, exit=False)

