import datetime
from odf import opendocument, text , teletype

#初めて使う時用、アンダースコアを引いて位置を調整します
class CreateFirstForm:

    def  __init__(self):
      
      print('class ', self.__class__.__name__, 'instanciated')

    def replace_old_dates(self, texts, start_date, prev_date):
       
       for elapsed_days in range(14):
            old_date = prev_date + datetime.timedelta(days=elapsed_days)
            new_date = start_date + datetime.timedelta(days = elapsed_days)
   
            print('old: ', old_date)
            print('new: ', new_date)


            old_text = teletype.extractText(texts[134])
            new_text = old_text.replace(str(old_date.month), str(new_date.month))
            new_text = new_text.replace(str(old_date.day), '______'+str(new_date.day)+'____')
 
            print('old: ', old_text)
            print('new: ', new_text)
       
            new_S = text.P()
            new_S.setAttribute("stylename",texts[134].getAttribute("stylename"))
            new_S.addText(new_text)

            texts[134].parentNode.insertBefore(new_S,texts[134])
            texts[134].parentNode.removeChild(texts[134])

    #上の処理だけだとなぜか最後の行だけ置換できない（なぞ・・・）
    def replace_last_line(texts, start_date, prev_date):

        old_date = prev_date + datetime.timedelta(days=13)
        new_date = start_date + datetime.timedelta(days = 13)
   
        print('old: ', old_date)
        print('new: ', new_date)


        old_text = teletype.extractText(texts[134])
        new_text = old_text.replace(str(old_date.month), str(new_date.month))
        new_text = new_text.replace(str(old_date.day), '______'+str(new_date.day)+'___')
 
        new_S = text.P()
        new_S.setAttribute("stylename",texts[134].getAttribute("stylename"))
        new_S.addText(new_text)

        texts[134].parentNode.insertBefore(new_S,texts[134])
        texts[134].parentNode.removeChild(texts[134])


    def create_new_form(self, start_date, prev_date):
        docname = input('書き換え元ファイルの名前 > ')
        document = opendocument.load(docname) 
        texts = document.getElementsByType(text.P)
    
        self.replace_old_dates(texts, start_date, prev_date)
        self.replace_last_line(texts, start_date, prev_date)

        document.save('shinsei'+str(start_date.date())+'.odt')
       