from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1.ตั้งค่าให้โหลด driver และเปิด chrome อัตโนมัติ
print("กำลังเปิด Youtube..")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

 
print("เปิดสำเร็จ กำลังเล่นวีดิโอ..")
driver.get("https://www.youtube.com/watch?v=Gp_vW-7bOkk")
    
input("Press Enter to Exit...")
    
print("เปิดสำเร็จ! หัวข้อเว็บคือ:",driver.title)