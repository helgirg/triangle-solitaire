
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import Tkinter
from Tkinter import *
from Canvas import Rectangle, CanvasText, Group, Window
import random


# self = Tkinter.Tk()
# C = Tkinter.Canvas(self, bg="forest green", height=650, width=1000)

# self.title ("Pyramida kapall")
# C.pack()
# self.mainloop()

z = [] # global fylki 
        
class Kapall():

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
        gildi_spila = {'AS':1, 'KS':13, 'QS':12, 'JS':11, '10S':10, '9S':9, '8S':8, '7S':7, '6S':6, '5S':5, '4S':4, '3S':3, '2S':2,\
        'AT':1, 'KT':13, 'QT':12, 'JT':11, '10T':10, '9T':9, '8T':8, '7T':7, '6T':6, '5T':5, '4T':4, '3T':3, '2T':2,\
        'AL':1, 'KL':13, 'QL':12, 'JL':11, '10L':10, '9L':9, '8L':8, '7L':7, '6L':6, '5L':5, '4L':4, '3L':3, '2L':2,\
        'AH':1, 'KH':13, 'QH':12, 'JH':11, '10H':10, '9H':9, '8H':8, '7H':7, '6H':6, '5H':5, '4H':4, '3H':3, '2H':2}
    
    def teikna_kapal(self):
        self = Tkinter.Tk()
        C = Tkinter.Canvas(self, bg="forest green", height=650, width=1000)
        C.create_rectangle(50,50,126,146,fill="red")
        filename = PhotoImage(file="Deck2.gif")
        image = C.create_image (126,50, anchor =NE, image = filename)
        self.title ("Pyramida kapall")
        C.pack()
        self.mainloop()


    # def myndir_spil(self):
    #     self.img = Image.open(Deck2.gif)
    #     self.Deck2 = Image Tk.PhotoImage(self.img)


