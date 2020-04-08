from api import views
from django.urls import include, path


urlpatterns = [
    path('weekday/', views.CategoryList.as_view()),
    path('weekday/<int:pk>/', views.CategoryDetail.as_view()),
    path('campaign/', views.campaignList.as_view()),
    path('campaign/<int:pk>/', views.campaignDetail.as_view()),
    path('/', include('client.urls')),
]

