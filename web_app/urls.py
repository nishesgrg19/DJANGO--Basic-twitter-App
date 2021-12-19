from django.urls import path
from web_app import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('register/',views.register,name='register'),
    path('sign-in/',views.sign_in,name='sign-in'),
    path('sign-out/',views.sign_out,name='sign-out'),
    path('info/',views.info,name='info'),
    path('reset/',views.reset,name='reset'),
    path('contact',views.contact,name='contact')
]