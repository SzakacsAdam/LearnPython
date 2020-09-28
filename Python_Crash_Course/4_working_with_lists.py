print("4 Working with lists")
print("\n/////////////////////////////////////////////////////////\n")

# loop használata egy teljes listán keresztül
# for loop  végigmegy a listán egyesével

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

print("\n.........................................................\n")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() +".\n")
print("Thank you, everyone. That was a great magic show!")

#ha nincs tab akkor indentation error
# ha a második print nincs tabozva akkor csak az utolsót fogja megkapni
# ha tabozok de nem kell akkor unexpected indent
# ha pl a 3 print is tabozott akkor minden alaklommla végig megy rajta
# ha for ciklunál lehgayom a : akkor syntax error mert nem kezdődik ela  loop


print("\n.........................................................\n")
#feladat
#4-1
fav_pizzas = ['margherita', 'bacon', 'cheese']
for fav_pizza in fav_pizzas:
    print(fav_pizza)
    print("I like " + fav_pizza + " pizza.")
print("I really love pizza!")

print("\n.........................................................\n")
# range() számsor
for value in range(1,5):
    print(value)
#5 ig számol, azaz az 5 nincs benne
# ha számsort akarunk listába helyezni akkor list()
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)
#a harmadig szám a range() ben az interval

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#egyszerű stastizstika
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print("\n.........................................................\n")
#feldat
#4-3

for num in range(1,21):
    print(num)
#4-4
#mil1 = [list(range(1,1000001))]
#print(mil1)

#4-5
mil1 = []

for value in range(1,1000001):
    mil2 = value + 1
    mil1.append(mil2)
print(sum(mil1))

#4-6
for odd in range(1,21,2):
    print(odd)

#4-7

multi3 = []

for multi in range(1,11):
    multi2 = multi * 3
    multi3.append(multi2)
print(multi3)

#4-8
cubes = []
for cub in range(1,11):
    cub1 = cub **3
    cubes.append(cub1)
for cube in cubes:
    print(cube)
#4-9
cubes2 = [value**3 for value in range(1,11)]
print(cubes2)

print("\n.........................................................\n")
#Working with part of a list
#a lista bizonyos része slice

players =['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#a listát nem változtatja csak azt a szeletet mutatja meg
#ugyanúgy 0ról kezdődik a számolás és 1el korábban megáll
print(players[1:4])
#ha az egyik értéket kihagyom akkor vagy előről kezdi vagy avégéig csinálja
print(players[:4])
print(players[2:])

#hátulról a 3.számtól a végéig mutatja
print(players[-3:])

#looping from slice
players =['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#copying list

#ha az egész listát akarom másolni akkor [:] azt így
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)
print("\nMyfriends1 favourite foods are:")
print(friend_foods)

#hogy biztosra menjünk hogy 2 külön lista ez hozzáadunk elemeket
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)
print("\nMyfriends1 favourite foods are:")
print(friend_foods)

# ha simán másoltam volna friend_foods = my_foods akkor ugyan az a 2 halmaz és nem 2 különbőző
# a 2 halmaz egyemlő lesz bármelyikhez adok bármit

print("\n.........................................................\n")
#feladat:

#4-10
players =['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print(("Three first names in the list are:"))
for player in players[:3]:
    print(player.title())
print(("Three names from the middle in the list are:"))
for player in players[1:4]:
    print(player.title())
print(("The last three names in the list are:"))
for player in players[-3:]:
    print(player.title())

#4-10
fav_pizzas = ['margherita', 'bacon', 'cheese']
friend_pizzas = fav_pizzas[:]
fav_pizzas.append('plain')
friend_pizzas.append('onion')

print("My favorite pizzas are:")
for fav in fav_pizzas[:]:
    print(fav)
print("My friend's favorite pizzas are:")
for friend in friend_pizzas[:]:
    print(friend)

print("\n.........................................................\n")
## Tuples
# egy olyan lista ami fix és nem lehet módosítani
#ott használjuk ahol tuti fix a szám
#nem négyzetes hanem sima zárójele van

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# for loop ugyan az mint list
for dimension in dimensions:
    print(dimension)

#nem módosítható, de új értéket kaphat
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 10)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print("\n.........................................................\n")
#Feladat:
#4-13
restaurant_foods = ('eggs', 'donuts', 'cakes', 'fried stuff', 'potatoes')
for restaurant_food in restaurant_foods:
    print(restaurant_food)
#restaurant_foods[0] = ('keksz')
restaurant_foods = ('bread', 'donuts', 'cheese cake', 'fried stuff', 'potatoes')
print(restaurant_foods)



