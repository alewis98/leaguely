from django.urls import path
from rest_framework.authtoken import views as drf_views

from .views import *
urlpatterns = [
    path('auth/', drf_views.obtain_auth_token, name='auth'),
    path('users/', UserProfileListView.as_view()),
    path('users/<pk>', UserProfileDetailView.as_view()),
    path('organizations/', OrganizationListView.as_view()),
    path('organizations/<pk>', OrganizationDetailView.as_view()),
    path('referees/<pk>', RefereeDetailView.as_view()),
    path('organizations/<pk>/leagues/', LeagueListView.as_view()),
    path('organizations/<pk>/leagues/<pk2>', LeagueDetailView.as_view()),
    path('organizations/<pk>/leagues/<pk2>/divisions/', DivisionListView.as_view()),
    path('organizations/<pk>/leagues/<pk2>/divisions/<pk3>', DivisionDetailView.as_view()),
    path('organizations/<pk>/leagues/<pk2>/divisions/<pk3>/teams/', TeamListView.as_view()),
    path('organizations/<pk>/leagues/<pk2>/divisions/<pk3>/teams/<pk4>', TeamDetailView.as_view()),
]

