from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, BookViewSet, LoanViewSet ,AuthorViewSet ,generate_200_books
from .views import get_author_by_name, filter_books_by_year,filter_books_by_title

router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"loans", LoanViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("author/<str:name>/", get_author_by_name),
   path('book/by-title/', filter_books_by_title),
    path('book/by-year/', filter_books_by_year),
    path('book/generate-200/', generate_200_books)
]
