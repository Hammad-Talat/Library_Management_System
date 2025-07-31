from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date
from .models import Author, Book, Student, Loan

class APIFunctionalityTests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling", bio="Fantasy author.")
        self.book = Book.objects.create(
            title="Harry Potter",
            author=self.author,
            published_year=1997,
            available_copies=5
        )
        self.student = Student.objects.create(
            name="Harry",
            email="harry@example.com",
            enrollment_number="ENR001",
            department="Magic",
            joined_date=date.today()
        )
        self.loan = Loan.objects.create(
            student=self.student,
            book=self.book,
            return_date=None,
            returned=False
        )

    def test_get_author_by_name(self):
        url = f'/api/author/{self.author.name}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.author.name)

    def test_filter_books_by_title(self):
        url = '/api/book/by-title/?title=Harry'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Harry Potter" in book["title"] for book in response.data))

    def test_filter_books_by_year(self):
        url = f'/api/book/by-year/?year={self.book.published_year}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["published_year"] == self.book.published_year for book in response.data))

    def test_generate_200_books(self):
        url = '/api/book/generate-200/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("200 books", response.data["message"])
        self.assertEqual(Book.objects.count(), 201)  
