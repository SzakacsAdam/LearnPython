print("3 Introducing lists")

print("\n/////////////////////////////////////////////////////////\n")

#lista mindig négyzetes zárójel

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

#lista első eleme 0
print(bicycles[1])
print(bicycles[3])

#ha - a szám akkor hátulról számol
print(bicycles[-1])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

print("\n.........................................................\n")
##feladat
#3-1
names = ['isti', 'vili', 'vári', 'dorka', 'ági', 'évi', 'alexa']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())
print(names[6].title())
#3-2
message = "Szia " + names[6].title() + "."
print(message)

for name in names:
    message = "Szia " + name.title() + "."
    print(message)
print("\n.........................................................\n")

#changing adding, remove

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0]= 'ducatti'
print(motorcycles)
#elem hozzáadás .append a lista végére teszi

motorcycles.append('ducatti')
print(motorcycles)

# .append -al egyszerű hozzáadn, akár üres listához is

gyümölcs = []

gyümölcs.append('alma')
gyümölcs.append('körte')
gyümölcs.append('szilva')
gyümölcs.append('ananász')
print((gyümölcs))

#elem behelyezés
# .insert zárójlben a helye majd vessző és a szöveg ami bekerül
motorcycles =['honda', 'yamaha', 'suzuki']

motorcycles.insert(0,'ducati')
print(motorcycles)

#elem törlése listából
# del + lista neve zárójelben a hely

#elsőhely törlése
motorcycles =['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

#második hely törlése
motorcycles =['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

#ha del -el törlök akkor az végleges törlés és nemtudo visszaszerezni

# .pop törlés, de utána még tudom használni az értéket
# az utolsó értéket törli, ha üres a zárójel

motorcycles =['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
#popped_motorcycles megmutatja hogy melyik esett ki

motorcycles =['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()

print("The last motorcycle I owned was a " + last_owned.title() +".")

#ha a .pop zárójelébe számot írok akkor azaz index fog kiesni
motorcycles =['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() +".")

#néha nemm tudok a helyzetét csak az értéket, így is tudsz törölni
#.remove értéket töröl

motorcycles =['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#
motorcycles =['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#a .remove csak az első találatot törli, ha több is lehet akkor loop kell

## feladat
# 3-4
names = ['isti', 'vili', 'vári', 'dorka', 'ági', 'évi', 'alexa']
message ="Please " + names[2].title() + " come to my party."
print(message)

print("\n.........................................................\n")
#lista rendezése

# .sort végleges abc sorrend, nem visszafordítható
cars =['bmw', 'subaru', 'toyota', 'audi']
cars.sort()
print(cars)

#fordított abc .sort(reverse=True)
cars =['bmw', 'subaru', 'toyota', 'audi']
cars.sort(reverse=True)
print(cars)

#ideinglenes abc sorrend sorted()
cars =['bmw', 'subaru', 'toyota', 'audi']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#fordított  sorrend, nem abc, csak fordított
#.reverse()
cars =['bmw', 'subaru', 'toyota', 'audi']
print(cars)

cars.reverse()
print(cars)

#a lista hosszához a len() kell
cars =['bmw', 'subaru', 'toyota', 'audi']
print(len(cars))

#feladat
#3-8
places = ['paris', 'amsterdam', 'tokyo', 'brussel', 'pécs']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)








