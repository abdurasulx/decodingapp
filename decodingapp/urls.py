from django.urls import path, include


from . import  views
urlpatterns = [ 
    path('', views.home,name='home'),
    path('savol/<slug:slug>',views.seeque,name='seepost'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]