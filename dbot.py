#!/usr/bin/env python3
import sqlite3
from selenium import webdriver
from selenium.webdriver.support.ui import Select

login_id = 'admin'
login_pwd = 'admin'
aps_server = 'aps.kerker.tp.edu.tw'
aps_port = '80'

# browser = webdriver.Firefox()

def set_aps(target_ip):
    page_login = 'http://' + target_ip + '/default.htm'
    page_aps = 'http://' + target_ip + '/autoprov.htm'
    page_restart = 'http://' + target_ip + '/rst.htm'
    # 登入
    browser.get(page_login)
    elem = browser.find_element_by_name('login_id')
    elem.clear()
    elem.send_keys(login_id)
    elem = browser.find_element_by_name('login_pwd')
    elem.clear()
    elem.send_keys(login_pwd)
    elem = browser.find_element_by_name('bntSubmit')
    elem.click() 
    # 改 APS
    browser.get(page_aps)
    select = Select(browser.find_element_by_name('auto_protocol'))
    select.select_by_value('2')
    elem = browser.find_element_by_name('auto_http_ip')
    elem.clear()
    elem.send_keys(aps_server)
    elem = browser.find_element_by_name('auto_http_port')
    elem.clear()
    elem.send_keys(aps_port)
    elem = browser.find_element_by_name('bntSubmit')
    elem.click()  
    # 重啟
    browser.get(page_restart)
    elem = browser.find_element_by_name('upBtn')
    elem.click()

# 連線資料庫
conn = sqlite3.connect('daps.db')
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
ip_list = c.execute("SELECT ip FROM voip").fetchall()
# 開瀏覽器
browser = webdriver.Firefox()
# 開工囉
for ip in ip_list:
    print(ip)
    set_aps(ip)

