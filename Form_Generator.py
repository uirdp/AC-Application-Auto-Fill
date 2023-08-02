import datetime
import locale
from odf import opendocument, text , teletype

#空調申請書を作成します
class Form_Generator:

    def  __init__(self, docname):
      
      self.docname = docname

    def replace_old_dates(self, texts, start_date):
       
       locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
       
       #申請書の最初の１３日分を書き換える
       for elapsed_days in range(13):

            new_date = start_date + datetime.timedelta(days = elapsed_days)
            old_text = teletype.extractText(texts[134])

            print('old: ', old_text)
            new_text = old_text.replace(old_text, str(new_date.month)+ '______'+str(new_date.day)+'____' + new_date.strftime('%a'))
            print('new: ', new_text)

            new_S = text.P()
            new_S.setAttribute("stylename",texts[134].getAttribute("stylename"))
            new_S.addText(new_text)

            texts[134].parentNode.insertBefore(new_S,texts[134])
            texts[134].parentNode.removeChild(texts[134])

    #上の処理だけだと最後の行だけ置換できない（最後だけ行のインデックスが134から135に変わってるみたい）
    def replace_last_line(self, texts, start_date):
        
        old_text = teletype.extractText(texts[135])
        print('old: ', old_text)

        new_date = start_date + datetime.timedelta(days = 13)        
        new_text = old_text.replace(old_text, str(new_date.month)+ '______'+str(new_date.day)+'____' + new_date.strftime('%a'))
        print('new: ', new_text)

        new_S = text.P()
        new_S.setAttribute("stylename",texts[135].getAttribute("stylename"))
        new_S.addText(new_text)

        texts[135].parentNode.insertBefore(new_S,texts[135])
        texts[135].parentNode.removeChild(texts[135])


    def create_new_form(self, start_date):
        
        document = opendocument.load(self.docname) 
        texts = document.getElementsByType(text.P)
    
        self.replace_old_dates(texts, start_date)
        self.replace_last_line(texts, start_date)

        document.save('shinsei'+str(start_date.date())+'.odt')
       