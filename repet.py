#This script is used to learn the French months and numbers (0-100). The script generates a random digit, the user has to enter the corresponding month/number.
#The script compares the input of the user to the list.
#This is repeated until the user enters "exit".
#Results are recorded in the repet_error.csv file.
#v3 Added a third option "mots" where word from a csv file called "repet_voc" are used. List needs the form German;French
#v4 defined functions for testing numerical words or using a dictionary file in the same location as the python file
#v5 removed all internal lists only works with external vocabulary.csv now. Changing "german, french" to "french, german" will learn in the other direction

import random, time, os

def testing(groupGER, groupFRA, name): # this function takes two groups - one German one French and compares them, the third variable is name describing that vocabulary. For integers group one is always "integers"
    print("Tu apprends les " + name + "! Tape \"exit\" pour exit.")
    count = 0
    errors = 0
    while True:
        count = count + 1
        test = random.randint(1, (len(groupFRA)-1))
        print("Qu'est »" + str(groupGER[test]) + "« en français?")
        check = input()
        if check == str(groupFRA[test]): # compare input to index
            print("C'est le mot correct!\n")
        elif check == "exit": #exit option
            break
        else:
            while True: # gives correct solution until it is repeted correctly
                errors = errors + 1
                print("Ce n'est pas correct! \nCe mot correct est: " + str(groupFRA[test]) + "\n Répèt!")
                check2 = input()
                if check2 == str(groupFRA[test]):
                    print("Oui, c'est correct!\n")
                    break
    print("Formidable! Tu as appris " + str(int(count)-1) + " " + name + " et tu faites juste " + str(errors) + " fautes.")
    if os.path.exists(".\\repet_error.csv") == False: #creates result file if non existant
        listFile = open(".\\repet_error.csv", "w")
        listFile.write("mots;fautes;date;thème\n")
        listFile.close()

    listFile2 = open(".\\repet_error.csv", "a") #saves results
    x = str(count) + ";" + str(errors) + ";" + str(time.strftime("%d.%m.%Y") + ";" + name)
    listFile2.write(x+"\n")
    listFile2.close()
    time.sleep(8)

def importing(filename): #this function takes a file of the given name, located in the same folder as the script and splits its two columns into two groups called "german" and "french"
    #loads the vocabulary file
    vocFile = open(".\\" + filename + ".csv")
    vocText = vocFile.read()
    vocFile.close()
   #teilt den Text von vocText (split) in einzelne Zeilen (lines()) und löscht die erste Zeile(Titel) sowie die letzte Zeile falls sie leer ist
    lines = vocText.split("\n")
    if lines[-1]== "":
        del lines[-1]
    #jede Zeile wird entlang des ";" aufgeteilt und der Wert der Liste german und french zugeschrieben
    a = 0
    for x in range(len(lines)):
        x = lines[a]
        z = x.split(";")
        ger = z[0]
        fre = z[1]
        german.append(ger)
        french.append(fre)
        a = a + 1 

#set up list of German and French words
german = []
french = []

#records what to learn
print("Apprends-tu les mois, les nombres, la semaine, les coleurs ou les interrogatifs? Tape: MOIS, NOMBRES, SEMAINE, COULEURS ou INTERROGATIF")
choice = input()

#learning months
if choice == "MOIS":
    importing("repet_months")
    testing(german, french, "mois")

#learning numbers
if choice == "NOMBRES":
    importing("repet_numbers")
    testing(german, french, "nombres")

#learning weekdays
if choice == "SEMAINE":
    importing("repet_week")
    testing(german, french, "jours de semaine")

#learning interrogatives from vocabulary file
if choice == "INTERROGATIF":
    importing("repet_question")
    testing(german, french, "interrogatif")

#learning colours from vocabulary file
if choice == "COULEURS":
    importing("repet_colour")
    testing(german, french, "couleurs")
    
else:
    print("Au revoir!")
    time.sleep(5)
