from django.shortcuts import render, HttpResponse
import requests


# def index(request):
#     text = "To be or not to be"
#     # if request.method == 'POST':
#     #     text = request.POST['text']
#     url = "https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCVx4jHICEs3Dt8VYlxupTeibnYhBziBkU"
#     response = requests.get(url.format(text)).json()
        
#     book_detail = {
#                 "book_name" : response['items'][0]['volumeInfo']['title'],
#                 "author_name" : response['items'][0]['volumeInfo']['authors'],
#                 "book_description" : response['items'][0]['volumeInfo']['description']
#             }
        

#     context = {"book_detail" : book_detail}

#     return render(request, "bookDetect.html", context)



def index(request):
    query = ""
    query2= ""
    book_detail = {}
    context = {}
    if request.method=='POST':
        query = request.POST['queryspeech']
        query2 = request.POST['query']
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
                book_detail = {
                        "book_name" : response['items'][0]['volumeInfo']['title'],
                        "author_name" : response['items'][0]['volumeInfo']['authors'],
                        "book_description" : response['items'][0]['volumeInfo']['description'],
                        "book_img" : response['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']
                }
            
            return book_detail

