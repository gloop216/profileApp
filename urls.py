from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('<slug:slug>/',views.portfoliodetails,name='portfoliodetails'),
    path('<slug:slug>/',views.blogsingle),

]
