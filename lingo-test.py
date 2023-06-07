from lingo import Lingo

# maak een instantie van lingo
mijnLingo = Lingo()

# controleer het woord
print(mijnLingo.validate_input("Lingo"))

# test het juiste woord
uitvoer = mijnLingo.validate_input("Lingo")
if (uitvoer == "gewonnen"):
    print( "Test OK! - Het juiste woord: " + uitvoer)
else:
    print("Test FAILED! - Het juiste woord: " + uitvoer)

# test de juiste lengte
uitvoer = mijnLingo.validate_input("lin")
if (uitvoer == "Voer een woord in van 5 letters!"):
    print( "Test OK! - De juiste lengte: " + uitvoer)
else:
    print("Test FAILED! - De juiste lengte: " + uitvoer)

# test de letters op de juiste plek
uitvoer = mijnLingo.validate_input("lin")
if (uitvoer == "Voer een woord in van 5 letters!"):
    print( "Test OK! - De juiste lengte: " + uitvoer)
else:
    print("Test FAILED! - De juiste lengte: " + uitvoer)

# test de juiste letters op de juiste plek
invoer = "liaaa"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "LI___"):
    print( "Test OK! - De juiste lengte: " + invoer + "> " + uitvoer)
else:
    print("Test FAILED! - De juiste lengte: " + uitvoer)

# test de juiste letters op de verkeerde plek
invoer = "aaali"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "___LI"):
    print( "Test OK! - De juiste lengte: " + invoer + "> " + uitvoer)
else:
    print("Test FAILED! - De juiste lengte: " + uitvoer)

# test de foute letters
invoer = "aaaaa"
uitvoer = mijnLingo.validate_input(invoer)
if (uitvoer == "_____"):
    print( "Test OK! - De juiste lengte: " + invoer + "> " + uitvoer)
else:
    print("Test FAILED! - De juiste lengte: " + uitvoer)