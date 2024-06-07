from django.urls import path
from . import views



urlpatterns = [
    path("create-book/",views.createbook,name='createbook'),

    path('',views.listBook,name='booklist'),

    path('detailview/',views.detailView,name='details'),

    path('updateview/<int:book_id>/',views.updateBook,name='update'),

    path('deleteview/<int:book_id>/',views.deleteView,name='delete'),

    path('author/',views.createauthor,name='author'),

    path('index/',views.Index),

    path('search/',views.Search_Book,name='search'),

    path('register/',views.Register_User,name='register'),

    path('login/',views.LoginUser,name='login'),

    path('logout/',views.Logout,name='logout'),

    
]

