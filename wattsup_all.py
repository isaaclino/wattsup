# It will run 4 wattsup scripts at the same time

import os
print "running Watts Up? pro on USB001 and USB002"
os.system("python wattsup_USB0.py -l & python wattsup_USB1.py")
#print "running Watts Up? pro on USB002"
#os.system("python wattsup_USB1.py -l")
