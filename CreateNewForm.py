import datetime
import locale
from odf import opendocument, text , teletype

class CreateNewForm:
    
    def  __init__(self):
      
         print('class ', self.__class__.__name__, 'instanciated')

    def replace_old_dates(self, texts, start_date, prev_date):
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

        for elapsed_days in range(14):
            old_date = prev_date + datetime.timedelta(days=elapsed_days)
            new_date = start_date + datetime.timedelta(days = elapsed_days)
   
            print('old: ', old_date)
            print('new: ', new_date)


            old_text = teletype.extractText(texts[134])
            new_text = old_text.replace(old_text, str(new_date.month)+str(new_date.day)+ new_date.strftime('%a'))
 
            new_S = text.P()
            new_S.setAttribute("stylename",texts[134].getAttribute("stylename"))
            new_S.addText(new_text)

            texts[134].parentNode.insertBefore(new_S,texts[134])
            texts[134].parentNode.removeChild(texts[134])


    def replace_last_line(self, texts, start_date, prev_date):


        old_text = teletype.extractText(texts[134])

        old_date = prev_date + datetime.timedelta(days=13)
        new_date = start_date + datetime.timedelta(days = 13)
   
        print('old: ', old_date)
        print('new: ', new_date)


        
        new_text = old_text.replace(old_text, str(new_date.month)+str(new_date.day)+ new_date.strftime('%a'))
 
        new_S = text.P()
        new_S.setAttribute("stylename",texts[134].getAttribute("stylename"))
        new_S.addText(new_text)

        texts[134].parentNode.insertBefore(new_S,texts[134])
        texts[134].parentNode.removeChild(texts[134])


    def create_new_form(self, start_date, prev_date):
        document = opendocument.load('shinsei'+str(prev_date.date())+'.odt') 
        texts = document.getElementsByType(text.P)
    
        self.replace_old_dates(texts, start_date, prev_date)
        self.replace_last_line(texts, start_date, prev_date)

        document.save('shinsei'+str(start_date.date())+'.odt')
