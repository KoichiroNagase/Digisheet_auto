import streamlit as st   # webアプリ開発のためのライブラリ
import time
import calendar
import datetime
import locale  # 曜日を表示するのに使用する（日本語曜日表記のため）
import webbrowser
import pyautogui   # GUI自動化ライブラリ
import sys   # インタプリタや実行環境を管理・操作するための標準ライブラリ
import pyperclip   # クリップボードに文字列をコピーしたり、クリップボードの文字列を取得することができるライブラリ
import os

value = os.getenv("TEST", "defaultvalue")

# 前準備----------------------------------------------------------------
today = datetime.date.today()   # 今日の日付を取得
this_Year = today.year   # 今日の日付から年だけを取得
this_Month = today.month   # 今日の日付から月だけを取得

days_Of_Month = calendar.monthrange(this_Year, this_Month)[1]   # 今月の日数を取得

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')   # 曜日の日本語表記するためのおまじない

end_Hours = []   # 勤務開始時間のプルダウン用リスト（streamlitでの用）
for i in range(2, 24):
    end_Hours.append(i)

minutes = ['00', '05', '10', '15', '20',
           '25', '30', '35', '40', '45', '50', '55']   # 分のプルダウン用リスト（streamlitでの用）

url = 'https://vsn.digisheet.com/staffLogin'   # DigisheetのURL


def login(COMPANY_ID, staff_ID, passWord):   # digisheetログインの関数
    time.sleep(1)
    pyautogui.hotkey("command", "Ctrl", "f")   # ★★★★★★★★★★★画面最大化(Macのみ)
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.typewrite(COMPANY_ID)
    time.sleep(0.5)
    pyautogui.press("tab")
    pyautogui.typewrite(staff_ID)
    time.sleep(0.5)
    pyautogui.press("tab")
    pyautogui.typewrite(passWord)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    if pyautogui.locateOnScreen('./img/icon.png', confidence=0.5):
        pass
    else:
        pyautogui.hotkey("command", "Ctrl", "f")   # ★★★★★★★★★★★画面最大化解除(Macのみ)
        sys.exit()


def kinmu_Houkoku():   # 勤務報告ボタンをクリックする関数
    time.sleep(0.5)
    i = 0
    for i in range(2):
        pyautogui.press("tab")
        i = i + 1
    pyautogui.press("enter")
    time.sleep(0.5)


def start_Hour_Left():   # digisheetで勤務開始時間（時間）を入力するための準備関数（十の位）（pyautoguiで一文字ずつ入力するため数字を2つに分解）
    if start_Hour < 10:
        start_Hour_Left = ''
    elif start_Hour >= 11 and start_Hour < 20:
        start_Hour_Left = '1'
    elif start_Hour > 20:
        start_Hour_Left = '2'
    return start_Hour_Left


def start_Hour_Right():   # digisheetで勤務開始時間（時間）を入力するための準備関数（一の位）（pyautoguiで一文字ずつ入力するため数字を2つに分解）
    if start_Hour == 0 or start_Hour == 10 or start_Hour == 20:
        start_Hour_Right = '0'
    elif start_Hour == 1 or start_Hour == 11 or start_Hour == 21:
        start_Hour_Right = '1'
    elif start_Hour == 2 or start_Hour == 12 or start_Hour == 22:
        start_Hour_Right = '2'
    elif start_Hour == 3 or start_Hour == 13 or start_Hour == 23:
        start_Hour_Right = '3'
    elif start_Hour == 4 or start_Hour == 14:
        start_Hour_Right = '4'
    elif start_Hour == 5 or start_Hour == 15:
        start_Hour_Right = '5'
    elif start_Hour == 6 or start_Hour == 16:
        start_Hour_Right = '6'
    elif start_Hour == 7 or start_Hour == 17:
        start_Hour_Right = '7'
    elif start_Hour == 8 or start_Hour == 18:
        start_Hour_Right = '8'
    elif start_Hour == 9 or start_Hour == 19:
        start_Hour_Right = '9'
    return start_Hour_Right


def start_Minute_Left():   # digisheetで勤務開始時間（分）を入力するための準備関数（十の位）（pyautoguiで一文字ずつ入力するため数字を2つに分解）
    if start_Minute == '00':
        start_Minute_Left = ''
    elif start_Minute == '05':
        start_Minute_Left = '0'
    elif start_Minute == '10' or start_Minute == '15':
        start_Minute_Left = '1'
    elif start_Minute == '20' or start_Minute == '25':
        start_Minute_Left = '2'
    elif start_Minute == '30' or start_Minute == '35':
        start_Minute_Left = '3'
    elif start_Minute == '40' or start_Minute == '45':
        start_Minute_Left = '4'
    elif start_Minute == '50' or start_Minute == '55':
        start_Minute_Left = '5'
    return start_Minute_Left


