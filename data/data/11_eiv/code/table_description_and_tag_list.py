import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time
import os
import pandas as pd
from datetime import datetime

class driver:
    def __init__(self,executable_path = '/Users/guoquanxiang/coding/energy_data_project/scripts/WebDriver/chromedriver_mac_arm64/chromedriver '):
        
        self.__executable_path = executable_path
        self.chrome_options = webdriver.ChromeOptions()
        self.__service = Service(self.__executable_path)
        self.button_dick = {
            'more_results': "btn.more-results.link-color-primary",
            'more_results_disappear':'btn more-results link-color-primary'
        }
    

    def launch(self,web_page = 'google.com',language = 'en-US'):
        self.chrome_options.add_argument("--lang=en-US")  
        self.chrome_options.add_argument('Accept-Language = en-US,en;q=0.9')
        #set language to english
        self.__driver = webdriver.Chrome(service=self.__service,options = self.chrome_options)
        self.__driver.get(web_page)

    def quit(self):
        self.__driver.quit()


    def get_table_description(self):
        self.launch("https://atlas.eia.gov/search")
        time.sleep(10)
        #more_result = self.__driver.find_element(By.CLASS_NAME,"btn.more-results.link-color-primary")#more results button, to see all results
        more_result = self.__driver.find_element(By.CLASS_NAME,self.button_dick['more_results'])
        #clicking buttons until the end
        wait = WebDriverWait(self.__driver,3)
        while True:
            try:
                more_result.click()
                time.sleep(3)
                wait.until(EC.invisibility_of_element_located((By.CLASS_NAME,self.button_dick['more_results_disappear'])))
            except StaleElementReferenceException:
                break

        #get table infomations
        time.sleep(10)
        table_info = self.__driver.find_elements(By.CSS_SELECTOR,'.metadata-item, .result-name')
        temp = []
        for i in table_info:
            temp.append(i.text)
        starters = ['Type','Rows','Tags','Last Updated','Uploaded']
        result = []
        for i in range(len(temp)):
            if not any(temp[i].startswith(starter) for starter in starters):
                result.append(i)
        last = 0
        index_to_add = []
        for i in result[1:]:
            if i - last != 5:#some tables have no 'rows' tag
                #temp.insert
                index_to_add.append(last)
            last = i
        for i in index_to_add:
            temp.insert(i+3,'Rows: not avaliable')
        
        self.raw_description = temp
        return(self.raw_description)

    def cleaning(self):
        Type = [s for s in self.raw_description if s.startswith('Type')]
        Last_Updated = [s for s in self.raw_description if s.startswith('Last Updated') or s.startswith('Uploaded')]
        Rows = [s for s in self.raw_description if s.startswith('Rows')]
        Tags = [s for s in self.raw_description if s.startswith('Tags')]
        starters = ['Type','Rows','Tags','Last Updated','Uploaded']
        name = [s for s in self.raw_description if not any(s.startswith(starter) for starter in starters)]

        delimiter = ': '
        new_Type = [s.split(delimiter,1)[-1] if isinstance(s,str) and delimiter in s else s for s in Type]
        new_Rows = [s.split(delimiter,1)[-1] if isinstance(s,str) and delimiter in s else s for s in Rows]
        new_Tags = [s.split(delimiter,1)[-1] if isinstance(s,str) and delimiter in s else s for s in Tags]
        new_Last_Updated = [s.split(delimiter,1)[-1] if isinstance(s,str) and delimiter in s else s for s in Last_Updated]

        #spliting tags
        list_of_tags = []
        for i in new_Tags:
            list_of_tags.append(i.split(', '))
        #converting str into datetime
        date_format = "%B %d, %Y"
        datetime_last_update = []
        for i in new_Last_Updated:
            datetime_last_update.append(datetime.strptime(i, date_format))
        num_Rows = [int(num.replace(',','')) if num != 'not avaliable' else pd.NA for num in new_Rows]

        table_description = {
            'Layer_Name':name,
            'Layer_Type':new_Type,
            'Last_Updated_date':datetime_last_update,
            'Rows':num_Rows,
            'Tags':list_of_tags
        }
        table_description_dataframe = pd.DataFrame(table_description)
        return table_description_dataframe
    
    def get_tag_list(self):
        table_description_dataframe = self.cleaning()
        tag_list = [word for sublist in table_description_dataframe.Tags for word in sublist]
        tag_list = list(set(tag_list))
        tag_list.sort()
        tag_dataframe = pd.DataFrame(tag_list,columns=['Tags_name'])
        return(tag_dataframe)



if __name__ == '__main__':
    my_d = driver()
    my_d.get_table_description()
    description = my_d.cleaning()
    tag_list = my_d.get_tag_list()

    description.to_csv('data_description.csv')
    tag_list.to_csv('tag_list.csv')

    my_d.quit()

    print('done')
