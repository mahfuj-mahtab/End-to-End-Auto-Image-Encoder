# pip install pyhtmlreport
import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

report = Report()
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()
report.setup(
    report_folder=r'E:\end-to-end-encrypton\End-to-End-Auto-Image-Encoder\testing\report',
    module_name='Report',
    release_name='Release 1',
    selenium_driver=driver
)
def isOk():
    try:
        report.write_step(
        'Testing Live functionality',
        status=report.status.Start,
        test_number=1
    )
        driver.get("http://127.0.0.1:8000/")
    except:
        print("Not ok")
    else:
        # print("site is ok")
        report.write_step(
        'Website is live',
        status=report.status.Pass,
        screenshot=True
    )
def LoginUrlOk():
    try:
        report.write_step(
        'Testing Login Url',
        status=report.status.Start,
        test_number=2
    )
        driver.get("http://127.0.0.1:8000/account/login")
    except:
        print("Not ok")
    else:
        # print("site is ok")
        report.write_step(
        'Website is live',
        status=report.status.Pass,
        screenshot=True
    )
def RegisterUrlOk():
    try:
        report.write_step(
        'Testing Register Url',
        status=report.status.Start,
        test_number=3
    )
        driver.get("http://127.0.0.1:8000/account/register")
    except:
        print("Not ok")
    else:
        # print("site is ok")
        report.write_step(
        'Testing Register Url',
        status=report.status.Pass,
        screenshot=True
    )
def WrongUrlOk():
    try:
        report.write_step(
        'Testing Wrong Url',
        status=report.status.Start,
        test_number=4
    )
        driver.get("http://127.0.0.1:8000/account/registerssss")
    except:
        report.write_step(
        'Testing Wrong Url',
        status=report.status.Warn,
        screenshot=True
    )
    else:
        report.write_step(
        'Testing Wrong Url',
        status=report.status.Fail,
        screenshot=True
    )
def LoginButtonClick():
    try:
        report.write_step(
        'Error msg show when login button clicked without filling form',
        status=report.status.Start,
        test_number=5
    )
        driver.get("http://127.0.0.1:8000/account/login")

    except:
        # print(l.get_attribute('innerHTML'))

        report.write_step(
        'Error msg show when login button clicked without filling form',
        status=report.status.Warn,
        screenshot=True
    )
    else:
        time.sleep(5)
        l =driver.find_element(By.CLASS_NAME,'lo_btn').click()
        time.sleep(10)
        k =driver.find_element(By.TAG_NAME,'strong')
        if(k.get_property('innerHTML') == "Sorry Email Or Password Is Wrong!"):
                report.write_step(
            'Error msg show when login button clicked without filling form',
            status=report.status.Pass,
            screenshot=True
                )
        # report.write_step(
        # 'Error msg show when login button clicked without filling form',
        # status=report.status.Fail,
        # screenshot=True
    # )

def WarningCheck():
    try:
        report.write_step(
            'Website Warning Msg Showing  If Not Logged In',
            status=report.status.Start,
            test_number=6
        )
        driver.get("http://127.0.0.1:8000/")
        time.sleep(5)
        h = driver.find_element(By.TAG_NAME,'h1')
        if(h.get_property('innerHTML') == 'You Need To Login To Encode'):
            report.write_step(
                'Website Warning Msg Showing  If Not Logged In',
                status=report.status.Pass,
                screenshot=True
            )
    except:
        print("Not ok")
        report.write_step(
                'Website Warning Msg Showing  If Not Logged In',
                status=report.status.Warn,
                screenshot=True
            )

    else:
        print("site is ok")

    finally:
        driver.close()



isOk()
time.sleep(5)

LoginUrlOk()
time.sleep(5)
RegisterUrlOk()
time.sleep(5)
WrongUrlOk()
time.sleep(5)
LoginButtonClick()
time.sleep(5)
WarningCheck()
time.sleep(5)
report.generate_report()