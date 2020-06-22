from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
def index(requests):
    return render(requests,"index.html")

def book(requests):
    books=[
        {"id":1,"title":"python","price":89},
        {"id":2,"title":"java","price":90},
        {"id":3,"title":"php","price":100},
    ]
    return JsonResponse(books,safe=False)