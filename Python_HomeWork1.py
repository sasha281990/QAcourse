# Создать переменную типа String
a = '5'
print(type(a), a)
# Создать переменную типа Integer
b = 5
print(type(b), b)
# Создать переменную типа Float
c = 1.2
print(type(c), c)
# Создать переменную типа Bytes
d = b'255, 255, 0'
print(type(d), d)
# Создать переменную типа List
e = [2, 1, 5]
print(type(e), e)
# Создать переменную типа Tuple
f = ("apple", "banana", "cherry")
print(type(f), f)
# Создать переме нную типа Set
g = {"apple", "banana", "cherry"}
print(type(g), g)
# Создать переменную типа Frozen set
h = frozenset({"apple", "banana", "cherry"})
print(type(h), h)
# Создать переменную типа Dict
i = {"name": "John", "age": 36}
print(type(i), i)
# Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print((type(a), a), (type(b), b), (type(c), c), (type(d), d), (type(e), e), (type(f), f), (type(g), g),
      (type(h), h), (type(i), i))
# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
x = 'King'
y = 'Lion'
con = x + y
print(con)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
q = 5
print(x, q, sep=',')
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(x, q, sep='+')
