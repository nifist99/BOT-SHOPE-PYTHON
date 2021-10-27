import time
from tkinter.constants import NO
from requests.models import Response
from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests
from os import system, name
from selenium.webdriver.chrome.service import Service

options = Options()
options.headless = True
options.add_argument("--incognito")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
prefs = {'profile.default_content_setting_values': {'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
options.add_experimental_option("prefs", prefs)
# LOKASI DRIVER WEBCHROEM DI KOMPUTER

s=Service('C:\chromedriver_win32\chromedriver.exe')
browser=webdriver.Chrome(service=s)
actionChains = ActionChains(browser)

#INFO AUTOR

class WindowsInhibitor:
        '''Prevent OS sleep/hibernate in windows; code from:
        https://github.com/h3llrais3r/Deluge-PreventSuspendPlus/blob/master/preventsuspendplus/core.py
        API documentation:
        https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx'''
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001

        def __init__(self):
            pass

        def inhibit(self):
            import ctypes
            print("")
            print("")
            print("======================================")
            print("Inisialisasi..........................")
            print("Preventing Windows from going to sleep")
            ctypes.windll.kernel32.SetThreadExecutionState(
                WindowsInhibitor.ES_CONTINUOUS | \
                WindowsInhibitor.ES_SYSTEM_REQUIRED)

        def uninhibit(self):
            import ctypes
            print("Allowing Windows to go to sleep")
            ctypes.windll.kernel32.SetThreadExecutionState(
                WindowsInhibitor.ES_CONTINUOUS)

def api_server(id_user):
        api_url='https://tanlalana.com/api/get_data'
        api_data={'id':id_user}
        r = requests.post(api_url, data=api_data)
        global res
        res = r.json()

def proses(email,password):
        
        api_url='https://tanlalana.com/api/login_bot'
        api_data={'email':email,'password':password}
        r = requests.post(api_url, data=api_data)
        login_response = r.json()  
    
        if (login_response['api_status']==1 and login_response['data']['status']=='active'):
             global id_user
             id_user = login_response['data']['id']
             print("")
             print("")
             print("Selamat Anda Berhasil Login Lanjutkan Untuk Menjalankan Boot")
             print("============================================================")
             boot()
        elif (login_response['api_status']==4):
             print(login_response['api_message'])
             cek=str(input("[+] Apakah Anda Akan Mencobanya Lagi Jika Iya Ketik Y Jika Tidak Ketik N ? : "))
             if(cek=='Y' or cek=='y'):
                    system('cls')
                    main()
             else:
                    exit()

        elif (login_response['api_status']==3):
             print(login_response['api_message'])
             cek=str(input("[+] Apakah Anda Akan Mencobanya Lagi Jika Iya Ketik Y Jika Tidak Ketik N ? : "))
             if(cek=='Y' or cek=='y'):
                    system('cls')
                    main()
             else:
                    exit()
        elif (login_response['api_status']==2):
           print(login_response['api_message']) 
           cek=str(input("[+] Apakah Anda Akan Mencobanya Lagi Jika Iya Ketik Y Jika Tidak Ketik N ? : "))
           if(cek=='Y' or cek=='y'):
                    system('cls')
                    main()
           else:
                    exit()

                                                                                                        
def authors():
    browser.get("https://shopee.co.id")
    print("----- Versi : Versi 1.0 -----")
    print("----- Author : Laughtale-----")
    print("----- Email : laughtale324@gmail.com -----")
    print("----- Instagram : laugh.tale77 -----")
    print("----- Created In : Shinsekai -----")
    print("----- Name App : Bot Shopee Flash Sale -----")
    print("===========================================")
    print("")
    print("")


def load_cookies():
    browser.get("https://shopee.co.id")
    browser.add_cookie({'name': 'SPC_EC', 'value': res['data']['cookie']})
    browser.get_cookies()
    time_now = time.strftime("%H:%M:%S", time.localtime())
    time.sleep(2)
    print('[+] Jam Sekarang : ',time_now)
    print('[+] Driver init suksess,...')
    print("")


def tombol_beli():
    
    try:
        # judul = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Samsung Galaxy M22 6/128GB Light Blue')]")))
        # actionChains.click(judul).perform()
        # print("[+] item Ketemu", time.strftime("%H:%M:%S", time.localtime()), "Detik")
        # try:
        varians = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[4]")))
        browser.execute_script("arguments[0].click();", varians)
        # except NoSuchElementException as e:
        # varians = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'01 Socialite Peach')]")))
        # browser.execute_script("arguments[0].click();", varians)
        # ukuran = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[3]")))
        # browser.execute_script("arguments[0].click();", ukuran)
   
        # TOMBOL BELI
        beli = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[5]/div/div/button[2]')))
        browser.execute_script("arguments[0].click();", beli)
        print("[+] INFO: Barang Masuk Dalam Keranjang! Dalam", time.strftime("%H:%M:%S", time.localtime()), "Detik")

        #TOMBOL CHECKOUT
        checkout = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[4]')))
        browser.execute_script("arguments[0].click();", checkout)
        print("[+] INFO: Barang otw Checkout!", time.strftime("%H:%M:%S", time.localtime()), "Detik")

        #pinshopee
        
            #TOMBOL PESAN
        pesanan = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[4]/div[2]/div[7]/button')))
        browser.execute_script("arguments[0].click();", pesanan)
        print("[+] INFO: Pesanan Dibuat!", time.strftime("%H:%M:%S", time.localtime()), "Detik")

            #TOMBOL BAYAR
        bayar = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.ID, 'pay-button')))
        bayar.click()
        print("[+] INFO: Otw Bayar!", time.strftime("%H:%M:%S", time.localtime()), "Detik")
            
            # INISIALISASI PIN NUMBER SHOPE PASTIKAN DI CONFIG PIN BENAR
        pin_shopee = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[3]/div[1]')))
        actionChains.send_keys_to_element(pin_shopee).send_keys(res['data']['pin_shope']).perform()
            

            # KONFIRMASI PEMBAYARAN
        konfirmasi = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[4]/div[2]')))
        konfirmasi.click()
        print("[+] INFO: Selamat,..Dapet Barangnya NGab!", time.strftime("%H:%M:%S", time.localtime()), "Detik")
  
        print("===================================")
        print("")
        # api_shope()
        print("")
        print("KALO DAPAT JANGAN LUPA SYUKURAN NGAB !!!!!")
        # api_history()
       
    except NoSuchElementException as e:
        print(e)

