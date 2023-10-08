from django.urls import path
from work1App import views


urlpatterns = [
    path('', views.apiOverview, name='api-Overview'),
    #CRUD
    path('add/', views.add,name='add'),
    path('Search_filter/', views.Search_filter.as_view(),name='Search_filter'),
    path('update/<str:pk>/', views.update,name='update'),
    path('remove/<str:pk>/', views.remove,name='remove'),
    path('viewAll/', views.viewAll,name='viewAll'),
 

]

