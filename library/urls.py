from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, BookViewSet, LoanViewSet ,AuthorViewSet

router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"loans", LoanViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
