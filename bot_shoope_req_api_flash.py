import time
from tkinter.constants import NO
from selenium import webdriver
# import pyfiglet as f
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests
from os import system, name

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

browser = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')


actionChains = ActionChains(browser)

def api_server(id_user):
        api_url='https://tanlalana.com/api/get_data'
        api_data={'id':id_user}
        r = requests.post(api_url, data=api_data)
        global res
        res = r.json()

def informasi_data():
    print("\033[92mINFORMASI YANG TELAH DI ISI DI PARAMETER SETTING BOT")
    print("\033[92m===================================================")
    print("\033[31m[+]Pin Shope :",str(res['data']['pin_shope'])+" Pastikan saldo mencukupi agar bisa checkout")
    print("\033[31m[+]Url Produk :",res['data']['url'])
    print("\033[31m[+]Item ID :",res['data']['itemid'])
    print("\033[31m[+]Shope ID :",res['data']['shopeid'])
    if(res['data']['varian']!=None):
        print("\033[31m[+]Varian :",res['data']['varian']+" Ini opsional isi jika ada varian jika tidak ada kosongkan agar tidak error")

    if(res['data']['ukuran']!=None):
        print("\033[31m[+]Ukuran :",res['data']['ukuran']+" Ini opsional isi jika ada ukuran jika tidak ada kosongkan agar tidak error")
    print("\033[92m===================================================")
    print("")
    print("")


def api_shope():
        itemid=int(res['data']['itemid'])
        shopeid=int(res['data']['shopeid'])
        ploads = {'itemid':itemid,'shopid':shopeid}
        response = requests.get('https://shopee.co.id/api/v4/item/get',params=ploads)
        response = response.json()
        global repository
        repository = response['data']
        if(repository["flash_sale"] is None and repository["upcoming_flash_sale"] is None):
            print(f'Flas_sale: {repository["flash_sale"]}')
            print(f'Upcoming Flas_sale: {repository["upcoming_flash_sale"]}')
            print('Tidak Ada Flash Sale Di Produk Ini Mungkin Di Jam Setelahnya Lagi')
           
        elif(repository["flash_sale"] is None and repository["upcoming_flash_sale"] != None):
            print('\033[93m[+] evemt flash sale belum di mulai')
            print("\033[93m[+] Nama Barang :",repository['name'])
            print("\033[93m[+] Start Time :",time.strftime('%H:%M:%S', time.localtime(repository['upcoming_flash_sale']['start_time'])))
            print("\033[93m[+] End TIme :",time.strftime('%H:%M:%S', time.localtime(repository['upcoming_flash_sale']['end_time'])))
        elif(repository["flash_sale"] != None and repository["upcoming_flash_sale"] is None):
            print("\033[93m[+]event flash sale dimulaii")
            print("\033[93m[+]Nama Barang :",repository['name'])
            print("\033[93m[+]Stock :",repository['flash_sale']['flash_sale_stock'])
            print("\033[93m[+]Sisa Stock :",repository['flash_sale']['stock'])
            print("\033[93m[+]Harga Flash Sale :",repository['flash_sale']['price'])
            print("\033[93m[+]Harga Normal :",repository['flash_sale']['price_before_discount'])
            print("\033[93m[+]Start Time :",time.strftime('%H:%M:%S', time.localtime(repository['flash_sale']['start_time'])))
            print("\033[93m[+]End TIme :",time.strftime('%H:%M:%S', time.localtime(repository['flash_sale']['end_time'])))

def proses(email,password):
        
        api_url='https://tanlalana.com/api/login_bot'
        api_data={'email':email,'password':password}
        r = requests.post(api_url, data=api_data)
        login_response = r.json()  
    
        if (login_response['api_status']==1 and login_response['data']['status']=='active'):
             global id_user
             id_user = login_response['data']['id']
             print("\033[32m[+]Selamat Anda Berhasil Login Lanjutkan Untuk Menjalankan Boot")
             boot()
        elif (login_response['api_status']==4):
             print(login_response['api_message'])
             cek=str(input("\033[32m[+] Apakah Anda Akan Mencobanya Lagi Jika Iya Ketik Y Jika Tidak Ketik N ? : "))
             if(cek=='Y' or cek=='y'):
                    system('cls')
                    main()
             else:
                    exit()

        elif (login_response['api_status']==3):
             print(login_response['api_message'])
             cek=str(input("\033[32m[+] Apakah Anda Akan Mencobanya Lagi Jika Iya Ketik Y Jika Tidak Ketik N ? : "))
             if(cek=='Y' or cek=='y'):
                    system('cls')
                    main()
             else:
                    exit()
        elif (login_response['api_status']==2):
           print(login_response['api_message']) 
           cek=str(input("\033[32m[+] Apakah Anda Akan Mencobanya Lagi Jika Iya Ketik Y Jika Tidak Ketik N ? : "))
           if(cek=='Y' or cek=='y'):
                    system('cls')
                    main()
           else:
                    exit()


#INFO AUTOR

def authors():
    browser.get("https://shopee.co.id")
    # style = f.figlet_format("Tanlalana")
    # print(style)
    print("\033[31m----- \033[93mVersi : \033[92mBot Shopee Versi 1 \033[31m-----")
    print("\033[31m----- \033[93mInstagram : \033[92mFollow tanlalana_ \033[31m-----")
    print("\033[31m----- \033[93mAuthor : \033[92mTanlalana Bot Pyton   \033[31m-----")
    print("\033[31m----- \033[93mNote : \033[92mJangan Di Publish Sembarangan Susah Bikinya NGAB !!   \033[31m-----")
    print("\033[31m----- \033[93m================================================================\033[31m-----")
    print("\033[31m----- \033[93m Pastikan Produk Yang Mau Di Beli Sudah Di Setting Di Menu GUInya Dan Data Sudah Success Save \033[31m-----")

