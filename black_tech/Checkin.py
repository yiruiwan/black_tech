#coding:utf-8
from selenium import webdriver
import random
import time,datetime

#配置时间区间
st = "08:40:30"
et = "08:45:50"

def time2seconds(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def seconds2time(sec):
    m,s = divmod(sec,60)
    h,m = divmod(m,60)
    return "%02d:%02d:%02d" % (h,m,s)

sts = time2seconds(st) #sts==27000
ets = time2seconds(et) #ets==34233

rt = random.sample(range(sts,ets),10)

def random_time():
    for r in rt:
        return (seconds2time(r))
random_time()
nowdate = datetime.datetime.now().strftime('%Y-%m-%d')
Checkin_time = nowdate + ' ' +str(random_time())


# #时间配置
# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)
# Checkin_time = str(tomorrow) + ' 09:00:00'  # 修改签到的时间

def Login_tc(Username,Password): #登录
    gg.find_element_by_xpath('//*[@id="username"]').send_keys(Username)
    gg.find_element_by_xpath('//*[@id="password_input"]').send_keys(Password)
    gg.find_element_by_xpath('//*[@id="login_button"]').click()

def Check_in(): #签入
    Checkin_btn = gg.find_element_by_xpath('//*[@id="checkin_btn"]')
    Checkin_btn.click()
    time.sleep(5)
    Confirm_btn1 = gg.find_element_by_xpath('//*[@id="tdialog-buttonwrap"]/a[1]/span')
    Confirm_btn1.click()
    gg.quit()


def logout(): # 注销
    out_elemet = gg.find_element_by_xpath('// *[ @ id = "user_infor"] / div[3] / a').click()


def checkout():
    datas = [("v_yiruiwan", "A1191190a"),]
    for i in range(0, len(datas)):
        gg.implicitly_wait(10)
        gg.maximize_window()
        gg.get(r'http://om.tencent.com/attendances/check_out/5101691?from=TAPD')
        Login_tc(datas[i][0],datas[i][1])
        time.sleep(3)
        Check_in()
        time.sleep(3)
        logout()
        gg.refresh()


if __name__ == '__main__':
    while 1:
        # str(datetime.datetime.now())[0:19]
        now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(Checkin_time, ' ', now_str)
        if now_str == Checkin_time:
            print(Checkin_time, ' ', now_str)
            gg = webdriver.Chrome()
            checkout()
            break
        else:
            print('sleep 1s')
            time.sleep(1)
