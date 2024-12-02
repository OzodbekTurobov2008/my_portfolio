from django.urls import path
from .views import home_view,about_view,work_view,category_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('work/',work_view,name='work-page'),
    path('category/',category_view,name='category-page'),
   
]
