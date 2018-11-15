# D-link DPH-150SE Auto Provisioning

## 環境需求

* python 3
* selenium (如果有需要用機器人)

## 建立資料庫

請先依照 daps.sqlite.schema 建立資料庫 daps.db

```
sqlite3 daps.db < daps.sqlite.schema
```

這個資料庫裡面只有一個 voip 資料表，包含以下欄位

| 欄位名稱 | 意義                     | 範例              |
| -------- | ------------------------ | ----------------- |
| mac      | 話機的網卡卡號，連續大寫 | AABBCCDDEEFF      |
| ip       | 話機的固定 IP            | 192.168.123.123   |
| sip01    | 第一個 sip 伺服器        | sip.kerker.edu.tw |
| usr01    | 第一個 sip 帳號          | 99101             |
| pwd01    | 第一個 sip 密碼          | 99101             |
| sip02    | 第二個 sip 伺服器        | 192.168.8.8       |
| usr02    | 第二個 sip 帳號          | 101               |
| pwd02    | 第二個 sip 密碼          | 101pwd            |

如需使用 csv 匯入可依照 daps.sample.csv 範例另存為 daps.csv 然後執行

```
sqlite3 daps.db < daps.import.sql
```

## 建立話機 profile

修改 daps.py 

```
APS = '設定為你 aps server 位置'
NETMASK = '設定話機的網路遮罩'
GATEWAY = '設定話機的網路閘道'
DNS = '設定話機的 DNS server'
# 話機 IP 則抓取資料庫的對應
```

使用方式

```
python daps.py
```

然後就會生出一大堆 .txt

把這堆丟去 APS server ( 其實就是一台 web server ) 上讓話機上來可以抓到自己的 profile 就好

## 大量修改話機 APS

dbot.py 為一個 python 機器人

作用就是依照 daps.db 內的 IP 位置，開瀏覽器幫你一台一台修改 APS 然後重開機

使用方法

```
python dbot.py
```

