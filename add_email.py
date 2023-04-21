import pandas as pd
import requests
from bs4 import BeautifulSoup

url="https://site?page=user_list"
headers={'Cookie':'PHPSESSID=--'}


while(1):
    #connect url
    html=requests.get(url,headers=headers)
    bs_html=BeautifulSoup(html.content,"html.parser")

    #csv파일에서 (가장 마지막 uniqnum + 1) 값 가져옴
    df = pd.read_csv('account.csv',sep=',',header=0)
    u_num = str(df.iloc[-1]["Uniq Num"]+1)

    #웹에서 새로 추가된 이메일,uniqnum찾아서 csv파일에 추가 
    get_class=bs_html.find("div",{"class":"card-body"})
    onclick=f"window.location.href='?p=user_modify&i={u_num}';"
    if u_num in get_class.get_text():
        tr=get_class.select_one(f'tr[onclick="{onclick}"]')
        td=tr.select("td")[2].get_text()
        df.loc[len(df)]=[u_num,str(td)]
        df.to_csv('account.csv', index=False)
        print(f"USER SIGNED===================================\nUniq Num:{u_num}\nE-mail:{td}\n==============================================")
