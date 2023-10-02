import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd
import numpy as np
import time
import datetime
from tqdm import tqdm
import sys
#need attention
import multiprocessing.dummy as mp
from lxml import etree
import requests
import logging
import pickle
import json
import string
from zhon.hanzi import punctuation
from threading import Thread
from functools import wraps
import re
import warnings
import ddddocr
import random
import argparse
from  PIL import Image
import shutil
from datetime import datetime
warnings.filterwarnings("ignore")
class eleven():
    
    def __init__(self,core = 3,chromedriver = "/Users/qianyuyang/Desktop/Qianyu/RA/energy_database/driver/chromedriver"):
        self.author = "Qianyu Yang"

        self.core = core

        self.path = chromedriver
        
     
    def get_latest_download_file(self,file_dir="/Users/qianyuyang/Downloads"):
        
        l=os.listdir(file_dir)
        if len(l) == 0:
            return "google"
        l.sort(key=lambda fn: os.path.getmtime(file_dir+"/"+fn) if not os.path.isdir(file_dir+"/"+fn) else 0)

        #get file dowload time
        d=datetime.datetime.fromtimestamp(os.path.getmtime(file_dir+"/"+l[-1]))
        return l[-1]
    def update_latest_download_file(self,file_dir,previous_file):
        l=os.listdir(file_dir)
        update = set(l) - set(previous_file)
        if len(update) == 0:
            return "google"
        else:
            return list(update)[0]
    def get(self,process_num):
        start_url = "https://atlas.eia.gov/search"
        chromedriver = "/Users/qianyuyang/Desktop/Qianyu/RA/energy_database/driver/chromedriver"
        options = webdriver.ChromeOptions()
        get_start_time = str(datetime.now())
        prefs = {"download.default_directory":"/Users/qianyuyang/Downloads/%s"%get_start_time}
        default_download = "/Users/qianyuyang/Downloads/%s"%get_start_time
        if not os.path.exists(default_download):
            os.mkdir(default_download)
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--disable-gpu') 
        driver = webdriver.Chrome(executable_path = chromedriver,options = options)
        driver.get(start_url)
        driver.maximize_window()
        
        xpath = {
        'dataset_button':'//div[@class="col-sm-12"]/h3/div/a',
        'load_button':'//button[@class="btn more-results link-color-primary"]',
        'level_2_button':'//div[@class="stacked-icon"]',
        'detail_button':'//div/a[contains(@class,"btn")]',
        'intro_cordinate':'//div[@class="content-summary"]/div/div/div/div',
        'download_panel_header':'//h1[@class="download-panel-header"]'
        }
        while True:
            try:
                WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['load_button']))).click()
                time.sleep(3)
            except:
                break
        html_source = driver.page_source
        label = etree.HTML(html_source)
        all_dataset_name = label.xpath('//div[@class="col-sm-12"]/h3/div/a/text()')
        
        all_dataset_name = [i.replace("\n","") for i in all_dataset_name]
        all_dataset_name = [" ".join([j for j in i.split(" ") if j != '']) for i in all_dataset_name]
        all_dataset_name = [i.replace("/","_") for i in all_dataset_name]
        
        prev = []
        yb = []
        for ii in all_dataset_name:
            if ii in prev:
                
                yb.append(ii + "*")
            else:
                yb.append(ii)
            prev.append(ii)
        
        all_dataset_name = yb
        
        driver.get('chrome://settings/')
        driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.4);')

        start_url = "https://atlas.eia.gov/search"
        chromedriver = "/Users/qianyuyang/Desktop/Qianyu/RA/energy_database/driver/chromedriver"
        options = webdriver.ChromeOptions()

        # document in google mention this trick to avoid bug
        options.add_argument('--disable-gpu') 
        # not load picture
        #options.add_argument('blink-settings=imagesEnabled=false') 
        # do not use the visable broswer
        # self.options.add_argument('--headless')

        #driver = webdriver.Chrome(executable_path = chromedriver,options = options)
        driver.get(start_url)
        #num_flag = True
        driver.maximize_window()
        
        data_dict = dict()
        for a,b in enumerate(all_dataset_name):
            data_dict[b] = a

        #rest_data = [v for k,v in data_dict.items() if k not in os.listdir('../data') if (v>= int(process_num * len(all_dataset_name) / self.core) and v <= int((process_num + 1) * len(all_dataset_name) / self.core))]
        rest_data = [v for k,v in data_dict.items() if k not in os.listdir('../data') if v % self.core == process_num]
        
        for i in rest_data:
           
            driver.get(start_url)
            while len(driver.find_elements_by_xpath(xpath['dataset_button'])) <= i:
                try:
                    WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['load_button']))).click()
                    time.sleep(5)
                except:
                    break
            WebDriverWait(driver,30,1).until(EC.presence_of_all_elements_located((By.XPATH,xpath['dataset_button'])))
            current_latest_download_file = os.listdir(default_download)
            current_dataset = all_dataset_name[i].replace('/','_')
            if not os.path.exists(os.path.join("../data",current_dataset)):
                os.mkdir(os.path.join("../data",current_dataset))
            current_dataset_path = os.path.join("../data",current_dataset)
            button = driver.find_elements_by_xpath(xpath['dataset_button'])[i]
            driver.execute_script("arguments[0].click();",button)
            time.sleep(random.randint(20,30))
            try:
                WebDriverWait(driver,60,1).until(EC.presence_of_all_elements_located((By.XPATH,xpath['level_2_button'])))
                
                WebDriverWait(driver,60,1).until(EC.presence_of_all_elements_located((By.XPATH,xpath['detail_button'])))
            
            except:
                continue
            
            
            time.sleep(random.randint(5,10))
             
            button = driver.find_element_by_xpath(xpath['detail_button'])
            driver.execute_script("arguments[0].click();",button)
            time.sleep(random.randint(10,20))
            html_source = driver.page_source
            label = etree.HTML(html_source)
            intro_text_list = label.xpath(xpath['intro_cordinate'])
            summary = [itl.xpath("string(.)") for itl in intro_text_list]
            summary = [" ".join([jj for jj in s.split(" ") if jj != '']) for s in summary]
            summary = "\n".join(summary)
            with open(os.path.join(current_dataset_path,"summary.txt"),'w') as f:
                f.write(summary)
                f.close()
            var = 0
            var_dict = {}
            while True:
                print(var_dict)
                try:
                    varibale_container = '''return document.querySelector('arcgis-hub-attributes-list').shadowRoot.querySelectorAll('calcite-accordion-item')[%s].shadowRoot.querySelector('div[class="header-text"]')'''%var
                    sd = driver.execute_script(varibale_container)
                    var_name = sd.find_elements_by_tag_name('span')[0].text
                    var_dict[var_name] = ""
                    var += 1
                    try:
                        description = sd.find_elements_by_tag_name('span')[1].text
                        var_dict[var_name] = description
                    except:
                        continue
                except:
                    break
            with open(os.path.join(current_dataset_path,"description.json"),'w') as outfile:
                json.dump(var_dict, outfile)
                    
            WebDriverWait(driver,60,1).until(EC.presence_of_all_elements_located((By.XPATH,xpath['detail_button'])))
            time.sleep(random.randint(10,15))
            try:
                button = driver.find_elements_by_xpath(xpath['level_2_button'])[1]
                driver.execute_script("arguments[0].click();",button)
                time.sleep(random.randint(20,30))
            except:
                with open(os.path.join(current_dataset_path,"update.txt"),'w') as f:
                    f.write('not avaliable yet')
                    f.close()
                continue
            
            
            file_num = driver.find_elements_by_xpath('//div[@class="dataset-download-card"]')
            
            for di in range(len(file_num)):
                download_start = time.time()
                try:
                    download_button = '''return document.querySelectorAll('div[class="dataset-download-card"] hub-download-card')[%s].shadowRoot.querySelector('calcite-button')'''%di

                    driver.execute_script(download_button).click()
                    
                    time.sleep(3)
                    download_button = '''return document.querySelectorAll('div[class="dataset-download-card"] hub-download-card')[%s].shadowRoot.querySelectorAll('calcite-dropdown-item')[1]'''%di

                    driver.execute_script(download_button).click()
                except AttributeError:
                    
                    time.sleep(15)
                    while 'google' in self.update_latest_download_file(default_download,current_latest_download_file) or 'download' in self.update_latest_download_file(default_download,current_latest_download_file):
                        time.sleep(15)
                        if time.time() - download_start >= 300:
                            with open(os.path.join(current_dataset_path,"update.txt"),'w') as f:
                                f.write('not avaliable yet')
                                f.close()
                            break
                            # driver.quit()
                            # raise TimeoutError
                            
                    latest_download_file = self.update_latest_download_file(default_download,current_latest_download_file)
                    current_latest_download_file = os.listdir(default_download)
                    try:
                        shutil.move(os.path.join(default_download,latest_download_file),current_dataset_path)
                    except:
                        continue
                    time.sleep(random.randint(10,15))
                    continue
            
                
                while 'google' in self.update_latest_download_file(default_download,current_latest_download_file) or 'download' in self.update_latest_download_file(default_download,current_latest_download_file):
                        time.sleep(15)
                        if time.time() - download_start >= 300:
                            with open(os.path.join(current_dataset_path,"update.txt"),'w') as f:
                                f.write('not avaliable yet')
                                f.close()
                            break
                            # driver.quit()
                            # raise TimeoutError
                latest_download_file = self.update_latest_download_file(default_download,current_latest_download_file)
                
                current_latest_download_file = os.listdir(default_download)
                try:
                    shutil.move(os.path.join(default_download,latest_download_file),current_dataset_path)
                except:
                    continue
                time.sleep(random.randint(10,15))
            
            
        driver.quit()
        return
    
    def mp_get(self):
        pool = mp.Pool(self.core)

        process = list(range(self.core))

        p = [pool.apply_async(self.get,args = (a,)) for a in process]

        final_res = [sub_p.get() for sub_p in p]
    
        return

    
if __name__ == "__main__":
    
    for i in tqdm(os.listdir('../data')):
        if (len(os.listdir(os.path.join('../data',i))) in [1,2] and 'update.txt' not in os.listdir(os.path.join('../data',i))) or (len(os.listdir(os.path.join('../data',i))) > 3 and 'update.txt' in os.listdir(os.path.join('../data',i))):
            print(i)
            shutil.rmtree(os.path.join('../data',i))
    eleven().mp_get()
    # while True:
    #     try:
    #         eleven().mp_get()
    #     except:
    #         continue
        