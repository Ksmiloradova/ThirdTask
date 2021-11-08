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
        shipType = int(strArray[i + 2])
        if shipType > 3 or shipType < 1:
            shipType = shipType % 3
            if (shipType == 0):
                shipType = 3
        self.t = Type(shipType)
        self.displacement = int(strArray[i + 3])
        i += 4
        # print("Ship: a = ", self.a, " b = ", self.b, "c = ", self.c)
        if (self.displacement < 20 or self.displacement > 554000000 or
                self.speed < 5 or self.speed > 120 or self.distance < 0):
            self.speed = -1
        return i

    def ReadRand(self):
        self.speed = random.randint(70, 200)
        self.distance = random.randint(0, 20075)
        self.t = Type(random.randint(1, 3))
        self.displacement = random.randint(20, 554000000)
        pass

    def Print(self):
        print("Ship: ideal travel time = ", round(self.IdealTravelTime(), 3), "h, distance = ", self.distance,
              "km, speed = ", self.speed, "kg, displacement = ", self.displacement, ", type = ", self.t)
        pass

    def Write(self, ostream):
        ostream.write("Ship: ideal travel time = {}h, distance = {}km, speed = {}km/h, displacement = {}kg, type "
                      "= {} ".format(round(self.IdealTravelTime(), 3), self.distance, self.speed,
                                     self.displacement, self.t))
        pass
