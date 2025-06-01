#! /usr/bin/python3.8

import os
import subprocess
import random
import asci_letters
import asci_numbers

#Setting directory with scripts
path = "/home/jan/godzina"
os.chdir(path)



##Below there are test how to invoke variables from other file, simple print did not work had to use getattr. 
#print(asci_letters.a)
#print(getattr(asci_letters, letter))
#
#number  = str(1)
#print(asci_numbers._1)
#print(getattr(asci_numbers, "_" + number))


string = "jancybulski"
audio_path="audio/"

#
wpisz_literke = "audio/wpisz_literke.mp3"
wpisz_ponownie = "audio/wpisz_ponownie.mp3"
bardzo_dobrze = "audio/bardzo_dobrze.mp3"
sprobuj_ponownie = "audio/sprobuj_ponownie.mp3"
zwyciestwo = "audio/zwyciestwo.mp3"
wpisz_cyfre = "audio/wpisz_cyfre.mp3"
jupi = "audio/jupi.mp3"
jupi2 = "audio/jupi2.mp3"
oko_tygrysa = "audio/oko_tygrysa.mp3"
mama="audio/wpisz_slowo_mama.mp3"
tata="audio/wpisz_slowo_tata.mp3"
gdansk="audio/wpisz_miasto_gdańsk.mp3"
w_jakim_miescie_mieszkamy="audio/w_jakim_miescie_mieszkamy.mp3"
mieszkamy_w_miescie_gdansk="audio/mieszkamy_w_miescie_gdansk.mp3"
wykonaj_dzialanie="audio/wykonaj_dzialanie.mp3"
piec_plus_piec="audio/piec_plus_piec.mp3"
cztery_plus_cztery="audio/cztery_plus_cztery.mp3"
trzy_plus_trzy="audio/trzy_plus_trzy.mp3"
dwa_plus_dwa="audio/dwa_plus_dwa.mp3"
jeden_plus_jeden="audio/jeden_plus_jeden.mp3"
wynik_to="audio/wynik_to.mp3"
wpisz_slowo="audio/wpisz_slowo.mp3"




def clear():
    os.system("clear")

# Function playing sound and displaying image
def imageSound(name):

    os.system("kitty +kitten icat " + "images/" + name + ".png")
    os.system("mpg123 -q " + wpisz_slowo)
    os.system("mpg123 -q " + "audio/" + name + ".mp3" + "&")
    input_slowo=input("Wpisz slowo: ")
    if input_slowo == name:
       print("Very good")
       os.system("mpg123 -q " + bardzo_dobrze)
       clear()
    else:           
       print("Try again")
       os.system("mpg123 -q " + sprobuj_ponownie) 
       imageSound(name)     







#Play intro an eye of the tiger
#os.system("source /etc/bash.bashrc")
os.system("kitty +kitten icat images/tygrys.jpg")
os.system("mpg123 -q " + oko_tygrysa)
clear()

#imageSound("jancybulski")

