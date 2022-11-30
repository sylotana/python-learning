# Пользовательские функции
# ОПРЕДЕЛЕНИЕ
# Функция - это фрагмент кода, который можно вызвать из любого места программы.
# Функции позволяют уменьшить избыточность кода и повысить его структурированность.

# ОБЪЯВЛЕНИЕ ФУНКЦИИ (СОЗДАНИЕ)
# def <Имя функции>([<Параметры>]):
#     [""" Строка документирования """]
#     <Тело функции>
#     [return <Результат>]

# Если тело функции не выполняет никаких инструкций, то внутри её необходимо разместить
# оператор pass, который не выполняет никаких действий.
def func():
    """ Пустая функция """
    pass


# Необязательная инструкция return позволяет вернуть из функции какое-либо значение
# в качестве результат. После исполнения этой инструкции выполнение функции
# будет остановлено
def func():
    print("Текст до инструкции return")
    return "Возвращаемое значение"


def print_ok():
    """  Пример функции без параметров """
    print("Сообщение при удачно выполненной операции")


def echo(m):
    """ Пример функции с параметром """
    print(m)


def summa(x, y):
    """ Пример функции с параметрами,
    возвращающей сумму двух переменных """
    return x + y


print_ok()
echo("Сообщение")
x = summa(5, 2)  # x = 7
a, b = 10, 50
y = summa(a, b)  # y = 60


# Переменные, указанные в определении функции, являются локальными и доступны ТОЛЬКО
# внутри функции.

# Ссылку на функцию можно сохранить в другую переменной, для этого название функции
# указывается без круглых скобок
def summa(x, y):
    return x + y


f = summa
v = f(10, 20)


# Можно также передать ссылку на функцию другой функции в качестве параметра.
# Функции, передаваемые по ссылке, обычно называются функциями обратного вызова
def summa(x, y):
    return x + y


def func(f, a, b):
    """ Через переменную f будет доступна ссылка на
    функцию summa() """
    return f(a, b)  # Вызываем функцию summa()


# Передаем ссылку на функцию в качестве параметра
v = func(summa, 10, 20)


# Объекты функций поддерживают множество атрибутов, обратиться к которым
# можно, указав атрибут после названия функции через точку. Например, через атрибут
# __name__ можно получить имя функции в виде строки, через атрибут __doc__ - строку
# документирования и т.д.

# Для того чтобы вывести все атрибуты функции используем функцию dir()
def summa(x, y):
    """ Суммирование двух чисел """
    return x + y


print(dir(summa))  # Выведет список (list) всех атрибутов функции

print(summa.__name__)  # >> summa
print(summa.__code__.co_varnames)  # параметры функции
print(summa.__doc__)  # описание функции, указанное в тройных кавычка (""")


# Необязательный параметры и сопоставление по ключам
# Чтобы сделать некоторые параметры функции необязательными, следует в определении
# функции присвоить этому параметру начальное значение
def summa(x, y=2):  # y - необязательный параметр
    return x + y


a = summa(5)  # a = 7
b = summa(10, 50)  # b = 60


# Таким, образом если паараметр не задан, ему будет присвоено значение 2.
# Необязательные параметры ДОЛЖНЫ СЛЕДОВАТЬ ПОСЛЕ ОБЯЗАТЕЛЬНЫХ, иначе будет ошибка

# Python также посволяет передать значения в функцию, используя сопоставление по ключам
def summa(x, y):
    return x + y


print(summa(y=20, x=10))  # Сопоставление по ключам


# Если значения параметров, которые планируется передать в функцию, содержатся
# в кортеже или списке, то перед этим следует указать символ *
def summa(a, b, c):
    return a + b + c


t1, arr = (1, 2, 3), [4, 5, 6]
print(summa(*t1))  # распаковываем кортеж
print(summa(*arr))  # распаковываем список

# Если значения содержатся в словаре, то перед ним следует поставить две звездочки **
d1 = {'a': 7, 'b': 8, 'c': 9}
print(summa(**d1))  # распаковываем словарь


# Объекты в функцию передаются по ссылке. Если объект относится к неизменяемому типу, то
# изменение значения внутри функции не затронет значение переменной вне функции
def func(a, b):
    a, b = 20, 'str'


x, s = 80, 'test'
func(x, s)  # Значения переменных x и s не изменяются
print(x, s)  # x = 80, s = 'test


# ОДНАКО, если объект относится к изменяемому типу, ситуация будет другой
def func(a, b):
    a[0], b['a'] = 'str', 800


x = [1, 2, 3]  # список
y = {'a': 1, 'b': 2}  # словарь

func(x, y)  # Значения будут изменены!!!
print(x, y)  # x = ['str', 2, 3], y = {'a': 800, 'b': 2}


