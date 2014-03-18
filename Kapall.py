#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import Tkinter
from Tkinter import *
from Canvas import Rectangle, CanvasText, Group, Window
import random

self = Tkinter.Tk()
self.geometry('1000x650')
self.title("Triangle solitaire")
self.configure(background='Forest green')
self.mainloop()

class Kapall():

    def __init__(self):
        self.deck=[]
        

    def newdeck(self):
        self.deck = ['AS', 'KS', 'QS', 'JS', '10S', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',\
                        'AT', 'KT', 'QT', 'JT', '10T', '9T', '8T', '7T', '6T', '5T', '4T', '3T', '2T',\
                        'AL', 'KL', 'QL', 'JL', '10L', '9L', '8L', '7L', '6L', '5L', '4L', '3L', '2L',\
                        'AH', 'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H']
    def shuffle(self):
        random.shuffle(self.deck)
        print self.deck
