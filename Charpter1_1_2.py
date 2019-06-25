# Created by Yi Xie 6/21/2019
# Examples on Python Cookbook
# This is a piece of code that show the ability of python to split a iterable data structure store into variables

p = (4, 5, 6)  # A Tuple
four, five, six = p

print("four: " + str(four))
print("five: " + str(five))
print("six: " + str(six))

print("-----------------------------")

# It will work if the data structure is iterable
data = ['RTX2080', '14000MHz', ['8GB', '256bit'], '$800']
name, freq, RAM, price = data
print("Name: " + name)
print("freq: " + freq)
print("RAM: ", RAM)
Capacity, bits = RAM
print("Capacity: ", Capacity)
print("Bits: ", bits)
print("price: " + price)

print("-----------------------------")
# This operation equals to the previous one
data = ['RTX2070', '14000MHz', ['8GB', '256bit'], '$800']
name, freq, (Capacity, Bits), price = data
print("Name: " + name)
print("freq: " + freq)
print("Capacity: ", Capacity)
print("Bits: ", Bits)
print("price: " + price)

print("-----------------------------")
# String is also iterable
str_1 = 'HelloWorld!'
a, b, c, d, e, f, g, h, i, j, k = str_1
print("a: ", a)
print("k: ", k)

print("-----------------------------")
# For the case we want to split a iterable structure which the item inside exceed the number of target variables
DaVinci = ["Leonardo", "di", "ser", "Piero", "da", "Vinci"]
First, *Middle, Last = DaVinci
print(First, Middle, Last)

print("-----------------------------")
# * can place at the first variable to get all the data except the last one
Years_Since_I_Born = [2000, 2001, 2002, 2003, 2004, 2005, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,2013, 2014,
                      2015, 2016, 2017, 2018, 2019]
*past_years, cur_year = Years_Since_I_Born
print(past_years, cur_year)

print("-----------------------------")


def dog(x, y):
    print("dog:", x, y)


def duck(t):
    print("duck", t)


record = [('dog', 1, 2), ('duck', 1), ('duck',2), ('dog', 3, 4)]
for tag, *arg in record:
    if tag == "dog":
        dog(*arg)
    else:
        duck(*arg)

