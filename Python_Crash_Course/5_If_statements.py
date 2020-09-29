print("5 If statements")
print("\n/////////////////////////////////////////////////////////\n")

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# egy állítás vagy igaz vagy hamis és ennek függvényében dönti el a program
# hogy mi lesz

# = hozzárendelés
# == egyenlő e ?

# ki nagy betűre érzékeny
# kisbetűvé kell alakítani  elötte
# ez false lesz
car = 'Audi'
print(car == 'audi')

# így a jó
car = 'Audi'
print(car.lower() == 'audi')

#egyenlőtlenség jele !=
#felkiáltó jel mindig NEMet jelent

requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#számok összehasonlítása ugyan az

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#többféle matematikai összehasonlítás alkalmazható
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#lehet többféle feltételre is szűrni
# and
#mindkettőre igaznak kell lennie
age_0 = 22
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

#egyszerűbb olvasásért lehet őket zárójelbe tenni
print((age_0 >= 21) and (age_1 >= 21))

# or
#ha 1 igaz már igaz
age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21))

# in
#megnézi hogy a lista tartalmazza e

requested_topping = ['mushrooms', 'onions', 'pinapple']
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

# megnézni hogy nincs benne a listába
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ",you can pot a response if you wish.")

#Boolean Expressions
# True vagy False

#If statement

age = 19
if age >= 18:
    print("You are old enough to vote!")

# annyit tehetek be if alá amennyit akarok
#ha igaz lesz akor mindet kiírja

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# else ha False ezt írja ki

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
#ez akkor jó amikor csak 2 kimenet van

#if-elif-else
#ha több lehetőségre vagyunk kíváncsiak
# pl a parkba belépődíj összegek

age = 12
if age < 4:
    print("Your admission cost $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# ha az 4év alatti akkor az elsőt veszi figyelembe
# ha 4évnél idősebb akkor folytatja azaz az elif lesz érvényes
# ha 18évnél idősebb akkor átlépi az elsőt és a másodikat, azaz ha az első kettő
#False akkor az else lesz true

#egyszerűbb ha az if-elif-else csak számokat tartalmaz

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

#bármennyi eli használható

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

#else nem szükséged lehet helyette hasznáni elifet
#viszont akkor mindig egyeznie kell a lehetőségekkel

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# ha a fentebbit használjuk jó else használni mert megtudjuk ha
# elrontottunk valamit
# else egy catchall azaz ami átmegy az if elifen az itt köt ki

#azért használunk csak IFet mert mindegyikre kíváncsiak vagyunk,
# ha lenne elif vagy else akkor az elsőn elakadhat
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print(("Adding extra cheese."))
print("\nFinished making your pizza.")

print("\n.........................................................\n")
##Feladat:
#5-3
alien_color = 'green'
if alien_color == 'green':
    print("Earned 5 points")

alien_color = 'green'
if alien_color == 'red':
    print("Earned 5 points")
#5-4
alien_color = 'red'
if alien_color == 'green':
    point = 5
else:
    point = 10
print("Your earned " + str(point) + " points.")

#5-5
alien_color = 'red'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
elif alien_color == 'red':
    point = 15
else:
    print("Color does not exist!")
print("Your earned " + str(point) + " points.")

#5-6
age = 10

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'
else:
    print("only number")
print("You are a/an " + stage + ".")

print("\n.........................................................\n")
## Using If statements with lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping +".")
print("\nFinished making your pizza.")

##for loopban is lehet IFet használni

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping +".")
print("\nFinished making your pizza.")

#else rákérdezünk arra hogy pl üres e a lista
# IFben is lehet for loop

requested_toppings = []
if requested_topping in requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping +".")
    print("\nFinished making your pizza.")
else:
    print("Are you sure want a plain pizza?")

#Use multiple lists
print("\n")

available_toppings = [ 'mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " +requested_topping + ".")
print("\nFinished making your pizza!")

print("\n.........................................................\n")
## feladat
#5-8
users = ['user1',  'user2', 'user3', 'user4', 'admin']


for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")

print("\n.........................................................\n")

#5-9
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users")

print("\n.........................................................\n")
#5-10

current_users = ['user1',  'user2', 'user3', 'user4', 'user5']
new_users = ['user1',  'user6', 'user7', 'user8', 'user9']

current_users_low = []
for current_user in current_users:
    current_users_low.append(current_user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_low:
        print("Sorry, " + new_user + ", pls new username")
    else:
        print("Well, " + new_user + ",username available.")

print("\n.........................................................\n")
#5-11

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in nums:
    if num == 1:
        print(str(num) + "st\n")
    elif num == 2:
        print(str(num) + "nd\n")
    elif num == 3:
        print(str(num) + "rd\n")
    else:
        print(str(num) + "th\n")



















