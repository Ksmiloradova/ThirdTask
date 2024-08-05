# ThirdTask
## Пассажирский транспорт
Третье домашнее задание по предмету "Архитектура вычислительных систем" студента Милорадовой Ксении группы БПИ206

Базовые альтернативы (уникальные параметры, задающие отличительные признаки
альтернатив):
1. Самолеты (дальность полета – целое, грузоподъемность – целое)
2. Поезда (количество вагонов – целое)
3. Корабли (водоизмещение – целое; вид судна – перечислимый тип = (лайнер, буксир, танкер)
   
Общие для всех альтернатив переменные:
1. Скорость – целое
2. Расстояние между пунктами отправления и назначения – действительное
   
Общие для всех альтернатив функции:
- Идеальное время прохождения пути (действительное число)

После размещения данных в контейнер необходимо осуществить их обработку в соответствии
с вариантом задания. Обработанные данные после этого заносятся в отдельный файл
результатов.

Необходимо реализовать следующию функцию:
- Упорядочить элементы контейнера по убыванию используя сортировку методом деления
пополам (Binary Insertion). В качестве ключей для сортировки и других действий используются
результаты функции, общей для всех альтернатив.
***
Для выполнения тестов из заготовленного набора дополнить коммандную строку: <имя входного файла> <имя выходного файла>.
Для генерации случайного транспорта: <количество генеруроеиого транспорта> (выходные данные в данном случае записываются в файл "outputRand<количестсво>.txt"
