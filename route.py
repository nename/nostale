import cv2 as cv
import pyautogui
import numpy as np


class Route:
  def __init__(self):
    self.route = []
    self.map = []
    self.image = 0
    self.h = 0
    self.w = 0
    self.im_map = 0
    self.offset = []

  def __select_map(self, event, x, y, *args):
    if event == cv.EVENT_LBUTTONDOWN:
      self.map.append([x, y])
      cv.circle(self.im_map, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
      pass

  @staticmethod
  def get_min(arr):
    min_x = 9999; min_y = 9999
    for x, y in arr:
      if x < min_x:
        min_x = x
      if y < min_y:
        min_y = y

    return min_x, min_y

  @staticmethod
  def get_max(arr):
    max_x = 0; max_y = 0
    for x, y in arr:
      if x > max_x:
        max_x = x
      if y > max_y:
        max_y = y

    return max_x, max_y

  def __get_screenshot(self):
    sc = pyautogui.screenshot()
    self.im_map = cv.cvtColor(np.array(sc), cv.COLOR_RGB2BGR)

    cv.namedWindow("select map")
    cv.moveWindow("select map", 80, 80)
    cv.setMouseCallback("select map", self.__select_map)

    while 1:
      cv.imshow("select map", self.im_map)
      k = cv.waitKey(1) & 0xFF

      if k == ord("d"):
        break
    
    cv.destroyWindow("select map")

    max_x, max_y = self.get_max(self.map)
    min_x, min_y = self.get_min(self.map)

    self.h = max_y - min_y
    self.w = max_x - min_x

    image = self.im_map[min_y:max_y, min_x:max_x]

    self.image = cv.resize(image, (400, 400), interpolation=cv.INTER_LINEAR)

  def __select_route(self):
    while 1:
      cv.imshow("map", self.image)

      k = cv.waitKey(1) & 0xFF

      if k == ord("d"):
        break

  def __draw_line(self):
    x1, y1 = self.route[-2]
    x2, y2 = self.route[-1]
    cv.line(self.image, [int(x1 * (400 / self.w)), int(y1 * (400 / self.h))], [int(x2 * 2.55), int(y2 * 2.55)], (0, 0, 255), 1)

  def __draw_point(self, event, x, y, *args):
    if event == cv.EVENT_LBUTTONDOWN:
      self.route.append([int(x / (400 / self.w)), int(y / (400 / self.h))])
      cv.circle(self.image, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
      pass

    if len(self.route) > 1:
        self.__draw_line()

  def get_route(self):
    global offset_g

    self.__get_screenshot()

    cv.namedWindow("map")
    cv.moveWindow("map", 80, 80)
    cv.setMouseCallback("map", self.__draw_point)

    self.__select_route()

    cv.destroyAllWindows()

    self.offset = self.map[0]

    return self.route

if __name__ == "__main__":
  route = Route()
  points = route.get_route()
  print(points)