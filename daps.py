#!/usr/bin/env python3
import sqlite3

# APS 為放置 txt 檔的 URL ex: aps.kerker.edu.tw
APS = ''

# 以下為指派靜態 IP 所需的網路資訊
NETMASK = ''
GATEWAY = ''
DNS = ''

with open('template.tpl','r') as f:
    data = f.readlines()

conn = sqlite3.connect('daps.db')
c = conn.cursor()
cursor = c.execute("SELECT mac, ip, sip01, usr01, pwd01, sip02, usr02, pwd02 FROM voip")
for row in cursor:
    MAC = row[0]
    IPADDR = row[1]
    SIP01 = row[2]
    USR01 = row[3]
    PWD01 = row[4]
    SIP02 = row[5]
    USR02 = row[6]
    PWD02 = row[7]
    ofn = MAC + '.txt'
    with open(ofn,'w') as f:
        for line in data:
            line = line.replace('%aps', APS)
            line = line.replace('%ipaddr', IPADDR)
            line = line.replace('%netmask', NETMASK)
            line = line.replace('%gateway', GATEWAY)
            line = line.replace('%dns', DNS)
            line = line.replace('%sip01', SIP01)
            line = line.replace('%usr01', USR01)
            line = line.replace('%pwd01', PWD01)
            line = line.replace('%sip02', SIP02)
            line = line.replace('%usr02', USR02)
            line = line.replace('%pwd02', PWD02)
            f.write(line)
