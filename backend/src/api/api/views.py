from rest_framework.generics import ListAPIView, RetrieveAPIView
from account.models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetailView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer