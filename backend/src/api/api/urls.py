from django.urls import path

from .views import *
urlpatterns = [
    path('users/', UserProfileListView.as_view()),
    path('users/<pk>', UserProfileDetailView.as_view()),
    path('organizations/', OrganizationListView.as_view()),
    path('organizations/<pk>', OrganizationDetailView.as_view()),
    path('referees/<pk>', RefereeDetailView.as_view()),
    path('organizations/<pk>/leagues/', LeagueListView.as_view()),
]