#for letter in string:
#    #Command type in letter
#    os.system("mpg123 -q " + wpisz_literke)
#    #print(getattr(asci_letters, letter))
#
#
#
#    file_path = audio_path+letter+".mp3"
#    os.system("mpg123 -q " + file_path )
#                        
#    while True:         
#        input_letter=input("Wpisz literkę: ")
#        if input_letter == letter:
#            print("Bardzo dobrze")
#            os.system("mpg123 -q " + bardzo_dobrze)
#            break       
#        else:           
#            print("Spróbuj ponownie")
#            os.system("mpg123 -q " + sprobuj_ponownie) 
#            os.system("mpg123 -q " + wpisz_literke)
#            os.system("mpg123 -q " + file_path )
#            #print(getattr(asci_letters, letter))
#
#print("\n")             
                        
                        
#for numb in range(1,5): 
#    os.system("mpg123 -q " + wpisz_cyfre)
#    number = str(random.randint(0,10))
#    #print(getattr(asci_numbers, "_" + number))         
#    file_path = audio_path+number+".mp3"
#    os.system("mpg123 -q " + file_path )
#
#    while True:
#        input_number=input("Wpisz cyferkę: ")
#        if input_number == number:
#            print("Bardzo dobrze")
#            os.system("mpg123 -q " + bardzo_dobrze)
#            clear()
#            break
#        else:
#            print("Spróbuj ponownie")
#            os.system("mpg123 -q " + sprobuj_ponownie)
#            os.system("mpg123 -q " + wpisz_cyfre)
#            os.system("mpg123 -q " + file_path )
#            #print(getattr(asci_numbers, "_" + number))
#
#
#
#while True:
#    slowo = "mama"
#    print("Teraz będziemy wpisywać słowa")
#    os.system("mpg123 -q " + mama)
#    input_slowo=input("Wpisz słowo: ")
#    if input_slowo == slowo:
#        print("Bardzo dobrze")
#        os.system("mpg123 -q " + bardzo_dobrze)
#        clear()
#        break       
#    else:           
#        print("Spróbuj ponownie")
#        os.system("mpg123 -q " + sprobuj_ponownie) 
#        os.system("mpg123 -q " + mama)
#
#
#
#while True:
#    slowo = "tata"
#    print("Teraz będziemy wpisywać słowa")
#    os.system("mpg123 -q " + tata)
#    input_slowo=input("Wpisz słowo: ")
#    if input_slowo == slowo:
#        print("Bardzo dobrze")
#        os.system("mpg123 -q " + bardzo_dobrze)
#        clear()
#        break       
#    else:           
#        print("Spróbuj ponownie")
#        os.system("mpg123 -q " + sprobuj_ponownie) 
#
#
#
#
#while True:
#    slowo = "gdansk"
#    print("Teraz będziemy wpisywać słowa")
#    os.system("mpg123 -q " + w_jakim_miescie_mieszkamy)
#    os.system("mpg123 -q " + mieszkamy_w_miescie_gdansk)
#    os.system("mpg123 -q " + gdansk)
#    input_slowo=input("Wpisz miasto \"Gdańsk\": ")
#    if input_slowo == slowo:
#        print("Bardzo dobrze")
#        os.system("mpg123 -q " + bardzo_dobrze)
#        clear()
#        break       
#    else:           
#        print("Spróbuj ponownie")
#        os.system("mpg123 -q " + sprobuj_ponownie) 
#
#
#def addition(number1, number2, result):
#    while True:
#        result = int(result)
#        result_path=str(result)
#        print("Wykonaj działanie")
#        os.system("mpg123 -q " + wykonaj_dzialanie + "&")
#        #os.system("mpg123 -q " + jeden_plus_jeden)
#        input_result=(input( '{} {} {} {}'.format(number1, "+", number2, "= ") ))
#        try:
#            input_result = int(input_result)
#        except:
#            print("Wprowadz cyfrę")
#
#        if input_result == result:
#            print("Bardzo dobrze")
#            os.system("mpg123 -q " + bardzo_dobrze)
#            file_path = audio_path+result_path+".mp3"
#            clear()
#            #os.system("mpg123 -q " + wynik_to)
#            #os.system("mpg123 -q " + file_path)
#            break       
#        else:           
#            print("Spróbuj ponownie")
#            os.system("mpg123 -q " + sprobuj_ponownie) 
#
##addition(1, 1, 2)
##addition(2, 2, 4)
##addition(3, 3, 6)
#addition(4, 4, 8)
#addition(5, 5, 10)
#addition(2, 1, 3)
#addition(3, 2, 5)
#addition(4, 3, 7)
#addition(5, 3, 8)
#addition(5, 4, 9)
#addition(6, 6, 12)
#addition(7, 7, 14)
#addition(8, 8, 16)
#addition(9, 9, 18)
#addition(10,10,20)
#
#
#
#
#
#
#
#def substraction(number1, number2, result):
#    while True:
#        result = int(result)
#        result_path=str(result)
#        print("Wykonaj działanie")
#        os.system("mpg123 -q " + wykonaj_dzialanie + "&")
#        #os.system("mpg123 -q " + jeden_plus_jeden)
#        input_result=(input( '{} {} {} {}'.format(number1, "-", number2, "= ") ))
#        try:
#            input_result = int(input_result)
#        except:
#            print("Wprowadz cyfrę")
#
#        if input_result == result:
#            print("Bardzo dobrze")
#            os.system("mpg123 -q " + bardzo_dobrze)
#            file_path = audio_path+result_path+".mp3"
#            clear()
#            #os.system("mpg123 -q " + wynik_to)
#            #os.system("mpg123 -q " + file_path)
#            break       
#        else:           
#            print("Spróbuj ponownie")
#            os.system("mpg123 -q " + sprobuj_ponownie) 
#
#substraction(3, 1, 2)
#substraction(4, 2, 2)
#substraction(5, 2, 3)
#substraction(6, 3, 3)
#substraction(7, 2, 5)
#substraction(8, 4, 4)
#substraction(9, 4, 5)
#substraction(10, 5, 5)
#
#substraction(12, 2, 10)
#substraction(14, 4, 10)
#substraction(16, 6, 10)
#substraction(18, 8, 10)
#substraction(20, 5, 15)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
##while True:
##    wynik = int(4)
##    wynik_path=str(wynik)
##    print("Teraz będziemy dodawać")
##    os.system("mpg123 -q " + wykonaj_dzialanie)
##    os.system("mpg123 -q " + dwa_plus_dwa)
##    input_wyni1Gk=int(input("2 + 2 = "))
##    if input_wynik == wynik:
##        print("Bardzo dobrze")
##        os.system("mpg123 -q " + bardzo_dobrze)
##        file_path = audio_path+wynik_path+".mp3"
##        #os.system("mpg123 -q " + wynik_to)
##        #os.system("mpg123 -q " + file_path)
##        break       
##    else:           
##        print("Spróbuj ponownie")
##        os.system("mpg123 -q " + sprobuj_ponownie) 
##
##
#
#
#
#
#Wywołanie funkcji
#imageSound("kot")
#imageSound("kupa")
#imageSound("noga")
#imageSound("dom")
#imageSound("papa")
#imageSound("pupa")
#imageSound("tatami")
#imageSound("ul")
#imageSound("tygrysek")
#imageSound("krowa")
#
#def imageNumber(name, number, picture):
#    os.system("kitty +kitten icat " + "images/" + name + ".png")
#    print(picture.upper())
#    input_number=input(":")
#    try:
#      input_number = int(input_number)
#    except:
#      print("Wprowadz cyfrę")
#
#    if input_number == number:
#       print("Bardzo dobrze")
#       os.system("mpg123 -q " + bardzo_dobrze)
#       clear()
#    else:
#        print("Spróbuj ponownie")
#        os.system("mpg123 -q " + sprobuj_ponownie) 
#        imageNumber(name, number, picture)
#
#imageNumber("lale", 3, "lale")
#imageNumber("lale", 1, "kot")
#imageNumber("lale", 5, "druty")
#imageNumber("lale", 6, "dom")
#imageNumber("lale", 2, "medal")


