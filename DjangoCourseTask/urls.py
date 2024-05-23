from django.contrib import admin
from django.urls import path
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('form/', views.my_form_view, name='my_form'),
    path('data/', views.data_view, name='data_view'),
]
