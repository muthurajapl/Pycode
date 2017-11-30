people = 30
cats = 30
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!")
elif people == cats:
    print ("people = cats")
elif people <= cats:
    print ("people <= cats")
else:
    print ("Not many cats! The world is saved!")

if people < dogs:
    print ("The world is drooled on!")
else:
    print ("The world is dry!")


dogs += 5

if people >= dogs:
    print ("People are greater than or equal to dogs.")

if people <= dogs:
    print ("People are less than or equal to dogs.")


if people == dogs:
    print ("People are dogs.")
    
if 10 != 20:
    print ("Not equal")