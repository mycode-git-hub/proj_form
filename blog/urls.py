from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,)


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),

    # All blog post entries will start with post/. Next is the primary key for our post entry which will be represented as an integer <int:pk>. What’s the primary key you’re probably asking? Django automatically adds an auto-incrementing primary key to our database models. So while we only declared the fields title, author, and body on our Post model, under-the-hood Django also added another field called id, which is our primary key. We can access it as either id or pk.
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]
