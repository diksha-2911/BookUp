from django.shortcuts import render, HttpResponse
import requests


# Create your views here.
# def index(request):
#     context = {
#         'variable' : "Homepage"
#     }
#     return render(request, 'bookDetect.html', context)
    # return HttpResponse("This is a Homepage")

def index(request):
    text = "To be or not to be"
    # if request.method == 'POST':
    #     text = request.POST['text']
    url = "https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCVx4jHICEs3Dt8VYlxupTeibnYhBziBkU"
    response = requests.get(url.format(text)).json()
        
    book_detail = {
                "book_name" : response['items'][0]['volumeInfo']['title'],
                "author_name" : response['items'][0]['volumeInfo']['authors'],
                "book_description" : response['items'][0]['volumeInfo']['description']
            }
        

    context = {"book_detail" : book_detail}

    return render(request, "bookDetect.html", context)
