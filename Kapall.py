
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import Tkinter
from Tkinter import *
import Tkinter as tk
from Canvas import Rectangle, CanvasText, Group, Window
from Gui import *
import random
import time

class Group(Group):
    def bind(self, sequence=None, command=None):
        return self.canvas.tag_bind(self.id, sequence, command)



 


class Kapall(tk.Tk):

    def __init__(self):
        self.deck=[]
        gildi_spila = []

        

    def newdeck(self):
        self.deck = ['AS', 'KS', 'QS', 'JS', '10S', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',\
                        'AT', 'KT', 'QT', 'JT', '10T', '9T', '8T', '7T', '6T', '5T', '4T', '3T', '2T',\
                        'AL', 'KL', 'QL', 'JL', '10L', '9L', '8L', '7L', '6L', '5L', '4L', '3L', '2L',\
                        'AH', 'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H']
        
    def shuffle(self):
        random.shuffle(self.deck)
        print self.deck

    #Gefa hverju spili gildi fyrir samlagningu
    def gildi(tala):
        gildi_spila = {'HA':1,'H2':2,'H3':3,'H4':4,'H5':5,'H6':6,'H7':7,'H8':8,'H9':9,'HT':10,'HJ':11,'HQ':12,'HK':13,\
            'SA':1,'S2':2,'S3':3,'S4':4,'S5':5,'S6':6,'S7':7,'S8':8,'S9':9,'ST':10,'SJ':11,'SQ':12,'SK':13,\
            'TA':1,'T2':2,'T3':3,'T4':4,'T5':5,'T6':6,'T7':7,'T8':8,'T9':9,'TT':10,'TJ':11,'TQ':12,'TK':13,\
            'LA':1,'L2':2,'L3':3,'L4':4,'L5':5,'L6':6,'L7':7,'L8':8,'L9':9,'LT':10,'LJ':11,'LQ':12,'LK':13}
        
        for i in range(0, len(self)):
            print (x[self[i]])

    def teikna_kapal(self):
        self = Tkinter.Tk()
        C = Tkinter.Canvas(self, bg="forest green", height=650, width=1000)

        C.create_rectangle(50,50,126,146,fill="red")
        rusl = C.create_rectangle(150,50,226,146, fill="red")
        rusl = C.create_rectangle(800,50,876,146, fill="red")

        photo = PhotoImage(file="Deck2.gif")
        image = C.create_image (126,50, anchor =NE, image = photo)
        image1 = C.create_image (550,50, anchor =NE, image = photo)
        image2 = C.create_image (510,110, anchor =NE, image = photo)
        image3 = C.create_image (590,110, anchor =NE, image = photo)
        image4 = C.create_image (470,170, anchor =NE, image = photo)
        image5 = C.create_image (550,170, anchor =NE, image = photo)
        image6 = C.create_image (630,170, anchor =NE, image = photo)
        image7 = C.create_image (430,230, anchor =NE, image = photo)
        image8 = C.create_image (510,230, anchor =NE, image = photo)
        image9 = C.create_image (590,230, anchor =NE, image = photo)
        image10 = C.create_image (670,230, anchor =NE, image = photo)
        image11 = C.create_image (390,290, anchor =NE, image = photo)
        image12 = C.create_image (470,290, anchor =NE, image = photo)
        image13 = C.create_image (550,290, anchor =NE, image = photo)
        image14 = C.create_image (630,290, anchor =NE, image = photo)
        image15 = C.create_image (710,290, anchor =NE, image = photo)
        image16 = C.create_image (350,350, anchor =NE, image = photo)
        image17 = C.create_image (430,350, anchor =NE, image = photo)
        image18 = C.create_image (510,350, anchor =NE, image = photo)
        image19 = C.create_image (590,350, anchor =NE, image = photo)
        image20 = C.create_image (670,350, anchor =NE, image = photo)
        image21 = C.create_image (750,350, anchor =NE, image = photo)
        image22 = C.create_image (310,410, anchor =NE, image = photo)
        image23 = C.create_image (390,410, anchor =NE, image = photo)
        image24 = C.create_image (470,410, anchor =NE, image = photo)
        image25 = C.create_image (550,410, anchor =NE, image = photo)
        image26 = C.create_image (630,410, anchor =NE, image = photo)
        image27 = C.create_image (710,410, anchor =NE, image = photo)
        image15 = C.create_image (790,410, anchor =NE, image = photo)

        

        self.title ("Pyramida kapall")
        

        #Byr til nyjan glugga fyrir hjalp-leidbeiningarnar
        def newwin():
            self=Tkinter.Tk()
            C1 = Tkinter.Canvas(self, bg='dark red', height=500, width=500)
            self.title('Help!')
            C1.create_text(30,30, text='Markmid leiksins er ad henda ollum porum af spilum i ruslbunka ef ad summa spilanna tveggja er 13. Mikilvaegt er ad hafa i huga ad sort spilanna skiptir ekki mali. Thegar ad oll spilin i pyramidanum eru komin i ruslbunkann ta er kapallinn unninn. Haegt er ad fletta i gegnum stokkinn 3-svar sinnum og ef tu ert ekki buin ad losa tig vid oll spilin i pyramidanum adur en tu ert buin ad fletta i gegnum stokkinn 3-svar hefur tu tapad leiknum. I upphafi kapalsins eru 7 nedstu spilin i pyramidanum nothaef asamt teim i bunkanum. Oll spil sem hafa spil ofan a ser eru ekki nothaef tar til tu hefur losad tig vid spilin sem liggja ofan a teim. Tu getur einnig parad saman spilin i stokknum, s.s. tu tarft ekki alltaf ad para saman spilin i stokknum vid spilin i pyramidanum. Haegt er ad faera konginn beint i ruslbunkann tvi ad gildi hans er 13. Ef tu naerd ad setja konung i ruslbunkann faerdu 100 stig en annars fast 200 stig fyrir hvert par sem er faert i ruslbunkann. Ef tu klarar leikinn fyrir 5 minutur faerdu bonusstig upp a 500.                                    GODA SKEMMTUN!', fill='white',anchor=Tkinter.NW, width=430 ,font=('Times new roman',12))
            C1.pack()

        #Lokar glugganum
        def close_window(): 
            self.destroy()

        #Byr til lokataakka
        close_button = Button (C, text='Exit!', command=close_window)
        close_button_window = C.create_window(135, 10,anchor=NE, window=close_button)
        #Byr til hjalptakka
        help_button= Button(C, text="Help!", command=newwin)
        help_button_window = C.create_window(91, 10, anchor=NE, window=help_button)

        C.pack()
        self.mainloop()