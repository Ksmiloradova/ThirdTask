import sys
import string
import time

from extender import *

# ----------------------------------------------
if __name__ == '__main__':
    startTime = time.perf_counter()
    transpNum = -1
    if len(sys.argv) == 3:
        inputFileName = "tests/" + sys.argv[1]
        outputFileName = "results/" + sys.argv[2]
    elif len(sys.argv) == 2:
        transpNum = int(sys.argv[1])
        if transpNum < 0:
            sys.exit()
        outputFileName = "results/outputRandom{}.txt".format(transpNum)
    elif len(sys.argv) == 1:
        print("Incorrect command line! You must write: python main <inputFileName> [<outputFileName>]")
        exit()
    if transpNum < 0:
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()

        # print(str)
        # print("len(str) = ", len(str))

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.replace("\n", " ").split(" ")
        # print(strArray)
        # print("len(strArray) = ", len(strArray))
        # figNum = ReadArray(strArray)

    print('==> Start')

    container = Container()
    if transpNum < 0:
        transpNum = ReadStrArray(container, strArray)
    else:
        transpNum = ReadRand(container, transpNum)
    container.BinaryInsertion()
    container.Print()

    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    time = time.perf_counter()-startTime
    ofile.write("Time: {}s".format(time))
    ofile.close()

    print('==> Finish')
    print("Time: {}s".format(time))