#imageNumber("auto", 3, "kura")
#imageNumber("auto", 1, "kaktus")
#imageNumber("auto", 5, "auto")
#imageNumber("auto", 6, "Artur")
#imageNumber("auto", 4, "lusterko")
#imageNumber("auto", 2, "skuter")



############### NEW #############################
#
#imageNumber("bohater", 76, "chomik")
#imageNumber("bohater", 54, "homar")
#imageNumber("bohater", 32, "harmonia")
#imageNumber("bohater", 21, "bohater")
#imageNumber("bohater", 43, "kawa")
#imageNumber("bohater", 65, "huśtawka")
#
#imageNumber("ciele", 21, "cielak")
#imageNumber("ciele", 54, "skrbonka")
#imageNumber("ciele", 65, "bucik")
#imageNumber("ciele", 76, "cukierki")
#imageNumber("ciele", 43, "klocki")
#imageNumber("ciele", 32, "cyrk")
#
#imageNumber("gepard", 65, "globus")
#imageNumber("gepard", 43, "karetka")
#imageNumber("gepard", 21, "gepard")
#imageNumber("gepard", 32, "gitara")
#imageNumber("gepard", 54, "czajnik")
#imageNumber("gepard", 76, "wigwam")
#
#imageNumber("jablko", 54, "ojciec")
#imageNumber("jablko", 76, "uczennica")
#imageNumber("jablko", 32, "jabłoń")
#imageNumber("jablko", 65, "jamnik")
#imageNumber("jablko", 43, "skrzynia")
#imageNumber("jablko", 21, "jabłko")
#
#imageNumber("kaktus", 32, "skuter")
#imageNumber("kaktus", 43, "kura")
#imageNumber("kaktus", 76, "wrona")
#imageNumber("kaktus", 54, "lusterko")
#imageNumber("kaktus", 21, "kaktus")
#imageNumber("kaktus", 65, "auto")
#
#imageNumber("kret", 65, "motor")
#imageNumber("kret", 32, "sikorka")
#imageNumber("kret", 21, "kret")
#imageNumber("kret", 76, "tratwa")
#imageNumber("kret", 43, "babeczka")
#imageNumber("kret", 54, "rakieta")
#
#imageNumber("lasica", 43, "słońce")
#imageNumber("lasica", 76, "piłka")
#imageNumber("lasica", 54, "buziak")
#imageNumber("lasica", 65, "kaczka")
#imageNumber("lasica", 32, "ławka")
#imageNumber("lasica", 21, "łasica")
#
#imageNumber("lekarka", 32, "drzewo")
#imageNumber("lekarka", 54, "malarz")
#imageNumber("lekarka", 76, "skrzat")
#imageNumber("lekarka", 65, "kałamarz")
#imageNumber("lekarka", 21, "lekarka")
#imageNumber("lekarka", 43, "krzesło")
#
#imageNumber("lesniczy", 76, "ołówek")
#imageNumber("lesniczy", 21, "leśniczy")
#imageNumber("lesniczy", 43, "jaskółka")
#imageNumber("lesniczy", 32, "góra")
#imageNumber("lesniczy", 54, "ogórek")
#imageNumber("lesniczy", 65, "pióro")
#
#imageNumber("lyzwy", 43, "żółw")
#imageNumber("lyzwy", 54, "żmija")
#imageNumber("lyzwy", 76, "jeżyny")
#imageNumber("lyzwy", 65, "żaba")
#imageNumber("lyzwy", 32, "żagówka")
#imageNumber("lyzwy", 21, "łyżwy")
#
#imageNumber("motyl", 32, "kwiatek")
#imageNumber("motyl", 54, "kamień")
#imageNumber("motyl", 65, "motyka")
#imageNumber("motyl", 76, "lody")
#imageNumber("motyl", 21, "motyl")
#imageNumber("motyl", 43, "rower")
#
#imageNumber("pasta", 54, "bukiet")
#imageNumber("pasta", 43, "rekin")
#imageNumber("pasta", 32, "wąż")
#imageNumber("pasta", 65, "biurko")
#imageNumber("pasta", 76, "robak")
#imageNumber("pasta", 21, "tubka")
#
#imageNumber("pies", 32, "ptak")
#imageNumber("pies", 21, "pies")
#imageNumber("pies", 76, "sopel")
#imageNumber("pies", 65, "wodospad")
#imageNumber("pies", 54, "prosiak")
#imageNumber("pies", 43, "papryka")
#
#imageNumber("statek", 43, "most")
#imageNumber("statek", 54, "deska")
#imageNumber("statek", 65, "lisek")
#imageNumber("statek", 32, "smok")
#imageNumber("statek", 76, "satelita")
#imageNumber("statek", 21, "statek")
#
#imageNumber("trabka", 43, "wielbłąd")
#imageNumber("trabka", 65, "gęś")
#imageNumber("trabka", 32, "groszek")
#imageNumber("trabka", 76, "owca")
#imageNumber("trabka", 21, "trąbka")
#imageNumber("trabka", 54, "ząb")
#
#imageNumber("wazon", 54, "czarodziej")
#imageNumber("wazon", 76, "obraz")
#imageNumber("wazon", 21, "wazon")
#imageNumber("wazon", 32, "zupa")
#imageNumber("wazon", 43, "prezenty")
#imageNumber("wazon", 65, "arbuz")
#
#imageNumber("zakretka", 65, "pętelka")
#imageNumber("zakretka", 32, "wędka")
#imageNumber("zakretka", 21, "zakrętka")
#imageNumber("zakretka", 43, "książka")
#imageNumber("zakretka", 76, "rękawice")
#imageNumber("zakretka", 54, "kurczę")
#


