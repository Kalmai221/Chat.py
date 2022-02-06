import py_compile
import time
import sys
from progress.bar import Bar


bar = Bar('Loading Python', max=500)
for i in range(500):
    # Do some work
    bar.next()
bar.finish()
time.sleep(3)
print("Checking version... ")
time.sleep(3)
print("Running on version " + sys.version)
time.sleep(2)
print("Checking Code Terminal")
time.sleep(2)
print("Running on " + sys.platform)
time.sleep(2)
print("Verifying Operating System...")
time.sleep(2)
print("Operating System " + sys.platform + " verified")
time.sleep(2)
bar = Bar('Loading settings...', max=500)
for i in range(500):
    # Do some work
    bar.next()
bar.finish()
time.sleep(3)
print("Welcome to Python!") 
time.sleep(3)
print("Finding Requested File (chat.py)")
time.sleep(5)
print("Found chat.py")
time.sleep(3)
bar = Bar('Loading chat.py...', max=500)
for i in range(500):
    # Do some work
    bar.next()
bar.finish()
time.sleep(3)
print("Starting chat.py")
import chat.chat_1 as chat_1
