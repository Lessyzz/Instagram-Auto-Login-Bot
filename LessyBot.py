#from lessyz

from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
  
usr=input('Enter Nickname:')  
pwd=input('Enter Password:')  
  
print("""
==========================

Starting LessyBot

==========================
""")

driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.instagram.com/') 
sleep(1) 


username_box = driver.find_element_by_name('username')
username_box.send_keys(usr) 
  
password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd) 
login_box = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div") 
login_box.click() 
  
driver.quit() 
print("Thx for the using Lessy - Instagram Bot ^^") 
sleep(2)

#end