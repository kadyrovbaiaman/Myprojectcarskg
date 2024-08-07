from django.urls import path
from.views import *



urlpatterns = [
    path('',CarViewSet.as_view({'get':'list',
                                'post':'create'}),name='car_list'),
    path('<int:pk>/',CarViewSet.as_view({'get':'retrieve',
                                         'put':'update','delete':'destroy'}),name='car_detail'),


    path('category/',CategoryViewSet.as_view({'get':'list',
                                              'post':'create'}),name='category_list'),
    path('category/<int:pk>/',CategoryViewSet.as_view({'get':'retrieve',
                                                       'put':'update','delete':'destroy'}),name='category_detail'),


    path('carmake/',CarMakeViewSet.as_view({'get':'list',
                                            'post':'create'}),name='carmake_list'),
    path('carmake/<int:pk>/',CarMakeViewSet.as_view({'get':'retrieve',
                                                     'put':'update','delete':'destroy'}),name='make_detail'),


    path('carmodel/',CarModelViewSet.as_view({'get':'list',
                                              'post':'create'}),name='carmodel_list'),
    path('carmodel/<int:pk>/',CarModelViewSet.as_view({'get':'retrieve',
                                                       'put':'update','delete':'destroy'}),name='model_detail'),
]
