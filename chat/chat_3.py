import time
from chat.chat_2 import age

edu = input("What education are you currently in? ")
if edu == "Sixth Form":
    if age <= 18 and age >= 16:
        time.sleep(1)
        print("Your old enough for Sixth Form!")
        year = input("What Year Group are you in? ")
        if year == "Year 12":
            time.sleep(1)
            print("First year of Sixth Form")
            time.sleep(1)
            print("Hope your enjoying it!")
        elif year == "Year 13":
            time.sleep(1)
            print("Second year of Sixth Form")
            time.sleep(1)
            print("Hope your having fun!")
        elif year == "Year 14":
            time.sleep(1)
            print("Last year of Sixth Form")
            time.sleep(1)
            print("You will be saying Goodbye soon!")
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