############## NEW ##############################

############## English #########################
#def imageNumberSound(name, number, picture):
#    os.system("kitty +kitten icat " + "images/" + name + ".png")
#    os.system("mpg123 -q " + "audio/" + picture + ".mp3" + "&")
#    print(picture.upper())
#    input_number=input(":")
#    try:
#      input_number = int(input_number)
#    except:
#        print("Enter number:")
#
#    if input_number == number:
#       print("Very good")
#       os.system("mpg123 -q " + bardzo_dobrze)
#       clear()
#    else:
#        print("Try again")
#        os.system("mpg123 -q " + sprobuj_ponownie) 
#        imageNumberSound(name, number, picture)
#
#
#
#
#
#imageNumberSound("lesson1", 10, "milk")
#imageNumberSound("lesson1", 3, "cheese")
#imageNumberSound("lesson1", 2, "carrots")
#imageNumberSound("lesson1", 4, "eggs")
#imageNumberSound("lesson1", 11, "peas")
#imageNumberSound("lesson1", 8, "ham")
#imageNumberSound("lesson1", 14, "potatoes")
#imageNumberSound("lesson1", 5, "sausages")
#imageNumberSound("lesson1", 13, "vegetables")
#imageNumberSound("lesson1", 6, "fish")
#imageNumberSound("lesson1", 9, "meat")
#imageNumberSound("lesson1", 7, "fruits")
#imageNumberSound("lesson1", 12, "plants")
#imageNumberSound("lesson1", 1, "animals")
#
#imageNumberSound("lesson1", 3, "cheese")
#imageNumberSound("lesson1", 2, "carrots")
#imageNumberSound("lesson1", 14, "potatoes")
#imageNumberSound("lesson1", 5, "sausages")
#imageNumberSound("lesson1", 13, "vegetables")
#imageNumberSound("lesson1", 6, "fish")
#imageNumberSound("lesson1", 9, "meat")
#imageNumberSound("lesson1", 7, "fruits")
#imageNumberSound("lesson1", 12, "plants")
#imageNumberSound("lesson1", 1, "animals")
#imageNumberSound("lesson1", 4, "eggs")
#imageNumberSound("lesson1", 8, "ham")
#imageNumberSound("lesson1", 10, "milk")
#
#imageNumberSound("lesson1", 3, "cheese")
#imageNumberSound("lesson1", 11, "peas")
#imageNumberSound("lesson1", 8, "ham")
#imageNumberSound("lesson1", 5, "sausages")
#imageNumberSound("lesson1", 6, "fish")
#imageNumberSound("lesson1", 9, "meat")
#imageNumberSound("lesson1", 7, "fruits")
#imageNumberSound("lesson1", 12, "plants")
#imageNumberSound("lesson1", 1, "animals")
#imageNumberSound("lesson1", 10, "milk")
#imageNumberSound("lesson1", 2, "carrots")
#imageNumberSound("lesson1", 14, "potatoes")
#imageNumberSound("lesson1", 13, "vegetables")
#
#

