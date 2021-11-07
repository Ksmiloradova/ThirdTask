from transport import *


# ----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    # def ReadStrArray(self, strArray):

    def BinaryInsertion(self):
        selected = Transport()
        for i in range(1, len(self.store)):
            selected = self.store[i]
            low = 0
            high = i - 1
            while low < high:
                mid = int(low + (high - low) / 2)
                if selected.IdealTravelTime() == self.store[mid].IdealTravelTime():
                    low = mid + 1
                    break
                elif selected.IdealTravelTime() < self.store[mid].IdealTravelTime():
                    low = mid + 1
                else:
                    high = mid
            if high <= low:
                if selected.IdealTravelTime() < self.store[low].IdealTravelTime():
                    low = low + 1
            j = i - 1

            while j >= low:
                self.store[j + 1] = self.store[j]
                j = j - 1
            self.store[j + 1] = selected

    def Print(self):
        print("Container is store", len(self.store), "transports:")
        i = 1
        for shape in self.store:
            print("{}) ".format(i))
            shape.Print()
            i = i + 1
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} transports:\n".format(len(self.store)))
        i = 1
        for shape in self.store:
            ostream.write("{}) ".format(i))
            shape.Write(ostream)
            ostream.write("\n")
            i = i + 1
        pass
