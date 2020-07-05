from selenium import webdriver
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions




class InstagramBot:


    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()


        #self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div').click()


    def login(self):

        self.driver.get('{}'.format(self.base_url))
        #self.driver.get('https://www.instagram.com/')
        #enter_username = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        #enter_username.send_keys(self.username)
        #enter_password = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        #enter_password.send_keys(self.password)
        time.sleep(3)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
       

                                    

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url,user))
        time.sleep(2)

    def follow_user(self, user):
        self.nav_user(user)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button').click()

    def send_dm(self, user, message):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]').click()
        self.driver.find_element_by_name('queryBox').send_keys(user)  #typing the username in the textbox
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div').click() #click on the name popped up
        #time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div').click()  #clicking next
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message) #clicking on the message box to type message
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]').click() #press send 

        
    def homepage(self):
        self.driver.get(self.base_url)



    #def comment_on_post(self):
    #    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[3]/div/article/div[2]/section[1]/span[2]/button').click()
    #    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/form[1]').click()




                                        
if __name__ == '__main__':
    ig_bot = InstagramBot('rhyylynn', 'popstar123')
    
    #print(ig_bot.username)

    #ig_bot.nav_user('allyyye')
    #ig_bot.send_dm('allyyye','Hello  wassup !')
    #ig_bot.follow_user('allyyye')
    ig_bot.comment_on_post()

    
  
    
  













