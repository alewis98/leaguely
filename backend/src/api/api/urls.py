from django.urls import path

from .views import UserProfileListView, UserProfileDetailView
urlpatterns = [
    path('', UserProfileListView.as_view()),
    path('<pk>', UserProfileDetailView.as_view())
]

