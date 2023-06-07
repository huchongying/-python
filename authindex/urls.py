from django.urls import path,include

from authindex import views
app_name="authindex"
urlpatterns=[
    path('',views.user_index,name='user_index'),
]