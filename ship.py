from transport import *
from enum import Enum


# ----------------------------------------------
class Type(Enum):
    LINER = 1
    TUG = 2
    TANKER = 3


class Ship(Transport):

    def __init__(self):
        self.displacement = 0
        self.t = Type(1)

    def ReadStrArray(self, strArray, i):
        # должно быть как минимум четыре непрочитанных значения в массиве
        if i >= len(strArray) - 3:
            return 0
        self.speed = int(strArray[i])
        self.distance = float(strArray[i + 1])
        shipType = int(strArray[i + 3])
        if shipType > 3 or shipType < 1:
            shipType = shipType % 3
            if (shipType == 0):
                shipType = 3
        self.t = Type(shipType)
        self.displacement = int(strArray[i + 2])
        i += 4
        # print("Ship: a = ", self.a, " b = ", self.b, "c = ", self.c)
        return i

    def Print(self):
        print("Ship: ideal travel time = ", self.IdealTravelTime(), ", distance = ", self.distance,
              ", speed = ", self.speed, ", displacement = ", self.displacement, ", type = ", self.t)
        pass

    def Write(self, ostream):
        ostream.write("Ship: ideal travel time = {}, distance = {}, speed = {}, displacement = {}, type "
                      "= {} ".format(self.IdealTravelTime(), self.distance, self.speed,
                                     self.displacement, self.t))
        pass
