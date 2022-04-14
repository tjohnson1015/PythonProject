
numbers = []

captain = "desmond"

print('''
_   ___ ___ ____   ____ ___  _  _ _  _   __ 
))  )) )))_  ))     ))  ))_) )) ))`) )) /_`)
((__((_( _(( ((     ((  ((`\ (( ((,' (( (( ( 

Welcome Hurley.

Unfortunately, you'e crash landed on "The Island". In order to get back home, you need to collect a series of 6 numbers.
Clues to these numbers can be found in the stations listed below.''')

def start_game():
    while True:
        input_1 = input("""
What station would you like to search?

Press 1 to visit "The Hydra"
Press 2 to visit "The Swan"
Press 3 to visit "The Flame"
Press 4 to visit "The Pearl"
Press 5 to visit "The Orchid"
Press 6 to visit "The Looking Glass"
Press 7 to visit "The Arrow"
Press 8 to see your list so far
Press 9 to leave The Island
Press 10 to exit the game
"""
        )

        if input_1 == "1":
                user_input = input('''Uh oh, The Hydra station is not on this island. To get a lift, you need to call for someone who knows his way around a boat. Any ideas? 
''')
                if user_input.lower() == "desmond":
                    print("\nHello mate, I'll take you across the pond!")
                    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
                    user_input_2 = int(input('''Welcome to The Hydra!
In order to get the number from this station you will need to answer a question.
What strange animal was discovered on this island?
1. Penguin
2. Dinosaur
3. Polar Bear
4. Hippo
5. Tiger
Answer: '''))
                    if user_input_2 == 3:
                        a = int(input("""\nThat is correct! The first number in the series is '4'.
To store this number, please type it in and press enter: """))
                        numbers.append(a)
                        print("\nYour list so far: ", numbers)
                    elif user_input_2 != 3:
                        print("\nSorry, that is not the right answer, come back later to try again!")
                else:
                    print("\nThey don't know how to captain a ship!\nCome back and try someone else.\n\n(hint: once upon a time he was going to sail around the world. That's how he ended up here.)")

        elif input_1 == "2":
                input_2 = input("Welcome to The Swan.\nSorry for that annoying noise, it never goes away.\nAt this station you will receive 2 numbers for your list.\nYou can get both numbers now if you can tell me how many minutes until that clock resets.\nWant you try? ")
                if input_2.lower().strip() == "yes" or input_2.lower().strip() == "y":
                    input_3 = input("Answer: ")
                    if input_3.strip() == "108":
                        a = int(input("That's correct! You're second and third numbers in the list are 8 and 15.\nType the first number to add it to your list: "))
                        numbers.append(a)
                        b = int(input("Now type the second to add: "))
                        numbers.append(b)
                        print("Nice work!!\nYou're list so far ", numbers)
                        print("\n Please visit another station to reveal more numbers!")
                    else:
                        print("\nSorry, that's not right.\nYou can come back and try again or try the other questions instead.")
                else:
                    input_4 = int(input("\nThats fine, let's move on.\nThe fist question is which of the survivors first discovered The Swan?\n1. John and Boone\n2. Jack and Kate\n3. Charlie and Mr. Eko\n4. None of these\n 5.All of these\nAnswer: "))
                    if input_4 == 1:
                        input_5 = int(input("\nCorrect!!!\n\nNext question is while The Swan is being destroyed, who turns the fail safe key?\n1. John\n2. Ben\n3. Desmond\n4. Hurley\n5. Lachlan and Mayra\nAnswer: "))
                        if input_5 == 3:
                            a = int(input("\nGreat job!!!\nThe second and third numbers in the list are 8 and 15\nType the first number to add it to your list: "))
                            numbers.append(a)
                            b = int(input("Now type the second number to add: "))
                            numbers.append(b)
                            print("Nice work!!\nYou're list so far ", numbers)
                            print("\nPlease visit another station to reveal more numbers!")
                        else:
                            print("\nThat is not correct. You need to get both answers right to reveal the numbers.\nPlease come back and try again.")
                    else:
                        print("\nThat is not correct. Please come back and try again to reveal the 2 numbers.")

        elif input_1 == "3":
                user_input_2 = input("Welcome to The Flame. It doesn't look like much, but it's cozy. \nIn order to receive the number from this station, you will need to answer 2 questions correctly. \nDo you wish to continue? (Y/N)  ")
                if user_input_2.upper() == "Y" or user_input_2.upper() == "YES":
                    q_1 = int(input("The first question is: \nWho discovered the flame? \n1. Sawyer and Kate \n2. Kate and John \n3. Sayid and John \n4. John and Jack \n5. Jack and Kate \nAnswer: "))
                    if q_1 == 3:
                        q_2 = int(input("Great Job! \nThe second question is: \nHow was The Flame destroyed? \n1. Explosion \n2. Fire \n3. Tornado \nAnswer: "))
                        if q_2 == 1:
                            c = int(input("Thats Right! \nThe fourth number in the series is '16' \nTo store this number, please type it in and press enter: "))
                            numbers.append(c)
                            print("Your list so far: ", numbers)
                        else:
                            print("Sorry, that's not the right answer. Come back to this station to try again")
                    else:
                            print("Sorry, that's not the right answer. Come back to this station to try again")
                elif user_input_2.upper == "N" or user_input_2.upper() == "NO":
                    print("Lame. Have fun stuck here forever")
                else:
                    print("That's not a valid selection, come back and try again")

        elif input_1 == "4":
                user_input_2 = input("\nUh oh, looks like there's no numbers to be found in this room!\nPress enter to continue ")
                if user_input_2 == "":
                    print("\nTaking you back....")

        elif input_1 == "5":
                input_2 = input("\nLooks like it's just a garden??\n\nMaybe try a different station.\nPress enter to continue ")
                if user_input_2 == "":
                    print("\nTaking you back....")

        elif input_1 == "6":
                input_2 = input("Looks like The Looking Glass is not on the island! \nYou're going to need the captain again. \nYELL the captains name if you would like a lift. \n")
                if input_2 == captain.upper():
                    input_3 = input("\nIM ON MY WAY MATE!!!! \nDid you bring your scuba gear?\n")
                    if input_3.lower() == "yes" or input_3.lower() == "y":
                        answer = input("Great, you're gonna need it!\nSince it was such a hassle getting down here, you're getting the 2 for 1 special. 1 question answered, 2 numbers received. \n \nWhat did Charlie write on his hand before he died? \nAnswer: ")
                        if answer.strip().lower() == "not penny's boat" or answer.strip().lower() == "not pennys boat":
                            a = int(input("That's correct! \nThe last 2 numbers in the series are 23 and 42 \nTo store these numbers, please enter the first number: "))
                            numbers.append(a)
                            b = int(input("Now enter the second number: "))
                            numbers.append(b)
                            print("Your list so far: ", numbers)
                        else:
                            print("Sorry that is incorrect. \nYou need to go back and watch season 3, episode 22 to find out. \n.......or just google it.")
                    elif input_3.lower() == "no" or input_3.lower() == "n":
                        answer_2 = input("Hopefully you can hold your breath!\nSince it was such a hassle getting down here, you're getting the 2 for 1 special. 1 question answered, 2 numbers received. \n \nWhat did Charlie write on his hand before he died? \nAnswer: ")
                        if answer_2.strip().lower() == "not penny's boat" or answer_2.strip().lower() == "not pennys boat":
                            a = int(input("That's correct! \nThe last 2 numbers in the series are 23 and 42 \nTo store these numbers, please enter the first number:  "))
                            numbers.append(a)
                            b = int(input("Now enter the second number: "))
                            numbers.append(b)
                            print("Your list so far: ", numbers)
                        else:
                            print("Sorry that is incorrect. \nYou need to go back and watch season 3, episode 22 to find out. \n.......or just google it.")
                elif input_2 == "desmond" or input_2 == "Desmond":
                    print("\nYell it LOUDER next time you come back!")
                else:
                    print("\nThat person doesn't know how to captain a ship! Here's a hint, he's Scottish.")

        elif input_1 == "7":
                user_input_2 = input("It's really dark in here...let's head out and try a different station.\nPress enter to return to the list of statios to search. ")
                if user_input_2 == "":
                    print("\nTaking you back....")

        elif input_1 == "8":
                print("Numbers you've collected so far: ", numbers)

        elif input_1 == "9":
                input_2 = input("Are you sure you want to leave? ")
                if input_2.strip().lower() == "y" or input_2.strip().lower() == "yes":
                    input_3 = (input("Please enter the series of 6 numbers and we'll get you out of here.\nThe numbers must be entered in the correct order!\nNumbers: "))
                    if input_3 == "4 8 15 16 23 42":
                        input_4 = input("\nCONGRATS!!!!!\n\nYou get to go home!\n\nSay bye to Vincent before you go!\n")
                        if input_4.lower().strip() == "bye vincent":
                            print("\nWoof Woof!")
                            exit()
                        else:
                            print("He didn't want to say bye anyway!/n")
                            exit()
                    else:
                        print("\nSorry, those are not the right numbers.\n\nPlease come back and try again once you have them.")
                else:
                    print("Glad you decided to stay!\nBernard and Rose need some company.")

        elif input_1 == "10":
                input_1 = input("You sure you want to be stuck here forever? ")
                if input_1.lower() == "yes" or input_1.lower() == "y":
                    print("\nAlright, better luck next time!")
                    quit()
                else:
                    print("Glad you decided to stay!")

        else:
            user_input_2 = input("Sorry that's not a valid selection.\nPlease hit ender to go back. ")
            if user_input_2 == "":
                print("\nTaking you back....")