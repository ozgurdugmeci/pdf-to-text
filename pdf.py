import random
import os
from os import path
from io import BytesIO
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


d="C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\pdf2"
all=0
sta=0
ahh=[]

# PDFMiner boilerplate
rsrcmgr = PDFResourceManager()



for root, dirs, files in os.walk("C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\pdf2"):
 for file in files:
  if file.endswith('.pdf'):
   all=all+1
   print(file)
   path='C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\pdf2\\'+ file
   print(path)
   sio = StringIO()
   codec = 'utf-8'
   laparams = LAParams()
   device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
   interpreter = PDFPageInterpreter(rsrcmgr, device)
   fp = open('C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\pdf2\\'+file, 'rb')
   for page in PDFPage.get_pages(fp):
    interpreter.process_page(page)
   fp.close()
   text = sio.getvalue()
   text=text.replace(chr(272),"i")
   text=text.replace(chr(729)," ")
   text=text.replace(chr(288),"ğ")
   text=text.replace(chr(290),"ç")
   text=text.replace("İ","i")
   print(type(text))
    
   file=file.replace(".pdf",".txt")
   t = open('C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\txt2\\'+file,'w')
   t.write(text)
   
   t.close() 
   