# MENU UTAMA PROGRAM DI EKSEKUSI
def boot():
    jam_device = time.strftime("%H:%M:%S", time.localtime())
    print("INFORMASI PRODUK")
    print("========================================")
    api_server(id_user)
    print("")
    print("Wait Proses Inisialisasi Produk Sedang Dilakukan................sabar ngab!!!")
    load_cookies()
    browser.get(res['data']['url'])
    jam = int(input("[+] Masukan Jam untuk memulai beli : "))
    menit = int(input("[+] Masukan Menit untuk memulai beli : "))
    detik = int(input("[+] Masukan Detik untuk memulai beli : "))
    waktu = '{:02d}:{:02d}:{:02d}'.format(jam, menit, detik)
    Inter = 0

    while jam_device <= waktu :
        jam_device = time.strftime("%H:%M:%S", time.localtime())
        jam_device_INT = int(time.strftime("%H%M%S", time.localtime()))
        waktu_int='{:02d}{:02d}{:02d}'.format(jam, menit, detik)
        nilai = int(waktu_int)
        Inter += 1
        osSleep = WindowsInhibitor()
        osSleep.inhibit()
        if(jam_device_INT <= nilai):
            browser.refresh()
            print(jam_device_INT,":",nilai)
            print("[+] INFO:", time.strftime("%H:%M:%S", time.localtime()), "Belum mulai.!")
        else:
            break
    tombol_beli()


def main():
    authors()
    email=str(input("[+] Masukan Email Login ? : "))
    password=str(input("[+] Masukan Password Login ? : "))
    proses(email,password)
    cek=str(input("[+] Apakah Anda Akan Mengakhiri Session Bot Ini ketik Y/y ? : "))
    if(cek=='Y' or cek=='y'):
        browser.quit()
        time.sleep(2)
        exit()
    else:
        system('cls')
        main()

if __name__ == "__main__":
    main()