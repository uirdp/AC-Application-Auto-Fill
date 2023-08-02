#空調申請の日付を書き換えるプログラム

import datetime
import Form_Generator

#-------------------------------------------------------------------------
START_YEAR = 2023
FINAL_MONTH = 10 #申請期間終了の月

start_month  = int(input('新しい申請書の初日の月 > '))
start_day = int(input('新しい申請書の初日の日 > '))

docname = input('書き換え元ファイルの名前 > ')

start_date = datetime.datetime(START_YEAR, start_month, start_day)
shinsei = Form_Generator.Form_Generator(docname)

while True:
     
     shinsei.create_new_form(start_date) 

     prev_date = start_date
     start_date += datetime.timedelta(days = 14)

     if(start_date.month == FINAL_MONTH): break


#かならず一個くらい間違ってるところがある、なんでだろう・・・
print('おわりー、ちゃんと確認してから提出してね')