########### English End ########################


############## English #########################
def imageNumberImage(name, number, picture):
    os.system("kitty +kitten icat " + "images/" + name + ".png")
    #os.system("kitty +kitten icat " + "images/" + picture + ".s.png")
    #os.system("mpg123 -q " + "audio/" + picture + ".mp3" + "&")
    #print(picture.upper())
    input_number=input(":")
    try:
      input_number = (input_number)
    except:
        print("Enter number:")

    if input_number == number:
       print("Very good")
       os.system("mpg123 -q " + bardzo_dobrze)
       clear()
    else:
        print("Try again")
        os.system("mpg123 -q " + sprobuj_ponownie) 
        imageNumberImage(name, number, picture)





imageNumberImage("1:00","1:00" , "1:00")
imageNumberImage("1:15", "1:15", "1:15")
imageNumberImage("2:30", "2:30", "2:30")
imageNumberImage("3:00", "3:00","3:00")
imageNumberImage("6:00", "6:00","6:00")
imageNumberImage("7:00", "7:00","7:00")
imageNumberImage("9:00", "9:00","9:00")
imageNumberImage("11:00", "11:00","11:00")
imageNumberImage("12:00", "12:00","12:00")

imageNumberImage("1:15", "1:15","1:15")
imageNumberImage("4:20", "4:20","4:20")
imageNumberImage("6:40", "6:40","6:40")
imageNumberImage("8:56", "8:56","8:56")
imageNumberImage("11:45", "11:45","11:45")
imageNumberImage("12:08", "12:08","12:08")
imageNumberImage("12:22", "12:22","12:22")
imageNumberImage("12:34", "12:34","12:34")
imageNumberImage("12:36", "12:36","12:36")


