# Watts up? Pro
Final Version




Table of Contents
* 1 INTRODUCTION 
* 2 USAGE 
* 3 FILES 
* 4 TO DO 
* 5 REPORT (WHAT I DID)
* 6 LICENSE


### INTRODUCTION 

This is a simple Python utility for logging data from a [Watts Up? Pro]
power meter.  Documentation for the serial port interface for the
mete. You can find the .pdf manual [here](https://www.wattsupmeters.com/secure/downloads/CommunicationsProtocol090824.pdf)

Other software capable of logging data on the Watts Up? meter are
available for [download from watts up?](https://www.wattsupmeters.com/secure/support.php), and they sell a [realtime version for Windows](https://orders.wattsupmeters.com/store/home.php?cat=26) .

The program will by default assume the most common device name for
Linux and OS X platforms, but the serial port device can also be
specified with the command line option -p

The Watts Up? Pro uses an FTDI serial to USB adapter internally.  If
the driver is not already installed on your operating system, download
the latest driver from the [FTDI website](http://www.ftdichip.com/Drivers/VCP.htm).

The files and packages I used are here under [FTDI](/ftdi) foder


### USAGE

In here there a

Basic command line to run an independent script is: 
''' python
wattsup.py -l -o sample.log
'''
outputs: sample.log
(this version requires numpy and matplotlib installed in your linux flavor)

Another way to run is by just using -l flag. It will output a default .log file
''' python
wattsup_USB0.py -l
'''
outputs: log0.out

wattsup_USB0.py will "ALWAYS" look only for the FTDI USB0 "ONLY". If run wattsup_USBX.py it will output logX.out and look only for the USBX port. If port is not enable it will not run.

run also wattup -h for full description


### FILES

'wattsup.py': logs and display the data to console, and generates a simple real time plot 
'plot.py': Simple plottin program for files already logged.
'wattui.py': Interface to power meter (this version still on beta testing). Click [here](http://code.enthought.com/projects/traits_ui/) for more information
'files.raw': Sample files generated from this program
'run.sh': simple script on bash to run multiple python files


### TO DO 

- Working on multiprocessing to run multiple python scripts wattsup_USBx.py at the same time
- Fetching data from internal storage from Watts Up? Pro
- Cumulative display of energy used
- Ask user for optiontial plotting for power(watts), current(amps) or volts(v).


### REPORT (What I did so far)

- Build from scratch a "mini server" to simulate the work load.
- Install ubuntu
- update packages
- install FTDI drivers for WATTS UP PRO
- created a git repository for all watts up pro
- update python libraries: numpy and matplotlib
	sudo apt-get install python-os
	sudo apt-get install python-numpy
	sudo apt-get install matplotlib.pyplot
- working on home/administrator directory
- use multiprocessing in python to run  4 different python scripts at the same time create 4 different wattsup.py versions, each with a single port 
- Files used: 
  wattsup_USB0.py using port /dev/ttyUSB0 in line 169(args.port=/dev/ttyUSB0), 179(message…) 204 (log0.out) 
  wattsup_USB1.py using port /dev/ttyUSB1 in line 169(args.port=/dev/ttyUSB1), 179(message…) 204 (log1.out)  
  wattsup_USB2.py using port /dev/ttyUSB2 in line 169(args.port=/dev/ttyUSB2), 179(message…) 204 (log2.out)  
  wattsup_USB3.py using port /dev/ttyUSB3 in line 169(args.port=/dev/ttyUSB3), 179(message…) 204 (log3.out)  
- created run.sh and give permissions chmod u+x run.sh

### Licence

These programs are free software: you can redistribute them and/or modify them under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.  A copy of the GPL version 3 license can be found in the file COPYING or at
[http://www.gnu.org/licenses].

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

Implemented by: 

Isaac Lino 
University of California, Riverside
BCOE | Computer Engineer
ilino001@ucr.edu
