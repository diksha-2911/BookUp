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
    book_detail = {}
    if request.method=='POST':
        query = request.POST['query']
        print(query)
        url = "https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCVx4jHICEs3Dt8VYlxupTeibnYhBziBkU"
        response = requests.get(url.format(query)).json()
        # print(response['items'][0]['volumeInfo']['title'])
        book_detail = {
                "book_name" : response['items'][0]['volumeInfo']['title'],
                "author_name" : response['items'][0]['volumeInfo']['authors'],
                "book_description" : response['items'][0]['volumeInfo']['description'],
                "book_img" : response['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']
            }
        

    context = {"book_detail" : book_detail}
    return render(request, 'BookDetect.html', context)

