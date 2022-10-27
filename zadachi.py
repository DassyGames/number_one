
list_func = ['1 - Ведро Яблок', "2 - Создание чайника(чашек и тарелок)", "3 - Температура воды", "4 - Температура массы", "5 - Сколько дней вы прожили", "6 - Сопративление", "7 - Трапеция", "8 - Плата за электричество", "9 - Наследство", "10 - Радуис",  "11 - Ребро паралелепипеда", "12 - Длина куба"]


#_______________________________1
def stud():
    student_1 = int(input("\nПервый ученик: "))
    student_2 = int(input("Второй ученик: "))
    student_3 = int(input("Третий ученик: "))

    time = int(input("Время: "))

    Func_1 = student_1 + student_2 + student_3 * time 

    print(f"Они собрали {Func_1} вёдер")

#_______________________________2
def raww():
    kettle = int(input('\nСколько Чайников: '))
    raw_1 = int(input('Сколько граммов: '))

    plate = int(input('Сколько Тарелок: '))
    raw_2 = int(input('Сколько граммов: '))

    cup = int(input('Сколько Чашек: '))
    raw_3 = int(input('Сколько граммов: '))

    Func_2 = kettle + plate + cup
    Func_3 = raw_1 + raw_2 + raw_3

    Func_4 = int(Func_3 / Func_2)

    print(f"Нужно {Func_4} кг Сырья!")

#_______________________________
def vessel_temp():
    vessel_1 = int(input("\nСколько литров воды в первом сосуде: "))
    temperat_1 = int(input("Температура: "))

    vessel_2 = int(input("Сколько литров воды в втором сосуде: "))
    temperat_2 = int(input("Температура: "))

    vessel_3 = int(input("Сколько литров воды в третьем сосуде: "))
    temperat_3 = int(input("Температура: "))

    Func_5 = vessel_1 + vessel_2 + vessel_3
    Func_6 = (temperat_1 + temperat_2 + temperat_3) / 3

    print(f'\n{Func_5} литров воды! \nТемпература воды {Func_6}')

#______________________________
def mass_kg():
    massa = int(input("\nВведите массу: "))

    tmp = int(input("Введите температуру массы: "))

    tmp_max = int(input("Температура нагревания: "))

    Func_7 = tmp_max - tmp
    print(f'Нужно {Func_7} температуры по цельсию!')

#______________________________
def years():
    year = int(input("\nВведите год вашего рождения: "))
    Func_8 = 2022 - year
    Func_9 = Func_8 * 365
    print(f"Вам {Func_9} дней!")

#______________________________
def R():
    r1 = float(input("\nВведите сопративление R1: "))
    r2 = float(input("Введите сопративление R2: "))
    r3 = float(input("Введите сопративление R3: "))

    Func_10 = 1/(1/r1 + 1/r2 + 1/r3)
    print(Func_10)

#______________________________
def trap():
    a = float(input("\nВведите основание а: "))

    b = float(input("Введите основание b: "))

    h = float(input("Введите чему равна высота: "))

    square = ((a+b)/2)*h

    print("Площадь трапеции равна:",square)
    
#______________________________
def money_eng():
    KBt = int(input("\nВведите сколько хотите заплатить за электричество(КВт): "))
    KBt_plat = int(input("Сколько вы раньше платили за электричество(КВт): "))
    KBt_Func = KBt * KBt_plat
    print(f"Вы заплатили: {KBt_Func}")

#_______________________________
def nasledstvo():
    nasled = int(input("\nРазмер наследства которую вы бы хотели(в Долларах): "))
    trat = int(input("Сколько вы будете тратить в месяц(в долларах): "))
    Func_11 = nasled / trat / 365
    print(f"Вам хватит наследства на {int(Func_11)} года")

#_______________________________
def radius():
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    c = int(input("Введите C: "))

    S = int(input("Введите площадь: "))
    P = int(input("Введите полуметр треугольника: "))

    RB = S/P
    print("Радиус RB", RB)

    RO = a * b * c / 4 * S
    print("Радиус RO", RO)

#_______________________________
def rebro():
    a = int(input("Введите длину A: "))
    b = int(input("Введите длину B: "))    
    c = int(input("Введите длину C: "))

    h = int(input("Введите высоту H: "))

    V = a * b * h
    print(f'Объём паралелепипеда: {V} см')

    S = 2 * (a*b+b*c+a*c)
    print(f'Площадь поверхности: {S} см')

#_______________________________
def dlinarebra():
    a = int(input("Введите ребро Куба А: "))
    print(f'Объем куба {a **3} см')
    print(f'Поверхность куба {a * 6} см')

#________________________________
def katet():
    a = int(input("Введите катет Куба А: "))
    b = int(input("Введите катет Куба B: "))

    cg = a * 2 + b * 2
    s = a + b * 6
    p = 2 * (a + b)

    print(f'Гипотенуза {cg}\nПлощадь {s}\nПериметр {p}')


while True:
    print("\nВсе функции!")
    print(" ")
    for l in list_func:
        print(l)
    choice = int(input("\nВыберите действие(по номеру): "))
    if choice == 1:
        stud()
    elif choice == 2:
        raww()
    elif choice == 3:
        vessel_temp()
    elif choice == 4:
        mass_kg()
    elif choice == 5:
        years()
    elif choice == 6:
        R()
    elif choice == 7:
        trap()
    elif choice == 8:
        money_eng()
    elif choice == 9:
        nasledstvo()
    elif choice == 10:
        radius()
    elif choice == 11:
        rebro()
    elif choice == 12:
        dlinarebra()
    elif choice == 13:
        katet()
    else:
        print('Введите нужную цифру!')
        continue
