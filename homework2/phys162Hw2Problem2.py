#robertoCampos
#HW2problem2
import sys
import time

if len(sys.argv) == 2:
   print(time.strftime("%m/%d/%Y"))
   print("The word you have entered is: "+sys.argv[1])
else:
   sys.exit("The function of this script is to only intake a single word as the command line argument, otherwise it will exit.")