#imageNumberImage("zebrane", 8, "taboret")
#imageNumberImage("zebrane", 2, "beret")
#imageNumberImage("zebrane", 3, "firana")
#imageNumberImage("zebrane", 5, "lampa")
#imageNumberImage("zebrane", 1, "zegar")
#imageNumberImage("zebrane", 4, "kanapa")
#imageNumberImage("zebrane", 6, "rower")
#imageNumberImage("zebrane", 9, "rakieta")
#imageNumberImage("zebrane", 7, "samolot")
#
#
#
##Wywołanie funkcji
#imageSound("taboret")
#imageSound("beret")
#imageSound("firana")
#imageSound("lampa")
#imageSound("zegar")
#imageSound("kanapa")
#imageSound("rower")
#imageSound("rakieta")
#imageSound("samolot")
#
#
#imageSound("taboret")
#imageSound("beret")
#imageSound("firana")
#imageSound("lampa")
#imageSound("zegar")
#imageSound("kanapa")
#imageSound("rower")
#imageSound("rakieta")
#imageSound("samolot")
#
#
#imageSound("taboret")
#imageSound("beret")
#imageSound("firana")
#imageSound("lampa")
#imageSound("zegar")
#imageSound("kanapa")
#imageSound("rower")
#imageSound("rakieta")
#imageSound("samolot")

############## Polish End #########################


#imageNumber("zwierzeta", 2, "pies")
#imageNumber("zwierzeta", 6, "świnia")
#imageNumber("zwierzeta", 10, "żółw")
#imageNumber("zwierzeta", 15, "łopata")
#imageNumber("zwierzeta", 1, "kot")
#imageNumber("zwierzeta", 11, "królik")
#imageNumber("zwierzeta", 4, "łoś")
#imageNumber("zwierzeta", 5, "krowa")
#imageNumber("zwierzeta", 7, "koń")
#imageNumber("zwierzeta", 8, "niedzwiedź")
#imageNumber("zwierzeta", 12, "wąż")
#imageNumber("zwierzeta", 3, "zając")
#imageNumber("zwierzeta", 9, "wiewiórka")
#imageNumber("zwierzeta", 13, "statek")
#imageNumber("zwierzeta", 14, "kwiatek")
#
#
#
#def colourNumber(name, number, picture):
#    os.system("kitty +kitten icat " + "images/" + name + ".png")
#    print(picture.upper())
#    input_number=input(":")
#    try:
#      input_number = int(input_number)
#    except:
#      print("Wprowadz cyfrę")
#
#
#    if input_number == number:
#        print("Bardzo dobrze")
#        os.system("mpg123 -q " + bardzo_dobrze)
#        clear()
#    else:
#        print("Spróbuj ponownie")
#        os.system("mpg123 -q " + sprobuj_ponownie) 
#        imageNumber(name, number, picture)
#
#
#colourNumber("RGB", 2, "niebieski")
#colourNumber("RGB", 6, "biały")
#colourNumber("RGB", 3, "zielony")
#colourNumber("RGB", 4, "żółty")
#colourNumber("RGB", 1, "czerwony")
#colourNumber("RGB", 5, "różowy")
#
#
#def readNumbers(word, number):
#    print("Jaka to liczba " + word )
#    input_number=input(":")
#    try:
#      input_number = int(input_number)
#    except:
#      print("Wprowadz cyfrę")
#
#
#    if input_number == number:
#        print("Bardzo dobrze")
#        os.system("mpg123 -q " + bardzo_dobrze)
#        clear()
#    else:
#        print("Spróbuj ponownie")
#        os.system("mpg123 -q " + sprobuj_ponownie) 
#        readNumbers(word, number)
#
#readNumbers("jeden", 1)
#readNumbers("trzy", 3)
#readNumbers("pięć", 5)
#readNumbers("dwa", 2)
#readNumbers("dziewięć", 9)
#readNumbers("siedem", 7)
#readNumbers("dziesięć", 10)
#readNumbers("osiem", 8)
#readNumbers("sześć", 6)
#readNumbers("cztery", 4)
#
#
#
#
#




os.system("touch /dev/shm/minetest")


wybor = int(input("""
    1 -> MINETEST
    2 -> YOUTUBE
    3 -> HBOGO, BAJKI
    4 -> MINECRAFT
    """))

if wybor == 1:
    print("Zwyciestwo uruchamiam minecraft")
    os.system("mpg123 -q " + zwyciestwo)

    print("Komunikat od Janka :)")
    os.system("mpg123 -q " + jupi)

    print("Komunikat od Taty :)")
    os.system("mpg123 -q " + jupi2)


    from subprocess import call
    minetest = call("/home/jan/minetest.sh", shell=True)

if wybor == 2:
    from subprocess import call
    minetest = call("firefox", shell=True)


if wybor == 3:
    from subprocess import call
    minetest = call("/opt/google/chrome/chrome", shell=True)

if wybor == 4:
    from subprocess import call
    minetest = call("/usr/bin/minecraft-launcher", shell=True)


