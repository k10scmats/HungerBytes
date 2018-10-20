from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page_1', views.page_1, name='page_1'),
    path('page_2', views.page_2, name='page_2'),
    path('page_3', views.page_3, name='page_3'),
    path('page_4', views.page_4, name='page_4'),
    path('page_4a', views.page_4a, name='page_4a'),
    path('page_4b', views.page_4b, name='page_4b'),
    path('page_4c', views.page_4c, name='page_4c'),
    path('page_4d', views.page_4d, name='page_4d'),
    path('page_4e', views.page_4e, name='page_4e'),
    path('page_5', views.page_5, name='page_5'),
]