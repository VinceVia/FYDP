# FYDP
This repo contains software for the MWX Testbench. It is written in Python 3 and meant to run on Raspbian (tested with Raspberry Pi 3B+). Written by Arjun von Hatten and Sophie Walford, 2019.
------------------------------------------------------------------------------------------------------------------------------
Run the following commands to install dependencies:  
sudo apt install python3-tk  
sudo apt install python3-pip  
pip3 install wheel  
pip3 install pandas  
pip3 install matplotlib  
pip3 install serial  
pip3 install minimalmodbus  

------------------------------------------------------------------------------------------------------------------------------

To start the software, run: ./UI.py  

------------------------------------------------------------------------------------------------------------------------------

Below is a brief description of each file.

UI.py: Starts everything.

startPage.py: Start page. The first screen the user sees. (Frame 1 of 3)

motorRoutine.py: Controls motor routine over RS-485, writes encoder measurements to database, and prompts user to enter  temperature and air release information.

motorFunctions.py: Contains functions for setting motor speed, gathering sensor data, initiating RS-485 communication, and other motor-related tasks.

graphPage.py: Displays test results. (Frame 2 of 3).

previousGraphPage.py: Nearly identical to graphPage.py, but displays previous test results. (Frame 3 of 3).

graphFunctions.py: Detailed failure info.

dao.py: General database functions.

detailedResultsDao.py: Functions to read and write from database.

settings.py: Global variables. Eg. language setting.

misc.py: Other common functions used by multiple classes.

------------------------------------------------------------------------------------------------------------------------------

The database is written in sqlite and contains the following tables.

detailedResults: Contains detailed test results for each test.  
                 -one column per sensor  
                 -one row per sample time  
                 
resultById: Aggregate of historical test results for a given MWX sensor (sorted by serial number).  
                 -get/set failure mode  
                 -one row per test  
                 -id matches to testId in detailedResults table  
                 -test_status: part of a state machine which indicates current status of test  
                 -failure_mode: fail case  