def start_Minute_Right():   # digisheetで勤務開始時間（分）を入力するための準備関数（一の位）（pyautoguiで一文字ずつ入力するため数字を2つに分解）
    if start_Minute == '00' or start_Minute == '10' or start_Minute == '20' or start_Minute == '30' or start_Minute == '40' or start_Minute == '50':
        start_Minute_Right = '0'
    elif start_Minute == '05' or start_Minute == '15' or start_Minute == '25' or start_Minute == '35' or start_Minute == '45' or start_Minute == '55':
        start_Minute_Right = '5'
    return start_Minute_Right


def end_Hour_Left():   # digisheetで勤務終了時間（時間）を入力するための準備関数（十の位）（pyautoguiで一文字ずつ入力するため数字を2つに分解）
    if end_Hour < 10:
        end_Hour_Left = ''
    elif end_Hour >= 11 and end_Hour < 20:
        end_Hour_Left = '1'
    elif end_Hour > 20:
        end_Hour_Left = '2'
    return end_Hour_Left


def end_Hour_Right():   # digisheetで勤務終了時間（時間）を入力するための準備関数（一の位）（pyautoguiで一文字ずつ入力するため数字を2つに分解）
    if end_Hour == 0 or end_Hour == 10 or end_Hour == 20:
        end_Hour_Right = '0'
    elif end_Hour == 1 or end_Hour == 11 or end_Hour == 21:
        end_Hour_Right = '1'
    elif end_Hour == 2 or end_Hour == 12 or end_Hour == 22:
        end_Hour_Right = '2'
    elif end_Hour == 3 or end_Hour == 13 or end_Hour == 23:
        end_Hour_Right = '3'
    elif end_Hour == 4 or end_Hour == 14:
        end_Hour_Right = '4'
    elif end_Hour == 5 or end_Hour == 15:
        end_Hour_Right = '5'
    elif end_Hour == 6 or end_Hour == 16:
        end_Hour_Right = '6'
    elif end_Hour == 7 or end_Hour == 17:
        end_Hour_Right = '7'
    elif end_Hour == 8 or end_Hour == 18:
        end_Hour_Right = '8'
    elif end_Hour == 9 or end_Hour == 19:
        end_Hour_Right = '9'
    return end_Hour_Right


def end_Minute_Left():   # digisheetで勤務終了時間（分）を入力するための準備関数（十の位）（pyautoguiで一文字ずつ入力するため数字を2つに分解）
    if end_Minute == '00':
        end_Minute_Left = ''
    elif end_Minute == '05':
        end_Minute_Left = '0'
    elif end_Minute == '10' or end_Minute == '15':
        end_Minute_Left = '1'
    elif end_Minute == '20' or end_Minute == '25':
        end_Minute_Left = '2'
    elif end_Minute == '30' or end_Minute == '35':
        end_Minute_Left = '3'
    elif end_Minute == '40' or end_Minute == '45':
        end_Minute_Left = '4'
    elif end_Minute == '50' or end_Minute == '55':
        end_Minute_Left = '5'
    return end_Minute_Left


def end_Minute_Right():   # digisheetで勤務終了時間（分）を入力するための準備関数（一の位）（pyautoguiで一文字ずつ入力するため数字を2つに分解）
    if end_Minute == '00' or end_Minute == '10' or end_Minute == '20' or end_Minute == '30' or end_Minute == '40' or end_Minute == '50':
        end_Minute_Right = '0'
    elif end_Minute == '05' or end_Minute == '15' or end_Minute == '25' or end_Minute == '35' or end_Minute == '45' or end_Minute == '55':
        end_Minute_Right = '5'
    return end_Minute_Right


def input_Worktime():   # digisheetで勤務時間を実際に入力するための関数
    i = 0
    for i in range(5):
        pyautogui.press("tab")
        i = i + 1
    pyautogui.press(start_Hour_Left())
    pyautogui.press(start_Hour_Right())
    time.sleep(0.2)
    pyautogui.press("tab")
    pyautogui.press(start_Minute_Left())
    pyautogui.press(start_Minute_Right())
    time.sleep(0.2)
    pyautogui.press("tab")
    pyautogui.press(end_Hour_Left())
    pyautogui.press(end_Hour_Right())
    time.sleep(0.2)
    pyautogui.press("tab")
    pyautogui.press(end_Minute_Left())
    pyautogui.press(end_Minute_Right())
    time.sleep(0.2)


def input_Zaitaku():   # 在宅勤務の場合にdigisheetで処理させるための関数
    j = 0
    for j in range(5):
        pyautogui.press("tab")
        j = j + 1
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.press("tab")
    pyperclip.copy("在宅勤務")   # ★★★★★★★★★★★他のプロジェクトのチームは必要ない？
    # ★★★★★★★★★★★WindowsOSは記述を変更する必要あり
    pyautogui.hotkey("command", "v")
    time.sleep(0.2)
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)


