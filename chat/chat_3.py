import time
import sys
from chat.chat_2 import age

edu = input("What education are you currently in? ")
if edu == "Sixth Form":
    if age <= 19 and age >= 16:
        time.sleep(1)
        print("Your old enough for Sixth Form!")
        year = input("What Year Group are you in? ")
        if year == "Year 12":
            if age == 16 or age == 17:
                time.sleep(1)
            print("First year of Sixth Form")
            time.sleep(1)
            print("Hope your enjoying it!")
            else:
                 time.sleep(1)
                 print("You are not at the right age to be in that year group!")
                 time.sleep(1)
                 print("As you have been lying... ")
                 time.sleep(1)
                 print("This form will now close!")
                 time.sleep(1)
                 print("Goodbye!")
                 sys.exit()
        elif year == "Year 13":
            if age == 17 or age == 18:
                time.sleep(1)
            print("Second year of Sixth Form")
            time.sleep(1)
            print("Hope your having fun!")
            else:
                 time.sleep(1)
                 print("You are not at the right age to be in that year group!")
                 time.sleep(1)
                 print("As you have been lying... ")
                 time.sleep(1)
                 print("This form will now close!")
                 time.sleep(1)
                 print("Goodbye!")
                 sys.exit()
        elif year == "Year 14":
            if age == 18 or age == 19:
                time.sleep(1)
                print("Last year of Sixth Form")
                time.sleep(1)
                print("You will be saying Goodbye soon!")
            else:
                 time.sleep(1)
                 print("You are not at the right age to be in that year group!")
                 time.sleep(1)
                 print("As you have been lying... ")
                 time.sleep(1)
                 print("This form will now close!")
                 time.sleep(1)
                 print("Goodbye!")
                 sys.exit()
            
        else:
            time.sleep(1)
            print("That isn't a valid year")
            time.sleep(1)
            print("This form will now end")
            time.sleep(1)
            print("Goodbye!") 
            sys.exit
    else:
        print("You are not at the right age to be at Sixth Form")
        time.sleep(1)
        print("As you have been lying... ")
        time.sleep(1)
        print("This form will now close!")
        time.sleep(1)
        print("Goodbye!")
        sys.exit()