# def finish():
#     style = f.figlet_format("Dapat Flash Salenya Syukuran Anjing")
#     time.sleep(2)
#     print(style)

# def error():
#     style = f.figlet_format("SYSTEM ERROR SHOPE TELAH DI PERBARUI")
#     time.sleep(2)
#     print(style)
#GET COOKIE LOGIN SHOPEE


def load_cookies():
    browser.get("https://shopee.co.id")
    browser.add_cookie({'name': 'SPC_EC', 'value': res['data']['cookie']})
    browser.get_cookies()
    time_now = time.strftime("%H:%M:%S", time.localtime())
    time.sleep(2)
    print('\033[32m[+] Jam Sekarang : ',time_now)
    print('\033[32m[+] Driver init suksess,...')

#FUNGSI TOMBOL BELI
#FUNGSI TOMBOL BELI

def tombol_beli():
    try:

        # ISI DISINI JIKA ADA MENU VARIASI ATAU WARNA 
        # print("//button[contains(text(),"+"'"+res['data']['varian']+"'"+")]")
        if(res['data']['varian'] is None):
                pass
                print("\033[32m[+] INFO: Varian warna atau jenis tidak ada")
        else:
                varians = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),"+"'"+res['data']['varian']+"'"+")]")))
                browser.execute_script("arguments[0].click();", varians)
                print("\033[32m[+] INFO: Varian yang di pilih :"+res['data']['varian'])

        # UKURAN JIKA ORDER SEPATU
        if(res['data']['ukuran'] is None):
            pass
            print("\033[32m[+] INFO: Ukuran Barang Tidak Ada")
        else:
                ukuran = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),"+"'"+res['data']['ukuran']+"'"+")]")))
                browser.execute_script("arguments[0].click();", ukuran)
                print("\033[32m[+] INFO: Ukuran yang di pilih :"+res['data']['ukuran'])
        
        # ISI JUMLAH JUANTITAS DISINI JIKA CUMA BELI 1 GAK USAHcl

        # jumlah = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
        # jumlah.clear()
        # actionChains.context_click(jumlah).send_keys("2").perform()

        # TOMBOL BELI
        beli = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[5]/div/div/button[2]')))
        browser.execute_script("arguments[0].click();", beli)
        print("\033[32m[+] INFO: Barang Masuk Dalam Keranjang! Dalam\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        #TOMBOL CHECKOUT
        checkout = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button/span')))
        browser.execute_script("arguments[0].click();", checkout)
        print("\033[32m[+] INFO: Barang otw Checkout!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        #TOMBOL PESAN
        pesanan = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[3]/div[2]/div[4]/div[2]/div[7]/button')))
        browser.execute_script("arguments[0].click();", pesanan)
        print("\033[32m[+] INFO: Pesanan Dibuat!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        #TOMBOL BAYAR
        bayar = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.ID, 'pay-button')))
        bayar.click()
        print("\033[32m[+] INFO: Otw Bayar!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
        
        # INISIALISASI PIN NUMBER SHOPE PASTIKAN DI CONFIG PIN BENAR
        pin_shopee = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[3]/div[1]')))
        actionChains.send_keys_to_element(pin_shopee).send_keys(res['data']['pin_shope']).perform()
        

        # KONFIRMASI PEMBAYARAN
        konfirmasi = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[4]/div[2]')))
        konfirmasi.click()
        print("\033[32m[+] INFO: Selamat,..Dapet Barangnya NGab!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")

        # finish()
        api_shope()
       
    except NoSuchElementException as e:
        print(e)
        # error()

# MENU UTAMA PROGRAM DI EKSEKUSI
def boot():
    jam_device = time.strftime("%H:%M:%S", time.localtime())
    print("\033[31mINFORMASI PRODUK")
    print("\033[93m========================================")
    api_server(id_user)
    api_shope()
    print("\033[31mWait Proses Inisialisasi Produk Sedang Dilakukan................sabar ngab!!!")
    load_cookies()
    informasi_data()
    browser.get(res['data']['url'])
    time.sleep(5)
    if(repository['upcoming_flash_sale'] is None):
        waktu = time.strftime('%H:%M:%S', time.localtime(repository['flash_sale']['start_time']))
    else:
        waktu = time.strftime('%H:%M:%S', time.localtime(repository['upcoming_flash_sale']['start_time']))

    str(input("\033[32m[+] Silahkan Ketik Apapun Lalu Enter ? : "))

    while jam_device != waktu :
        itemid=int(res['data']['itemid'])
        shopeid=int(res['data']['shopeid'])
        param = {'itemid':itemid,'shopid':shopeid}
        r = requests.get('https://shopee.co.id/api/v4/item/get',params=param)
        json_r = r.json()
        res_shope = json_r['data']
        if(res_shope["flash_sale"] is None and res_shope["upcoming_flash_sale"] != None):
           print('\033[32m[+] evemt flash sale belum di mulai')
           print("\033[32m[+] INFO:\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mBelum mulai.!")
        else:
            browser.refresh()
            break

    tombol_beli()

def main():
    authors()
    time.sleep(5)
    email=str(input("\033[32m[+] Masukan Email Login ? : "))
    password=str(input("\033[32m[+] Masukan Password Login ? : "))
    proses(email,password)

if __name__ == "__main__":
    main()