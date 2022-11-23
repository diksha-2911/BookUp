from django.shortcuts import render, HttpResponse
from .models import Search
import requests
import cv2
import numpy as np
import os
import pytesseract



def index(request):
    query = ""
    query2= ""
    book_detail = {}
    context = {}
    book = Search()
    if request.method=='POST':
        query = request.POST.get('queryspeech', "")
        query2 = request.POST['query']
        if(len(request.FILES)!=0):
            book.image = request.FILES["image"]
        
            book.save()
            file = str(book.image)
            # print(file)
            file = file.replace("/", "\\\\")
            file = "media\\" + file

            # filepath = "\"" + file + "\""
            # print(filepath)
            pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
            img = cv2.imread(file)#will change this so photos can be user input
            img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img2=img.copy()
            kernel = np.ones((1, 1), np.uint8)
            img = cv2.dilate(img, kernel, iterations=1)
            img = cv2.erode(img, kernel, iterations=1)
            img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            hi,wi=img2.shape
            box=pytesseract.image_to_boxes(img)
            #rectangles are made here which is not important
            for b in box.splitlines():
                b=b.split(" ")
            #     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
            #     cv2.rectangle(img2,(x,hi-y),(w,hi-h),(0,255,0),2)
            # cv2.imshow('Frame',img2)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            #junk clearing from text found
            txt = pytesseract.image_to_string(img, lang='eng')
            txt = txt[:-1]
            txt = txt.replace('\n', ' ')
            if len(txt)<=10:
                main_query_final=txt
            else:
                main_query=txt.split(".")
            main_query_final=main_query[0]+main_query[1]
            #main_query=main_query[1][2::]
            context = detail(main_query_final)

        
        if(query != ""):
            print(query)
            context = detail(query)

        elif(query2 != ""):
            print(query2)
            context = detail(query2)

        
    
    # context = {"book_detail" : book_detail}
     
    return render(request, 'BookDetect.html', {"book_detail" : context})


def detail(query):
            book_detail = {}
            if query != "":
                url = "https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCVx4jHICEs3Dt8VYlxupTeibnYhBziBkU"
                response = requests.get(url.format(query)).json()
                # print(response['items'][0]['volumeInfo']['title'])
                for i in range(1):
                    book_detail = {
                        'book_data' : [
                            {"book_name" : response['items'][0]['volumeInfo']['title'],
                            "author_name" : response['items'][0]['volumeInfo']['authors'],
                            "book_description" : response['items'][0]['volumeInfo']['description'],
                            "book_img" : response['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']}
                        ]
                    }
                    print(book_detail['book_data'])
            
                    

            
            return book_detail

