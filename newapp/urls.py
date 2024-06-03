from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('student',views.studentpage,name='student'),
    path('adminsignup',views.adminsignup,name='adminsignup'),
    path('adminsignin',views.adminsignin,name='adminsignin'),
    path('addbook',views.addbook,name='addbook'),
    path('viewbook',views.viewbook,name='viewbook'),
    path('studentsignup',views.studentsignup,name='studentsignup'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('issuebook',views.issuebook,name='issuebook'),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view,name='viewstudent'),
    path('search', views.search_view,name='search'),
    path('logout_user', views.logout_user,name='logout_user'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('return-book/<str:firstname>/<str:lastname>/', views.return_book, name='return_book'),
    path('viewissuedbookbystudent/<int:stud_id>', views.viewissuedbookbystudent,name='viewissuedbookbystudent'),
    path('search_query', views.search_query,name='search_query'),
    path('adminafterlogin', views.adminafterlogin,name='adminafterlogin'),
    path('forgot_password', views.forgot_password,name='forgot_password'),
    path('studentafterlogin', views.studentafterlogin,name='studentafterlogin'),
    path('editbook/<int:book_id>', views.editbook,name='editbook'),

    
    



]