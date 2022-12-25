from django.contrib import admin
from django.urls import path, include
from .views import Home, Article, Addpost, Editpost, Deletepost, Addcategory, category, category_listview, Likes, Addcomment

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', Article.as_view(), name='article'),
    path('addpost/', Addpost.as_view(), name='addpost'),
    path('article/edit/<int:pk>', Editpost.as_view(), name='editpost'),
    path('article/<int:pk>/remove', Deletepost.as_view(), name='deletepost'),
    path('addcategory/', Addcategory.as_view(), name='addcategory'),
    path('category/<str:name>/', category, name='category'),
    path('category_list', category_listview, name='category_listview'),
    path('likes/<int:pk>', Likes, name='likes'),
    path('article/<int:pk>/addcomment', Addcomment.as_view(), name='addcomment'),
]
