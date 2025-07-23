from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    published_year = models.IntegerField()
    available_copies = models.PositiveIntegerField()

    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    joined_date = models.DateField()

   

class Loan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='loans')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)


