# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:32:03 2023

@author: ShendR
"""
from selenium import webdriver
import time


def web_refresher():
    
    driver = webdriver.Firefox()
    
    driver.get('https://acidcow.com/')
    while True:
        time.sleep(20)
        driver.refresh()
    driver.quit()