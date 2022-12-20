from time import sleep
from random import randint as rn
import datetime as dt

from movement import *
from route import *
from healthBar import *
  

def auto_bot():
  # select route
  r = Route()
  points = r.get_route()
  offset = r.offset
  del r

  bar = HealtBar()

  # select health and mana
  bar.get_health_bar()

  # wait to activate window
  sleep(3)

  print("start")
  while True:
    for x, y in points:
      # walk
      walk(x, y, offset)
      
      sleep(3)

      attack()
      
      sleep(10)

      for _ in range(4):
        pick_up()
        sleep(1)

      if not bar.check_health_and_mana():
        sit()
        sleep(30)

def auto_attack():

  bar = HealtBar()
  # select health and mana
  bar.get_health_bar()

  # wait to activate window
  sleep(3)

  # buff()
  # buff_s = dt.datetime.now()

  heal()
  heal_s = dt.datetime.now()

  print("start")
  while True:
    # image reset
    sc = pyautogui.screenshot()
    bar.image = cv.cvtColor(np.array(sc), cv.COLOR_RGB2BGR)

    # regen
    if bar.check_health_low() or bar.check_mana_low():
      print("regen")
      while (not bar.check_health_full()) or (not bar.check_mana_full()):
        if bar.sitting():
          sit()
        sleep(10)

        sc = pyautogui.screenshot()
        bar.image = cv.cvtColor(np.array(sc), cv.COLOR_RGB2BGR)
      walk(bar.middle[0], bar.middle[1])

    # buff timer
    # if dt.datetime.now() >= (buff_s + dt.timedelta(minutes=4)):
    #   buff()
    #   buff_s = dt.datetime.now()

    # heal timer
    if dt.datetime.now() >= (heal_s + dt.timedelta(minutes=1.5)):
      heal()
      heal_s = dt.datetime.now()

    # movementq
    attack()

    sleep(1)

    cast_Q()

    sleep(1)

    cast_W()

    sleep(1)

    pick_up()
    pick_up()

    sleep(1)

    attack()

    sleep(1)

if __name__ == "__main__":
  auto_attack()
