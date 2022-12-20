import cv2 as cv
import pyautogui
import numpy as np

class HealtBar:
  bars = []
  health = []
  mana = []
  middle = []
  hat = []
  image = 0

  def select_health_bar(self, event, x, y, *args):
    if event == cv.EVENT_LBUTTONDOWN:
      self.bars.append([x, y])
    elif event == cv.EVENT_LBUTTONUP:
      pass

  def get_health_bar(self):
    print("1. click low hp\n2. click max hp\n3. click low mana\
          \n4. click full mana\n5. click near pos\n6. click top head")
    sc = pyautogui.screenshot()
    self.image = cv.cvtColor(np.array(sc), cv.COLOR_RGB2BGR)

    cv.namedWindow("select health bar")
    cv.setMouseCallback("select health bar", self.select_health_bar)

    while 1:
      cv.imshow("select health bar", self.image)
      k = cv.waitKey(1) & 0xFF

      if k == ord("d"):
        break
    
    self.health = [self.bars[0], self.bars[1]]
    self.mana = [self.bars[2], self.bars[3]]
    self.middle = self.bars[4]
    self.hat = self.bars[5]
    self.b, self.g, self.r = self.image[self.bars[5][1], self.bars[5][0]]
    cv.destroyWindow("select health bar")

  def check_health_low(self):
    cm = np.array([9, 9, 9])
    
    # check health
    if ((np.array(self.image[self.health[0][1], self.health[0][0]]) != cm).all()):
      return False 

    return True

  def check_health_full(self):
    cm = np.array([9, 9, 9])
    
    # check health
    if ((np.array(self.image[self.health[1][1], self.health[1][0]]) == cm).all()):
      return False 

    return True

  def check_mana_low(self):
    cm = np.array([9, 9, 9])

    if ((np.array(self.image[self.mana[0][1], self.mana[0][0]]) != cm).all()):
      return False

    return True
    
  def check_mana_full(self):
    cm = np.array([9, 9, 9])

    if ((np.array(self.image[self.mana[1][1], self.mana[1][0]]) == cm).all()):
      return False

    return True

  def sitting(self):
    b, g, r = self.image[self.hat[1], self.hat[0]]

    #return (b > 40 and b < 60 and g > 150 and g < 190 and r > 170 and r < 220)
    return (b > self.b - 25 and b < self.b + 25 
          and g > self.g - 25 and g < self.g + 25 
          and r > self.r - 25 and r < self.r + 25)