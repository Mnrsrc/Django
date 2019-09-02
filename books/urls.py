from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book',views.book,name="Books Page"),
    path('author',views.author,name="Authorss"),
    path('authordetails/<int:authorId>',views.authorDetail,name="Author Details"),
    path('bookdetails/<int:bookId>', views.bookDetail,name="Book Details")
]