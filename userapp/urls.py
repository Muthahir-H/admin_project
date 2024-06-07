from django.urls import path
from . import views 



urlpatterns = [

    path('userlistview/',views.listBook,name='userbooklist'),

    path('userdetailview/<int:book_id>/',views.detailView,name='userdetails'),

    path('usersearch/',views.Search_Book,name='usersearch'),

    path('add_to_cart/<int:book_id>/',views.add_to_cart,name='addtocart'),

    path('view_cart',views.view_cart,name='viewcart'),

    path('increase/<int:item_id>/',views.increase_quantity,name='increase_quantity'),

    path('decrease/<int:item_id>/',views.decrease_quantity,name='decrease_quantity'),

    path('remove_from_cart/<int:item_id>/',views.remove_from_cart,name='remove_cart'),

    path('craete_checkout-session/',views.create_checkout_session,name='create-checkout-session'),

    path('success/',views.success,name='success'),

    path('cancel/',views.cancel,name='cancel')


    
]

