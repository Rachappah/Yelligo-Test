'''
Created on 11/04/2017

@author: Rachappa
'''
from selenium import webdriver
import time
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://54.213.247.169/yelligo/login.html")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[2]/input").send_keys("Yelligo@gmail.com")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[3]/input").send_keys("1234")
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/select").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/select/option[1]").click()
    #time.sleep(2)
    #driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block bt-color']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@class='btn btn-default btn-xl page-scroll']").click()
    time.sleep(10)
    pass1=driver.find_element_by_xpath("//a[@class='btn btn-default btn-xl page-scroll']").click()
    time.sleep(10)
    pass2=driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[3]/a").click()
    time.sleep(10)
    pass3=driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[4]/a").click()
    time.sleep(10)
    pass4=driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[5]/a").click()
    time.sleep(10)
    pass5=driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[6]/a").click()
    time.sleep(10)
    pass6=driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[7]/a").click()
    time.sleep(2)
    pass7=driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[8]/a").click()
    time.sleep(2)
    pass8=driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[9]/a").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[2]/input").send_keys("Yelligo@gmail.com")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[3]/input").send_keys("1234")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/select").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='loginForm']/div/div[4]/select/option[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block bt-color']").click()
    
    
    
    
