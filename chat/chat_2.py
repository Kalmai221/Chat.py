import time
import sys

print("Let's get Started!")
time.sleep(1)
age = int(input("How old are you? ")) 
if age >= 10:
    time.sleep(1)
    print("Great! Your old enough to continue this quiz!")
    import chat.chat_3 as chat_3
elif age <= 10:
        time.sleep(1)
        print("You're too young to be doing this quiz!")
        sys.exit()
else:
    time.sleep(1)
    print("Let's Continue the quiz!")
    time.sleep(1)
    import chat.chat_3 as chat_3