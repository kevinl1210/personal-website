from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('notes/', views.notes, name='notes'),
    path('classifier/', views.classifier, name='classifier'),
    path('classify/', views.classify, name='classify'),
]
