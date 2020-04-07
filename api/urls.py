from api import views
from django.urls import include, path


urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('campaign/', views.campaignList.as_view()),
    path('campaign/<int:pk>/', views.campaignDetail.as_view()),
    path('search/', views.CreateSale.as_view()),
    path('/', include('client.urls')),
]