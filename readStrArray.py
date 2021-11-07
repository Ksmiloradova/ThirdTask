from extender import *

def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0   # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)   # преобразование в целое 
        #print("key = ", key)
        if key == 2: # признак самолета
            i += 1
            transp = Train()
            i = transp.ReadStrArray(strArray, i) # чтение самолета с возвратом позиции за ним
        elif key == 1: # признак поезда
            i += 1
            transp = Airplane()
            i = transp.ReadStrArray(strArray, i) # чтение поезда с возвратом позиции за ним
        elif key == 3:  # признак корабля
            i += 1
            transp = Ship()
            i = transp.ReadStrArray(strArray, i)  # чтение корабля с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанного транспорта
            return figNum
        if i == 0:
            return figNum
        # Количество транспорта увеличивается на 1
        figNum += 1
        container.store.append(transp)
    return figNum
