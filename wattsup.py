##! /bin/bash
#
#python wattsup_USB0.py &
#python wattsup_USB1.py &
#python wattsup_USB2.py &
#python wattsup_USB3.py &



# It will run 4 wattsup scripts at the same time



import multiprocessing

def worker(file):

#add more wattsup_USB0.py after been created

if __name__ == '__main__':
    files = ["wattsup_USB0.py","wattsup_USB1.py","wattsup_USB2.py","wattsup_USB3.py"]
    for i in files:
        p = multiprocessing.Process(target=worker(i))
        p.start()
