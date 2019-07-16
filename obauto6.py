from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from msvcrt import getch,kbhit
from sys import exit
import os.path
import csv



def openOB():

    opt = Options()
    opt.add_argument('--log-level=3')
    opt.add_argument('--disable-logging') 

    driver = webdriver.Chrome(service_log_path='NUL',options=opt)
    driver.maximize_window()
    driver.get("https://10.180.66.20/office")

    return driver



def multiSearch(driver):

    while True:

        while True:
            string = input('\nEnter the accounts (or 0 for menu): ')
            accs = string.split()
            if accs:
                break
        
        if accs[0] == "0":
            return

        for ac in accs:

            driver.switch_to.window(driver.window_handles[-1])
            driver.execute_script("window.open('https://10.180.66.20/admin?action=ADMIN::CUST::GoCustQuery')")
            driver.switch_to.window(driver.window_handles[-1])

            driver.find_element_by_name('Username').send_keys(ac)
            driver.find_element_by_name('ExactName').click()
            driver.find_element_by_xpath("//input[@name='custSearch'][@type='button']").click()

            print("Successful searched account: {} !".format(ac))



def multiStatus(driver):

    List = list()

    while True:

        while True:
            string = input('\nEnter the accounts (or 0 for Menu): ')
            accs = string.split()
            if accs:
                break
        
        if accs[0] == "0":
            break

        for ac in accs:

            driver.switch_to.window(driver.window_handles[-1])
            driver.execute_script("window.open('https://10.180.66.20/admin?action=ADMIN::CUST::GoCustQuery')")
            driver.switch_to.window(driver.window_handles[-1])

            driver.find_element_by_name('Username').send_keys(ac)
            driver.find_element_by_name('ExactName').click()
            driver.find_element_by_xpath("//input[@name='custSearch'][@type='button']").click()

            status = "No status, maybe some error occured.."
            try:
                status = driver.find_element_by_class_name('statusReason').text
            except:
                try:
                    status = driver.find_element_by_xpath("//table[1]/tbody/tr[2]/td[2]/table/tbody/tr[./td[contains(text(),'Status:')]]/td[2]/span").text
                except:
                    try:
                        status = driver.find_element_by_xpath('/html/body/span').text
                    except:
                        try:
                            status = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td').text
                        except:
                            print("An Error has occured with the OpenBet page, during the search of {} !".format(ac))
                
            driver.close()

            if not os.path.isfile('accounts.csv'):
                List.insert(0,["Username", "Status"])

            List.append([ac,status])
                                                            ################# we should use a big try/except and open the file once!
            with open('accounts.csv', 'a', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(List)

            writeFile.close()

            print("Successful searched and saved account: {} !".format(ac))

            List.clear()




if __name__ == '__main__':
    
    print("Welcome to OpenBet Office MultiSearch 1.1!")

    while True:

        print("""

%%%%%%  OpenBet MultiSearch Menu  %%%%%%%%%%%%%%%%%%%%%%%%

        1.Open new OpenBet Office window (for security reasons please login manually)
        2.MultiSearch
        3.MultiStatus

        -1.Exit program
                """)

        while True:
            while kbhit(): getch()
            ch = input('Enter your choice: ')
            if ch in {"1","2","3","-1"}:
                break

        if ch=="1":
            try:
                driver = openOB()
            except:
                print("""

-----An Error has occured!----------

Solution suggestions:
1) Check if the Webdriver has been installed correctly.
2) Check if the Chrome browser has been updated resently. You may need to update the Chromedriver too.
   Visit http://chromedriver.chromium.org/downloads to download the latest version.
                        """)
        elif ch=="2":
            try:
                multiSearch(driver)
            except:
                print("""

-----An Error has occured!----------

Solution suggestions:
1) Check if you have login successfully.
2) Check if the last Chrome browser window has been closed. If yes, you have to login again.
3) Check if the OpenBet Office pages have been modified/changed. If yes, then the program needs changes too.
                        """)
        elif ch=="3":
            try:
                multiStatus(driver)
            except:
                print("""

-----An Error has occured!----------

Solution suggestions:
1) Check if you have login successfully.
2) Check if the last Chrome browser window has been closed. If yes, you have to login again.
3) Check if the OpenBet Office pages have been modified/changed. If yes, then the program needs changes too.
                        """)
        elif ch=="-1":
            try:
                driver.quit()
                print("Exiting the program...")
            except:
                print("Exiting the program...")
            exit()

        



