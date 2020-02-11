f = open("reservations")

for x in f:
    name, number = x.split(",")
    #print(f"Navn: {name} Reservasjoner: {number}")
    #print(f"Tall: {int(number)}")
    try:
        chairs_per_person = round(50 / int(number))
        if chairs_per_person > 50:
            chairs_per_person = 50
        print("{} will get {} chairs per person".format(name, chairs_per_person))
    except ValueError as error:
        print(f"Feil: Tall kan ikke skrives med bokstaver!! Todd!!")
    except ZeroDivisionError as error:
        print(f"Feil: Kan ikke reservere 0 stoler")
    except:
        print(f("Feil: WTF Todd!?"))
