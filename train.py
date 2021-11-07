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
        return i

    def Print(self):
        print("Train: ideal travel time = ", self.IdealTravelTime(), ", distance = ", self.distance,
              ", speed = ", self.speed, ", number of wagons = ", self.numberOfWagons)
        pass

    def Write(self, ostream):
        ostream.write("Train: ideal travel time = {}, distance = {}, speed = {}, number of wagons = {}"
                      .format(self.IdealTravelTime(), self.distance, self.speed, self.numberOfWagons))
        pass