# Переменное число параметров в функции
# Если перед параметром в определении функции указать символ *, то функции можно будет
# передать произвольное количество параметров. Все переданные параметры сохраняются в
# кортеже
def summa(*t):
    """ Функция принимает произвольное количество параметров """
    res = 0
    for i in t:  # Перебираем кортеж с переданными параметрами
        res += i
    return res


print(summa(10, 20))
print(summa(10, 20, 30, 40, 50, 60))


# Можно также вначале указать несколько обязательных параметров и параметров, имеющих
# значения по умолчанию
def summa(x, y=5, *t):  # Комбинация параметров
    res = x + y
    for i in t:
        res += i
    return res


print(summa(10))
print(summa(10, 20, 30, 40, 50, 60))


# Если перед параметром, указать две звездочки **, то все именованные параметры будут сохранены
# в словаре
def func(**d):
    for i in d:  # Перебираем словарь с переданными параметрами
        print('{0} => {1}'.format(i, d[i]), end=' ')


func(a=1, b=2, c=3)


# Если функция не должна принимать переменного количества параметров, но необходимо
# использовать переменные, передаваемые только по именам, то можно указать только
# звездочку без переменной
def func(x=1, y=2, *, a, b=10):
    print(x, y, a, b)


func(35, 10, a=1)
func(10, a=5)
func(a=1, b=2)

# Анонимные функции
# Анонимные функции, также называются лямбда-функциями.
# Анонимная фунция не имеет имени и описывается с помощью ключевого слова
# lambda в следующем формате
# lamda[<Параметр1>[, ..., <ПараметрN>]]: <Возвращаемое значение>

f1 = lambda: 10 + 20  # Функция без параметров
f2 = lambda x, y: x + y  # Фунция с двумя параметрами
f3 = lambda x, y, z: x + y + z  # Функция с тремя параметрами
print(f1())  # >> 30
print(f2(5, 10))  # >> 15
print(f3(5, 10, 30))  # >> 45

# Как и у обычных функций, у лямбда функций некоторые параметры могут быть необязательными
f = lambda x, y=2: x + y
print(f(5))
print(f(5, 6))

# Чаще всего ламбда функцию не сохраняют в переменной, а сразу передают в качестве
# параметра в другую функцию
arr = ['единица1', 'Единый', 'Единица2']
arr.sort(key=lambda s: s.lower())  # отсортируем список без учета регистра
for i in arr:
    print(i, end=' ')
print()


# Функции-генераторы
# Функциями-генераторами называется функция, которая при последовательных вызовах
# возвращает очередной элемент какой-либо последовательности.
# Приостановить выполнение функции и превратить функцию в генератор
# позволяет ключевое слово yield
def func(x, y):
    for i in range(1, x + 1):
        yield i ** y


for n in func(10, 2):
    print(n, end=' ')
print()

for n in func(10, 3):
    print(n, end=' ')
print()


# Функции-генераторы поддерживают метод __next__(),
# который позволяет получить следующее значение.
# Когда значения заканчиваются, метод возбуждает исключение StopIteration
# Вызов метода next() в цикле for производится незаметно для нас.
def func(x, y):
    for i in range(1, x + 1):
        yield i ** y


i = func(3, 3)
print(i.__next__())
print(i.__next__())
print(i.__next__())


# print(i.__next__()) - исключение StopIteration

# С помощью обычных функций мы возвращаем все значения за раз,
# а с помощью функций-генераторов - только одно значение за раз.
# Эта особенность полезна при обработке большого количества значений,
# т. к. не понадобится загружать весь список со значениями в память.

# Существует возможность вызвать одну функцию-генератор из другой.
# Для этого применяется расширенный синтаксис ключевого слова yield:
# yield from <Вызываемая функция-генератор>
def gen(l):
    for e in l:
        yield from range(1, e + 1)


l = [5, 10]
for i in gen([5, 10]): print(i, end=' ')


# Здесь мы в функции-генераторе gen перебираем переданные ей
# в качестве параметра список и для каждого его элемента вызываем
# другую функцию-генератор.

# Декораторы функций
# Декораторы позволяют изменить поведение обычных функций -
# - например, выполнить какие-либо действия перед выполнением функции
def deco(f):  # Функция-декоратор
    print('Вызвана функция func()')
    return f  # Возвращаем ссылку на функцию


@deco
def func(x):
    return 'x = {}'.format(x)


print(func(10))

passw = input('Введите пароль: ')


def test_passw(p):
    def deco(f):
        if p == '10':
            return f
        else:
            return lambda: 'Доступ закрыт'

    return deco


@test_passw(passw)
def func():
    return 'Доступ открыт'


print(func())


# Использование двух декораторов эквивалентно следующему коду
# func = deco1(deco2(func)) сперва выполняется функция deco2 потом deco1

