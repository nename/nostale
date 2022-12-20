import mouse as m
import keyboard as kb
from time import sleep


def buff():
  kb.send("E")
  sleep(2)
  kb.send("R")
  sleep(2)

def heal():
  kb.send("T")
  sleep(2)

def attack():
  kb.send("space")
  kb.send("space")

def cast_Q():
  kb.send("q")

def cast_W():
  kb.send("w")

def pick_up():
  kb.send("x")

def sit():
  kb.send("é")

def walk(x, y, offset=[0, 0]):
  x = offset[0] + x
  y = offset[1] + y
  m.move(str(x), str(y))
  m.click()
  m.click()