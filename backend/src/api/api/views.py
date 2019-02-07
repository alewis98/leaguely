from rest_framework.generics import ListAPIView, RetrieveAPIView
from account.models import UserProfile
from api.models import *
from .serializers import *

class UserProfileListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetailView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class OrganizationListView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationDetailView(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class RefereeDetailView(RetrieveAPIView):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

class LeagueListView(ListAPIView):
    serializer_class = LeagueSerializer

    def get_queryset(self):
        organization = Organization.objects.get(pk=self.kwargs['pk'])
        queryset = organization.leagues.all()
        return queryset

        
