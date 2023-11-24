#空調申請の日付を書き換えるプログラム

import datetime
import Form_Generator
import PySimpleGUI as gui

#-------------------------------------------------------------------------
FINAL_MONTH = 3 #申請期間終了の月


def fill_form():
    
     start_year = int(values["start_year"])
     start_month = int(values["start_month"])
     start_day = int(values["start_day"])
     file_path = values["file_path"]

     print(file_path)

     try:
          start_date = datetime.datetime(start_year, start_month, start_day)
          shinsei = Form_Generator.Form_Generator(file_path)

 
          while True:
     
               shinsei.create_new_form(start_date) 
               start_date += datetime.timedelta(days = 14)

               if(start_date.month == FINAL_MONTH): break   
          
          print('おわりー、ちゃんと確認してから提出してね（閉じてください）')

     except:
        gui.PopupError('エラー発生が発生しました。処理を終了します。\r\n入力した値を確認してください。',
                      title='エラー', background_color='#f00' )
        window["start_year"].update("")
        window["start_month"].update("")
        window["start_day"].update("")
        window["file_path"].update("")


     #かならず一個くらい間違ってるところがある、なんでだろう・・・
    

#--------------------------------------------
#       GUI
#--------------------------------------------

gui.theme("DarkBlue")

col1 = [[gui.Text("年", size=(10,1), pad=((0,0),(10)))],
             [gui.Text("月", size=(10,1), pad=((0,0),(10)))],
             [gui.Text("日", size=(10,1), pad=((0,0),(10)))],
             [gui.Text("書き換え元", size=(10,1), pad=((0,0),(10)))]]

col2 = [[gui.InputText(size=(30,1), pad=((5),(10)), key="start_year")],
             [gui.InputText(size=(30,1), pad=((5),(10)), key="start_month")],
             [gui.InputText(size=(30,1), pad=((5),(10)), key="start_day")],
             [gui.InputText(size=(30,1), pad=((5),(10)), key="file_path")]]

layout = [[gui.Column(col1), gui.Column(col2)],          
                 [gui.Button("実行", size=(10,1), pad=((130),(10)), key="-change_exe-")]]

window = gui.Window("空調申請自動書き込み", layout, size=(360,230))


while True:
  event, values = window.read()
  
  print("イベント：",event , ', 値', values)
  if event == gui.WIN_CLOSED :
    break
  
  if event == "-change_exe-":
     fill_form()
    
window.close()