def input_Shukkin():   # 在宅勤務ではない場合にdigisheetで処理させるための関数
    j = 0
    for j in range(8):
        pyautogui.press("tab")
        j = j + 1
    pyautogui.press("enter")
    time.sleep(1)


def holiday_Cancel():   # 土日祝日などで勤務時間を入力する必要がない日の場合に実行する関数
    x, y = pyautogui.locateCenterOnScreen(
        './img/cancel.png', confidence=0.8)
    pyautogui.click(x, y)
    time.sleep(1)


def day_1():   # 1日を処理する関数
    pyautogui.scroll(-7)
    x, y = pyautogui.locateCenterOnScreen('./img/day_1.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[1] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_2():   # 2日を処理する関数
    pyautogui.scroll(-8)
    x, y = pyautogui.locateCenterOnScreen('./img/day_2.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[2] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_3():   # 3日を処理する関数
    pyautogui.scroll(-9)
    x, y = pyautogui.locateCenterOnScreen('./img/day_3.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[3] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_4():   # 4日を処理する関数
    pyautogui.scroll(-10)
    x, y = pyautogui.locateCenterOnScreen('./img/day_4.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[4] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_5():   # 5日を処理する関数
    pyautogui.scroll(-11)
    x, y = pyautogui.locateCenterOnScreen('./img/day_5.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[5] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_6():   # 6日を処理する関数
    pyautogui.scroll(-12)
    x, y = pyautogui.locateCenterOnScreen('./img/day_6.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[6] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_7():   # 7日を処理する関数
    pyautogui.scroll(-13)
    x, y = pyautogui.locateCenterOnScreen('./img/day_7.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[7] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_8():   # 8日を処理する関数
    pyautogui.scroll(-14)
    x, y = pyautogui.locateCenterOnScreen('./img/day_8.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[8] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_9():   # 9日を処理する関数
    pyautogui.scroll(-15)
    x, y = pyautogui.locateCenterOnScreen('./img/day_9.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[9] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_10():   # 10日を処理する関数
    pyautogui.scroll(-16)
    x, y = pyautogui.locateCenterOnScreen('./img/day_10.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[10] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_11():   # 11日を処理する関数
    pyautogui.scroll(-17)
    x, y = pyautogui.locateCenterOnScreen('./img/day_11.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[11] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_12():   # 12日を処理する関数
    pyautogui.scroll(-18)
    x, y = pyautogui.locateCenterOnScreen('./img/day_12.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[12] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_13():   # 13日を処理する関数
    pyautogui.scroll(-19)
    x, y = pyautogui.locateCenterOnScreen('./img/day_13.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[13] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_14():   # 14日を処理する関数
    pyautogui.scroll(-20)
    x, y = pyautogui.locateCenterOnScreen('./img/day_14.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[14] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_15():   # 15日を処理する関数
    pyautogui.scroll(-21)
    x, y = pyautogui.locateCenterOnScreen('./img/day_15.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[15] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_16():   # 16日を処理する関数
    pyautogui.scroll(-22)
    x, y = pyautogui.locateCenterOnScreen('./img/day_16.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[16] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_17():   # 17日を処理する関数
    pyautogui.scroll(-23)
    x, y = pyautogui.locateCenterOnScreen('./img/day_17.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[17] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_18():   # 18日を処理する関数
    pyautogui.scroll(-24)
    x, y = pyautogui.locateCenterOnScreen('./img/day_18.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[18] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_19():   # 19日を処理する関数
    pyautogui.scroll(-25)
    x, y = pyautogui.locateCenterOnScreen('./img/day_19.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[19] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_20():   # 20日を処理する関数
    pyautogui.scroll(-26)
    x, y = pyautogui.locateCenterOnScreen('./img/day_20.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[20] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_21():   # 21日を処理する関数
    pyautogui.scroll(-27)
    x, y = pyautogui.locateCenterOnScreen('./img/day_21.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[21] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_22():   # 22日を処理する関数
    pyautogui.scroll(-28)
    x, y = pyautogui.locateCenterOnScreen('./img/day_22.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[22] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_23():   # 23日を処理する関数
    pyautogui.scroll(-29)
    x, y = pyautogui.locateCenterOnScreen('./img/day_23.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[23] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_24():   # 24日を処理する関数
    pyautogui.scroll(-30)
    x, y = pyautogui.locateCenterOnScreen('./img/day_24.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[24] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_25():   # 25日を処理する関数
    pyautogui.scroll(-31)
    x, y = pyautogui.locateCenterOnScreen('./img/day_25.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[25] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_26():   # 26日を処理する関数
    pyautogui.scroll(-32)
    x, y = pyautogui.locateCenterOnScreen('./img/day_26.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[26] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_27():   # 27日を処理する関数
    pyautogui.scroll(-33)
    x, y = pyautogui.locateCenterOnScreen('./img/day_27.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[27] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_28():   # 28日を処理する関数
    pyautogui.scroll(-34)
    x, y = pyautogui.locateCenterOnScreen('./img/day_28.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[28] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_29():   # 29日を処理する関数
    pyautogui.scroll(-35)
    x, y = pyautogui.locateCenterOnScreen('./img/day_29.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[29] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_30():   # 30日を処理する関数
    pyautogui.scroll(-36)
    x, y = pyautogui.locateCenterOnScreen('./img/day_30.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[30] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


def day_31():   # 31日を処理する関数
    pyautogui.scroll(-37)
    x, y = pyautogui.locateCenterOnScreen('./img/day_31.png', confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/shigyo_shugyo.png', confidence=0.8):
        input_Worktime()
        if zaitaku_Flag[31] == True:
            input_Zaitaku()
        else:
            input_Shukkin()
    else:
        holiday_Cancel()


days_list = [day_1, day_2, day_3, day_4, day_5,
             day_6, day_7, day_8, day_9, day_10, day_11, day_12, day_13, day_14, day_15, day_16, day_17, day_18, day_19, day_20, day_21, day_22, day_23, day_24, day_25, day_26, day_27, day_28, day_29, day_30, day_31]
# -----------------------------------streamlit画面 start---------------------------------------
st.title('Digisheet簡易入力アプリ')

COMPANY_ID = '7008'
staff_ID = st.text_input('スタッフID')
passWord = st.text_input('パスワード', type='password')

if staff_ID == '' or passWord == '':
    st.markdown(":red[スタッフIDとパスワードを入力してください]")
    iD_PassWord_Flag = 0
else:
    iD_PassWord_Flag = 1

st.write(f"""
    ---------------------------------------
    ##### 処理日付指定（{this_Year}年{this_Month}月）
    """)
day_Min, day_Max = st.slider(
    # 処理対象日付
    'Digisheetで処理したい日付の範囲指定してください',
    1, days_Of_Month, (1, days_Of_Month)
)

days = []   # 処理日付指定スライドバーで設定された日をリストに格納
for i in range(day_Min, day_Max+1):
    days.append(i)

st.write(f"""
    ##### 選択日 :  {day_Min}日〜{day_Max}日
""")

st.write("""
    ---------------------------------------
    ##### 勤務時間指定
    """)

time_Col1, time_Col2, time_Col3, time_Col4 = st.columns(
    (2, 2, 2, 2))   # 勤務時間のセレクトボックスのレイアウト設定
with time_Col3:
    end_Hour = st.selectbox(
        '勤務終了時間',
        end_Hours, 16)
with time_Col4:
    end_Minute = st.selectbox(
        '終了分',
        minutes, 0)

start_Hours = []
for i in range(0, 22):
    start_Hours.append(i)

with time_Col1:
    start_Hour = st.selectbox(
        '勤務開始時間',
        start_Hours, 9)
with time_Col2:
    start_Minute = st.selectbox(
        '開始分',
        minutes, 4)

st.write(f"""
    ##### 選択時間 :  {start_Hour}:{start_Minute}〜{end_Hour}:{end_Minute}
""")

if start_Hour > end_Hour-2:
    hour_Check_Flag = 0
    st.markdown(":red[勤務開始時間は勤務終了時間より1時間以上前に設定してください]")
else:
    hour_Check_Flag = 1

# -----------------------------------サイドバー start （在宅チェック）---------------------------------------
st.sidebar.write("""
    ### 在宅勤務チェック
    在宅勤務をした日にはチェックを入れてください
    """)

# 在宅チェックボックスでそれぞれの日がチェックされているかのboolを辞書型で格納する
# 処理日付指定スライドバーで設定された日数分チェックボックスは表示される
zaitaku_Flag = {}
for i in range(day_Min, day_Max+1):
    date = datetime.date(this_Year, this_Month, i)
    day = date.strftime('%a')   # 曜日を日本語で取得
    zaitaku_Flag[i] = st.sidebar.checkbox(f"{this_Month}/{i} （{day}）")
# -----------------------------------サイドバー end （在宅チェック）---------------------------------------

st.write("""
    ---------------------------------------
    """)

if hour_Check_Flag == 1 and iD_PassWord_Flag == 1:
    if st.button('処理開始'):
        webbrowser.open_new_tab(url)
        login(COMPANY_ID, staff_ID, passWord)   # digisheetログインの関数の実行
        kinmu_Houkoku()   # 勤務報告ボタンをクリックする関数の実行
        for i in range(day_Min-1, day_Max):
            days_list[i]()
            i = i + 1
        # ★★★★★★★★★★★画面最大化解除(Macのみ)
        pyautogui.hotkey("command", "Ctrl", "f")
