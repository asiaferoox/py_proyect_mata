# playground/urls.py
from django.urls import path
from pages.views import PostListView, PostDetailView

urlpatterns = [
    # …
    path('páginas/',          PostListView.as_view(),   name='pages_list'),
    path('páginas/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
