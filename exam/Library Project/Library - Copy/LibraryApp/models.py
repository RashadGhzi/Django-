from django.db import models

class BooksAdd(models.Model):
    name = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    book_desc = models.CharField(max_length=140)
    image = models.ImageField(upload_to="mages")
    def __str__(self):
        return f"{self.name}  {self.book_name}"

class BookLend(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)    
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(blank=True)
    def __str__(self):
        return f"{self.full_name} {self.from_date}"

