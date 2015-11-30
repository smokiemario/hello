#!/usr/bin/env python3

import skilstak.colors as c
import time as t
import random
def print_merica(message):
    while True:
        buf = ""
        for character in message:
    #for word in message.split():
            color = [
                c.red,
                c.blue,
                c.base3
                ]
           
            buf += c.rc() + random.choice(color) + character
        print(buf, end=" ")
           
def print_strawberry(message):
    while True:
        buf = ""
        for character in message:
            color = [
                c.red,
                c.base03,
                c.g,
                c.r
                ]
            buf += c.rc() + random.choice(color) + character
        print(buf, end=" ")
def print_searchbar(who):
    while True:
        print(c.base3 + """
            ________________________________________________
            |                                               |
            | """ + c.cyan + who + c.base3 + """
            |_______________________________________________|
             """)
            
def print_heart(who):
    while True:
        print(c.m + """
      _____           _____
  ,ad8PPPP88b,     ,d88PPPP8ba,
 d8P"      "Y8b, ,d8P"      "Y8b
dP'           "8a8"           `Yd
8(              "              )8
I8                             8I
 Yb,  """ + c.base3 + who + c.m + """
  "8a,                     ,a8"
    "8a,                 ,a8"
      "Yba             adP"
        `Y8a         a8P'
          `88,     ,88'
            "8b   d8"  
             "8b d8"   
              `888'
                "

""")


def print_ascii(who):
    print(c.rc() + """
    |     |    |---   |      |       |---|  |
    |-----|    |---   |      |       |   |  |
    |     |    |---   |----  |----   |---|  O
    """ + who)

def print_plain(message):
    print(c.cl + c.rc() + message + c.reset)

def print_multi(message):
    while True:
        print(c.cl + c.multi(message))
        t.sleep(0.5)

def print_color(message):
    print(c.cl)
    while True:
        print(c.rc() + message + c.x, end="                            ")
