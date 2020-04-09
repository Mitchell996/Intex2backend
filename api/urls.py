from api import views
from django.urls import include, path


urlpatterns = [
    path('weekday/', views.WeekdayList.as_view()),
    path('weekday/<int:pk>/', views.WeekdayDetail.as_view()),
    path('campaign/', views.CampaignList.as_view()),
    path('campaign/<int:pk>/', views.CampaignDetail.as_view()),
    #path('/', include('client.urls')),
]

