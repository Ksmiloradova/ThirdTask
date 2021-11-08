from transport import *


# ----------------------------------------------
class Train(Transport):
    def __init__(self):
        self.numberOfWagons = 0

    def ReadStrArray(self, strArray, i):
        # должно быть как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 2:
            return 0
        self.speed = int(strArray[i])
        self.distance = float(strArray[i + 1])
        self.numberOfWagons = int(strArray[2])
        i += 3
        # print("Train: x = ", self.x, " y = ", self.y)
        if 0 > self.numberOfWagons > 75 or self.speed < 70 or self.speed > 200 or self.distance < 0:
            self.speed = -1
        return i

    def ReadRand(self):
        self.speed = random.randint(70, 200)
        self.distance = random.randint(0, 20075)
        self.numberOfWagons = random.randint(0, 75)
        pass

    def Print(self):
        print("Train: ideal travel time = ", round(self.IdealTravelTime(), 3), "h, distance = ", self.distance,
              "km/h, speed = ", self.speed, ", number of wagons = ", self.numberOfWagons)
        pass

    def Write(self, ostream):
        ostream.write("Train: ideal travel time = {}h, distance = {}km, speed = {}km/h, number of wagons = {}"
                      .format(round(self.IdealTravelTime(), 3), self.distance, self.speed, self.numberOfWagons))
        pass
