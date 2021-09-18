import requests
import time

def sleep(n_secs):
    time.sleep(n_secs)

def login_cookies():
    url="http://121.42.15.146:9090/mtx/index.php?s=/index/buy/add.html"
    data={
        "accounts":"yaoyao",
        "pwd" :"yaoyao"
    }
    headers = {"X-Requested-With":"XMLHttpRequest"}
    resp=requests.post(url,data=data,headers=headers)
    r=resp.json()
    return r

if __name__ == '__main__':
    print(login_cookies())