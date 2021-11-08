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
        if (self.flightRange > 40075 or self.flightRange < 100 or self.loadCapacity < 100 or
                self.loadCapacity > 150000 or self.speed < 300 or self.speed > 1194 or self.distance < 0):
            self.speed = -1
        return i

    def ReadRand(self):
        self.speed = random.randint(70, 200)
        self.distance = random.randint(0, 20075)
        self.flightRange = random.randint(100, 40075)
        self.loadCapacity = random.randint(100, 150000)
        pass

    def Print(self):
        print("Airplane: ideal travel time = ", round(self.IdealTravelTime(), 3), "h, distance = ", self.distance,
              "km, speed = ", self.speed, "km/h, flight range = ", self.flightRange, "km, load capacity = ", self.loadCapacity, "kg")
        pass

    def Write(self, ostream):
        ostream.write("Airplane: ideal travel time = {}h, distance = {}km, speed = {}km/h, flight range = {}km, load capacity "
                      "= {}kg".format(round(self.IdealTravelTime(), 3), self.distance, self.speed,
                                     self.flightRange, self.loadCapacity))
        pass
