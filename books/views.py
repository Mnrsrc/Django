from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author
from .models import Book
from django.http import Http404

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Home Page:)")

def author(request):
    template=loader.get_template('authors.html')
    context= {
        'author_lists': Author.objects.all()
    }
    return HttpResponse(template.render(context,request))
def book(request):
    # template2=loader.get_template('books.html')
    # authorView =Author.objects.filter(pk=4)
    try:
        context2={
            'book_lists':Book.objects.all()
             }
    except Book.DoesNotExist:
        raise Http404("Book does not exist!!!!!!!")
    
    return render(request,'books.html',context2)
def authorDetail(request,authorId):
    try:
        context3={
       'author_details' :Author.objects.get(pk=authorId)
       }
    except Author.DoesNotExist:
        raise Http404("Author does not exist!!!!!")
    
    return render(request,'authorDetails.html',context3)
def bookDetail(request,bookId):
    try:

        context4={
            'book_details': Book.objects.get(id=bookId)
        }
    except Book.DoesNotExist:
        raise Http404("Book does not exist!!!!!")
    return render(request,'bookDetails.html',context4)