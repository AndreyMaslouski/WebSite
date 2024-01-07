
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('about-us', views.about, name = 'about'),
    path('help-me', views.help),
    path('create', views.about, name = 'create'),
    path('draw', views.about, name = 'draw')

]
