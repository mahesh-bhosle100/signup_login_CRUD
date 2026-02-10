from .views import Home ,About ,Test_data ,Echo_api ,Easy_api,Student_all ,signup ,login ,login_session
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
   
    path("home/" ,Home),
    path("about/",About),
    path("test_data/" ,Test_data),
    path("echo_api/" ,Echo_api),
    path("easy_api/" ,Easy_api) ,
    path("student_all/" ,Student_all),
    path("signup/" ,signup),
    path("login/" ,login) ,
    # path("login_session",login_session)
    
]
token = "7861378726b7581a31222a960e99287419a5b960"
    # "token": "c3aef291d1dbed3e43007e46bdfde83a6bc61072"

