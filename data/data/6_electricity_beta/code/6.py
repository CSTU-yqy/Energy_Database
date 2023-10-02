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
from datetime import datetime
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
from datetime import datetime, timedelta
import ddddocr
import random
import argparse
from  PIL import Image
import shutil
warnings.filterwarnings("ignore")

if __name__ == "__main__":
    
    def generate_dates(start, end):
        start_date = datetime.strptime(start, "%Y%m")
        end_date = datetime.strptime(end, "%Y%m")
        current_date = start_date

        dates = []

        while current_date <= end_date:
            dates.append(current_date.strftime('%Y%m'))
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)

        return dates
    
    def generate_quarters(start, end):
        start_year, start_quarter = int(start[:4]), int(start[4:6])
        end_year, end_quarter = int(end[:4]), int(end[4:6])
        
        current_year, current_quarter = start_year, start_quarter

        quarters = []

        while (current_year, current_quarter) <= (end_year, end_quarter):
            quarters.append(f'{current_year}{current_quarter:02}')
            
            # Increment the quarter
            current_quarter += 1

            # If the current quarter exceeds 4, reset it to 1 and increment the year
            if current_quarter > 4:
                current_quarter = 1
                current_year += 1

        return quarters
    
    def generate_years(start,end):
        start = int(start)
        end = int(end) + 1
        return [str(i) for i in range(start,end)]
        
    xpath = {
    'freq':{
        'freq_select_button':'//div[@class="time-selection-controls"]/div[@class="selection-menu-button frequency"][1]',
        'freq_button':{
            'monthly':'//label[@for="monthly"]',
            'quarterly':'//label[@for="quarterly"]',
            'annual':'//label[@for="annual"]'
            }
    },
    'download':{
        'download_menu':'//div[@id="main_download_button"]',
        'download_csv_table':'//dl[@class="download_menu"]/dd/a[@id="csv_table"]'
    },
    'data':'//option[@class="link_option"]',
}
    freq_map = {
                'M':'monthly',
                'Q':'quarterly',
                'A':'annual'
            }
    
    flag = 0
    wait_time = 3
    while flag < 3:
        flag = 0
        get_start_time = str(datetime.now())
        prefs = {"download.default_directory":"/Users/qianyuyang/Downloads/%s"%get_start_time}
        default_download = "/Users/qianyuyang/Downloads/%s"%get_start_time
        if not os.path.exists(default_download):
            os.mkdir(default_download)
        
        start_url = "https://www.eia.gov/beta/electricity/data/browser/#/topic/0?agg=2,0,1&fuel=vtvv&sec=g&geo=g&freq=M&tab=consumption-quantity&pin=&rse=0&maptype=0&ltype=pin&ctype=linechart&end=202305&start=200101"
        chromedriver = "/Volumes/TOSHIBA EXT/RA/energy_database/driver/chromedriver"
        options = webdriver.ChromeOptions()
        
        options.add_argument('--disable-gpu') 
    
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path = chromedriver,options = options)
        driver.get(start_url)
        driver.maximize_window()
        for f in xpath['freq']['freq_button'].keys():
            
                
            driver.get(start_url)
            if not os.path.exists('../data/%s'%f):
                os.mkdir('../data/%s'%f)
            for file1 in os.listdir('../data/%s'%f):
                if len(os.listdir('../data/%s/%s'%(f,file1))) == 0:
                    print(file1)
                    os.rmdir('../data/%s/%s'%(f,file1))
            
            try:
                WebDriverWait(driver,20,1).until(EC.presence_of_element_located((By.XPATH,xpath['freq']['freq_select_button'])))
                time.sleep(wait_time)
                driver.find_element_by_xpath(xpath['freq']['freq_select_button']).click()
                time.sleep(wait_time)
                WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['freq']['freq_button'][f])))
                driver.find_element_by_xpath(xpath['freq']['freq_button'][f]).click()
                time.sleep(wait_time)
            except:
                print(f"freq:{f}: error")
                continue
            
            html_source = driver.page_source
            label = etree.HTML(html_source)
            data_list = label.xpath(f"{xpath['data']}/text()")
            
            todolist = set(data_list) - set(os.listdir('../data/%s'%f))
            if len(todolist) == 0:
                flag += 1
                continue
            for j in todolist:
                print(j)
                if 'Plant level data' not in j:
                    print(j)
                    idx = data_list.index(j)
                    
                    try:
                        WebDriverWait(driver,10,1).until(EC.presence_of_all_elements_located((By.XPATH,xpath['data'])))[idx].click()
                        time.sleep(wait_time)
                    except:
                        print(f"data:{j}: error")
                        continue
                    
                    try:
                        time.sleep(wait_time)
                        WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['download']['download_menu']))).click()
                        time.sleep(wait_time)
                        WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['download']['download_csv_table']))).click()
                        time.sleep(wait_time)
                    except:
                        print(f"download:{j}: error")
                        continue
                    if not os.path.exists('../data/%s/%s'%(f,j)):
                        os.mkdir('../data/%s/%s'%(f,j))
                    for file in os.listdir(f'{default_download}'):
                        shutil.move(f'{default_download}/{file}','../data/%s/%s'%(f,j))
                    time.sleep(wait_time)
        j = 'Plant level data'        
        print('change')
        print(j)
        # add a part for plant level data
        """
        overview
            M: 200101-202305, Q: 200101-202301, A: 2001-2022
        generation
            M: 200101-202305, Q: 200101-202301, A: 2001-2022
        consumption: consumption-mmbtu_unit, consumption-quantity, consumption-mmbtu
            M: 200101-202305, Q: 200101-202301, A: 2001-2022
        water: water-rate, water-volume, water-intensity, water-source
            M: 201401-202112, Q: 201401-202104, A: 2014-2021
        annual_emissions
            A: 2014-2021
        """
        plant_level_dict = {
            'overview':{
                'M': generate_dates("200101", "202305"),
                'Q': generate_quarters("200101", "202301"),
                'A': generate_years('2001','2022')
            },
            'generation':{
                'M': generate_dates("200101", "202305"),
                'Q': generate_quarters("200101", "202301"),
                'A': generate_years('2001','2022')
            },
            'consumption-mmbtu_unit':{
                'M': generate_dates("200101", "202305"),
                'Q': generate_quarters("200101", "202301"),
                'A': generate_years('2001','2022')
            },
            'consumption-quantity':{
                'M': generate_dates("200101", "202305"),
                'Q': generate_quarters("200101", "202301"),
                'A': generate_years('2001','2022')
            },
            'consumption-mmbtu':{
                'M': generate_dates("200101", "202305"),
                'Q': generate_quarters("200101", "202301"),
                'A': generate_years('2001','2022')
            },
            'water-rate':{
                'M': generate_dates("201401", "202112"),
                'Q': generate_quarters("201401", "202104"),
                'A': generate_years('2014','2021')
            },
            'water-intensity':{
                'M': generate_dates("201401", "202112"),
                'Q': generate_quarters("201401", "202104"),
                'A': generate_years('2014','2021')
            },
            'water-source':{
                'M': generate_dates("201401", "202112"),
                'Q': generate_quarters("201401", "202104"),
                'A': generate_years('2014','2021')
            },
            'water-volume':{
                'M': generate_dates("201401", "202112"),
                'Q': generate_quarters("201401", "202104"),
                'A': generate_years('2014','2021')
            },
            'annual_emissions':{
                'A': generate_years('2014','2021')
            }
        }
        for tab,v in plant_level_dict.items():
            for freq,vv in v.items():
                for datecode in vv:
                    
                    print(tab,freq,datecode)
                    if os.path.exists(f"../data/{freq_map[freq]}/{j}/{tab}/{datecode}.csv"):
                        continue
                    page_url = f"https://www.eia.gov/beta/electricity/data/browser/#/topic/1?agg=2,0,1&fuel=vtvv&sec=g&geo=g&freq={freq}&datecode={datecode}&tab={tab}&maptype=0&rse=0&pin=&ltype=pin&ctype=linechart&end=202305&start=200101"
                    driver.get(page_url)
                    if not os.path.exists('../data/%s'%f):
                        os.mkdir('../data/%s'%f)
                    for file1 in os.listdir('../data/%s'%f):
                        if len(os.listdir('../data/%s/%s'%(f,file1))) == 0:
                            print(file1)
                            os.rmdir('../data/%s/%s'%(f,file1))
                    
                    try:
                        time.sleep(wait_time)
                        WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['download']['download_menu']))).click()
                        time.sleep(wait_time)
                        WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['download']['download_csv_table']))).click()
                        time.sleep(wait_time)
                    except:
                        
                        try:
                            time.sleep(10)
                            WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['download']['download_menu']))).click()
                            time.sleep(5)
                            WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH,xpath['download']['download_csv_table']))).click()
                            time.sleep(10)
                        except:
                            print(f"download:{j}: error")
                            continue
                        
                        pass
                    if not os.path.exists('../data/%s/%s'%(freq_map[freq],j)):
                        os.mkdir('../data/%s/%s'%(freq_map[freq],j))
                    if not os.path.exists('../data/%s/%s/%s'%(freq_map[freq],j,tab)):
                        os.mkdir('../data/%s/%s/%s'%(freq_map[freq],j,tab))
                    for file in os.listdir(f'{default_download}'):
                        shutil.move(f'{default_download}/{file}',f"../data/{freq_map[freq]}/{j}/{tab}/{datecode}.csv")
                    time.sleep(wait_time)
                    
            
        driver.quit()
            
        wait_time += 1
                
            
            