def deco1(f):
    print("Вызвана функция deco1()")
    return f


def deco2(f):
    print("Вызвана функция deco2()")
    return f


@deco1
@deco2
def func(x):
    return "x = {0}".format(x)


print(func(10))


# Рекурсия. Вычисление факториала
# Рекурсия - это возможность функции вызывать саму себя. Рекурсию удобно использовать для
# перебора объекта, имеющего заранее неизвестную структуру, или для выполнения
# неопределенного количества операций.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    x = input("Введите число: ")
    if x.isdigit():  # Если строка содержит только цифры
        x = int(x)  # Преобразуем строку в число
        break  # Выходим из цикла
    else:
        print("Вы ввели не число!")
print('Факториал числа {0} = {1}'.format(x, factorial(x)))

# Количество вызовов фунции самой себя ОГРАНИЧЕНО, узнать количество, можно вызвав
# функцию getrecursionlimit() из модуля sys
import sys

print(sys.getrecursionlimit())  # >> 1000


# При превышении допустимого количества, будет возбуждено исключение
# RuntimeError - в версиях Python, предшествующих 3.5
# RecursionError - в Python 3.5 и выше

# Глобальные и локальные переменные
# Глобальные переменные - это переменные, объявленые в программе вне функции.
# В Python глобальные переменные видны в любой части модуля, включая функции
def func(glob2):
    print('Значение глобальной переменной glob1 =', glob1)
    glob2 += 10
    print('Значение локальной переменной glob2 =', glob2)


glob1, glob2 = 10, 5
func(77)
print('Значение глобальной переменной glob2 =', glob2)


# Все изменения переменной glob2 внутри функции не затронут значение одноименной глобальной переменной

# Локальные переменные - это переменные, объявленные внутри функции. Если имя локальной
# переменной совпадает с именем глобальной переменной, то все операции внутри функции
# осуществляются с локальной переменной, а значение глобальной переменной не изменяется.
# Локальные переменные видны только в теле функции
def func():
    local1 = 77
    glob1 = 25
    print('Значение glob1 внутри функции =', glob1)


glob1 = 10
func()
print('Значение glob1 вне функции =', glob1)
try:
    print(local1)
except NameError:
    print('Переменная local1 не видна вне функции')


# Для того чтобы значение глобальной переменной можно было изменить внутри функции,
# необходимо объявить ее глобальной с помощью ключевого слова global
def func():
    # Объявляем переменную glob1 глобальной
    global glob1
    glob1 = 25
    print('Значение glob1 внутри функции =', glob1)


glob1 = 10
print("Значение glob1 вне функции =", glob1)
func()
print("Значение glob1 после функции =", glob1)


# Вложенные функции
# Одну функцию модно вложить в другую функцию, причем уровень вложенности не ограничен.
# При этом вложенная функция получает свою собственную локальную область видимости
# и имеет доступ к переменным, объявленным внутри функции, в которую она вложена (функции-родителя)
def func1(x):
    def func2():
        print(x)

    return func2


f1 = func1(10)
f2 = func1(99)
f1()
f2()


# Чтобы изменить из вложенной функции значение переменной, объявленной внутри функции-родителя
# следует объявить необходимые переменные с помощью ключевого слова nonlocal
def func1(a):
    x = a

    def func2(b):
        nonlocal x  # Объявляем переменную как nonlocal
        print(x)
        x = b  # Можем изменить значение x в func1()

    return func2


f = func1(10)
f(5)


# При использовании ключевого слова nonlocal следует помнить, что переменная обязательно
# должна существовать внутри функции-родителя.

# Аннотации функций
# В Python функции могут содержать аннотации, который вводят новый способ документирования
# Теперь в заголовке функции допускается указывать предназначение каждого параметра,
# # его тип данных, а также тип возвращаемого функцией значения.
# def <Имя функции>(
#     [<Параметр1>[: <Выражение>] [= <Значение по умолчанию>][, ...,
#     <ПараметрN>[: <Выражение>] [= <Значение по умолчанию>]]]
#     ) -> <Возвращаемое значение>:
#     <Тело функции>
def func(a: 'Параметр1', b: 10 + 5 = 3) -> None:
    print(a, b)


# В этом примере для переменной a создано описание "Параметр1". Для переменной b выражение
# 10 + 5 является описанием, а число 3 - значение параметра по умолчанию. Кроме того, после
# закрывающей круглой скобки указан тип возвращаемого функцие значения: None.
# После создания функции все выражения будут выполнены, и результаты сохранятся в виде словаря
# в атрибуте __annotations__ объекта функции.

def func(a: 'Параметр1', b: 10 + 5 = 3) -> None:
    pass


print(func.__annotations__)  # >> {'a': 'Параметр1', 'b': 15, 'return': None}
