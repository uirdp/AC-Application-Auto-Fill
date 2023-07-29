#空調申請の日付を書き換えるプログラム

import datetime
import CreateFirstForm
import CreateNewForm
from odf import opendocument, text , teletype


def convert_to_bool(ans):
    if ans == 'yes' : return True
    else : return False

#--------------------------------------------------------------------------

start_month  = int(input('新しい申請書の初日の月 > '))
start_day = int(input('新しい申請書の初日の日 > '))

prev_month = int(input('書き換え元の申請書の初日の月 > '))
prev_day = int(input('書き換え元の申請書の初日の日 > '))

ans = input('元の申請書にアンダースコアは引かれてますか？ (yes/no) > ').lower()
is_underscored = convert_to_bool(ans)

start_date = datetime.datetime(2023, start_month, start_day)
prev_date = datetime.datetime(2023, prev_month, prev_day)

print('start: ', start_date)
print('prev: ', prev_date)

if(is_underscored) : 
     shinsei = CreateNewForm.CreateNewForm()
     shinsei.create_new_form(start_date, prev_date)

else : 
     shinsei = CreateFirstForm.CreateFirstForm()
     shinsei.create_new_form(start_date, prev_date)

#かならず一個くらい間違ってるところがある、なんでだろう・・・
print('書き出しが完了しました、当該ファイルを確認、修正してください')

