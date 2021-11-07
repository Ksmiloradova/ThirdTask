from transport import *


# ----------------------------------------------
class Airplane(Transport):
    def __init__(self):
        self.flightRange = 0
        self.loadCapacity = 0

    def ReadStrArray(self, strArray, i):
        # должно быть как минимум четыре непрочитанных значения в массиве
        if i >= len(strArray) - 3:
            return 0
        self.speed = int(strArray[i])
        self.distance = float(strArray[i + 1])
        self.flightRange = int(strArray[i + 2])
        self.loadCapacity = int(strArray[i + 3])
        i += 4
        # print("Airplane: a = ", self.a, " b = ", self.b, "c = ", self.c)
        return i

    def Print(self):
        print("Airplane: ideal travel time = ", self.IdealTravelTime(), ", distance = ", self.distance,
              ", speed = ", self.speed, ", flight range = ", self.flightRange, ", load capacity = ", self.loadCapacity)
        pass

    def Write(self, ostream):
        ostream.write("Airplane: ideal travel time = {}, distance = {}, speed = {}, flight range = {}, load capacity "
                      "= {} ".format(self.IdealTravelTime(), self.distance, self.speed,
                                     self.flightRange, self.loadCapacity))
        pass
