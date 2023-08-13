from django.urls import  path
from sample_app import  views
urlpatterns=[
    path('index',views.index,name="index"),
    path('',views.sign_in,name="sign_in"),
    path('sign_up',views.sign_up,name="sign_up"),
    path('sign_out',views.sign_out,name="sign_out"),
    path('style',views.style,name="style"),
    path('media',views.media,name="media")
]