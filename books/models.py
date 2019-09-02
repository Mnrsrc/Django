from django.db import models

# Create your models here.
class Author(models.Model):
    def __str__(self):
        return self.authorName
    authorName=models.CharField(max_length=50)
    createdDate=models.DateField("Date created!")

class Book(models.Model):
    def __str__(self):
        return self.bookName
    bookName=models.CharField(max_length=70)
    createdDate=models.DateTimeField("Date created")
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    bookPrice=models.DecimalField(decimal_places=2,max_digits=4,null=True)