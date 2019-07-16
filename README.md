# Automation-with-selenium
This is a script/program which opens multiple tabs and extract data from a site. 


Welcome to Multisearch!


 Multisearch is a python program-script that uses python's selenium framework to automates the OB's account search in Google Chrome browser.

 Multisearch simulates the copy-paste of the username and the click to find customers in OB's Office page. You can copy-paste all the usernames that you want to search at once and the program will open all the tabs for you. 


 It uses Python 3.7 and Selenium framework, but the program is in executive format (.exe) and you don not need to install them. To control the Google Chrome webrowser uses the Chrome webdriver (ChromeDriver).



 To run the program:

1) You need to download the ChromeDriver from this page: http://chromedriver.chromium.org/downloads

 The ChromeDriver must be the same version as the Chrome browser version (Chrome browser version 76 ->  ChromeDriver 76)

 Just download it, put it in any directory you want (but be careful with te permissions of that directory, maybe cause prolems) and put this directory to the Path variable of windows. 

2) Run the Multisearch.exe file from any directory you want.





 You have to be able to see that Menu in a window:


Welcome to OB MultiSearch 1.1!



%%%%%%  OB MultiSearch Menu  %%%%%%%%%%%%%%%%%%%%%%%%

        1.Open new OB window (for security reasons please login manually)
        2.MultiSearch
        3.MultiStatus

        -1.Exit program


Enter your choice:



 Choice 1: will open a chrome window and navigate it to OB's page. For security reasons you have to login manually in this page.

 Choice 2: you will see the follow message:

Enter the accounts (or 0 for menu):

 where you can put the accounts you want to search or 0 to return to the main menu. If you put your accounts then the browser will open one-by-one the tabs with each account's data. 
 After you finish with them you can close the tabs, but if you close all tabs (end session), the whole browser, you have to login again in order to do another search.
 When the search will be completed you will see the above message and you can perform another search.

 Choice 3: you will see again the follow message:

Enter the accounts (or 0 for menu):

 but here the program opens a tab, navigates to account's data, extracts the status of the account, then closes the tab and saves the Username, Status in the accounts.csv file. 
 Because the tab closes, you can enter a big number of accounts in this choice.

 Choice -1: closes the browser, if it still open and exits the program. 




