from selenium import webdriver
import time
from random import randint


def startMethod(user, password):
    global bot
    bot = TinderBot()
    s = bot.login(user, password)
    if s:
        while 1:
            i = 0
            if i == 0:
                print('______________________________________________________')
            i = i+1
            print("Swipe attempt number: " + str(i))
            bot.swipe()

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')

    def login(self, user, password):
        self.driver.get('https://tinder.com')
        time.sleep(5)
        pNum = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        pNum.click()

        time.sleep(3)

        #saving the base window after loging in
        baseWindow = self.driver.window_handles

        if(len(baseWindow)== 1):
            self.driver.quit()
            startMethod(user, password)
        else:
            self.driver.switch_to.window(self.driver.window_handles[1])
            emailInput = self.driver.find_element_by_xpath('//*[@id="email"]')
            emailInput.send_keys(str(user))
            time.sleep(1)
            passwrdInput = self.driver.find_element_by_xpath('//*[@id="pass"]')
            passwrdInput.send_keys(str(password))

            time.sleep(1)
            loginBtn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            loginBtn.click()
            time.sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[0])

            allowBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            allowBtn.click()

            enableBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            enableBtn.click()

            cancelBtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/button')
            cancelBtn.click()
            time.sleep(5)

            noThanksBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            noThanksBtn.click()
            return True

    def swipe(self):
        window = self.driver.window_handles
        self.driver.switch_to.window(window[0])
        waitNum = randint(1, 5)
        randNum = randint(0, 10)
        if randNum < 8:
            print("Going to Like after " + str(waitNum) + " seconds")
        else:
            print("Going to Dislike after " + str(waitNum) + " seconds")
        time.sleep(waitNum)

        if randNum < 8:
            try:
                notInterestedBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                notInterestedBtn.click()
                print('****NO SWIPE HAS HAPPENED****')
                print('______________________________________________________')
            except:
                try:
                    noThanksBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
                    noThanksBtn.click()
                    print('****NO SWIPE HAS HAPPENED****')
                    print('______________________________________________________')
                except:
                    try:
                        matchBtn = self.driver.find_element_by_xpath('//*[id@="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
                        matchBtn.click()
                        print('****Closed Match****')
                        print('______________________________________________________')
                    except:
                        likeBtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
                        likeBtn.click()
                        print('______________________________________________________')
        else:
            try:
                notInterestedBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                notInterestedBtn.click()
                print('****NO SWIPE HAS HAPPENED****')
                print('______________________________________________________')
            except:
                try:
                    noThanksBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
                    noThanksBtn.click()
                    print('****NO SWIPE HAS HAPPENED****')
                    print('______________________________________________________')
                except:
                    try:
                        matchBtn = self.driver.find_element_by_xpath('//*[id@="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
                        matchBtn.click()
                        print('****Closed Match****')
                        print('______________________________________________________')
                    except:
                        disBtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
                        disBtn.click()
                        print('______________________________________________________')





