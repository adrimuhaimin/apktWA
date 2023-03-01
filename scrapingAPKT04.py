from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from copy import deepcopy
import pandas as pd
from datetime import datetime, timedelta


options = webdriver.ChromeOptions()
options = Options() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
options.add_experimental_option('useAutomationExtension', False) 
options.add_argument("--disable-blink-features=AutomationControlled")
#.options.add_argument("user-data-dir={}".format(pro11))
options.add_argument('--disable-infobars')
options.add_argument('disable-web-security')
options.add_argument('disable-popup-blocking')
options.add_argument('ignore-certificate-errors')
options.add_argument('disable-geolocation')
options.add_argument('disable-translate')
#options.add_argument("--no-sandbox")
options.add_argument('--blink-settings=imagesEnabled=True')
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, executable_path=r"C:\\Users\\bin\\chromedriver.exe")
driver.get("http://apkt.pln.co.id/")
#driver.get('http://10.68.35.95/Login.aspx')

USERNAME = "18.ADRI"
PASSWORD = "123456"
userid_input = driver.find_element(By.ID, "txtUserName")
userid_input.send_keys(USERNAME)

pass_input = driver.find_element(By.ID, "txtPassword")
pass_input.send_keys(PASSWORD)


login_button = driver.find_element(By.ID, "btnLogin")
login_button.click()


wait = WebDriverWait(driver, 15)
monitoringAktif = wait.until(EC.presence_of_element_located((By.ID, "ctl00_tvMenut7")))
monitoringAktif.click()

keluhan = wait.until(EC.presence_of_element_located((By.ID, "__tab_ctl00_MainContent2_tcTask_tpKL")))
keluhan.click()

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'html.parser')

tblKeluhan = soup.find('table', id = {'ctl00_MainContent2_tcTask_tpKL_tlKL_webGridTask_grid'})
print(tblKeluhan)


headings = []
header = tblKeluhan.find('tr', {"class" : "headerstyle"})

for b in header.find_all('th'):
    headings.append(b.text)

print(headings)
    #for c in b.find_all('th'):
    #    print(c)

kontenTable = tblKeluhan.find_all('tr', {"class" : "rowstyle"})

isiTable = []
t_row = {}

#headings2 = ['No', 'No. Lapor', 'Tipe Isu', 'Status ', 'Nama', 'Unit', 'No.Telepon', 'Deskripsi', 'Permasalahan', 'Tanggal Buat', 'Tanggal Selesai', 'Lapor', 'Keterangan', 'Durasi', '\\xa0']
for tr in kontenTable:
    findtd = tr.find_all('td')
    for c, th in zip(findtd, headings):
        #isiTable.append(c.text.replace('\n', ' ').strip())
        t_row[th] = c.text.replace('\n', ' ')
        #kemungkinan penggunaan dict th yg tidak dinamis menghambat c yg dinamis
        #menggunakan append berhasil
        #print("ini adalah nilai row", c.text)
    #time.sleep(0.5)
    isiTable.append(deepcopy(t_row))
    #menggunakan deepcopy berhasil tidak memunculkan row 100 semua
    

print(isiTable)

df = pd.DataFrame(isiTable)
print(df)

print(df.loc[0].at["Durasi"])
print(type(df.loc[0].at["Durasi"]))

print(df.shape[0])
#number of rows

print(df.shape[1])
#number of column

print(len(df.index))

nilaiDurasi = []
for i in range(0, df.shape[0]):
    stm = df.loc[i].at["Durasi"]
    t = datetime.strptime(stm[-8:], "%H:%M:%S")

    delta = timedelta(days=int(stm[:len(stm)-9]), hours=t.hour, minutes=t.minute, seconds=t.second)
    nilaiDurasi.append(delta)
print(nilaiDurasi)
df["nilaiDurasi"] = nilaiDurasi

dltaLess = timedelta(days=365)
dltaGreat = timedelta(hours=1)

res = df[(df['nilaiDurasi']<dltaLess) & (df['nilaiDurasi']>dltaGreat)]
print(df)
print(res)

import openpyxl
res.to_excel("output.xlsx", index=False)




