from django.urls import path
from secondapp import views
app_name='secondapp'

urlpatterns=[
    path('index/',views.index,name='index'),
    path('other/',views.other,name='other'),
    path('form/',views.form,name='form'),
    path('users/',views.users,name='users'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')
]
