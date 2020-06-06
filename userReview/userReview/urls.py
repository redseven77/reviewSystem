from django.contrib import admin
from django.urls import path
from userReview.views import HomeAPIView, ReviewListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', ReviewListView.as_view(), name='review'),
    path('', HomeAPIView.as_view(), name='search-review'),
]
