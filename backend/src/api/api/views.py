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

class LeagueDetailView(RetrieveAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    lookup_url_kwarg = 'pk2'

    
class DivisionListView(ListAPIView):
    serializer_class = DivisionSerializer

    def get_queryset(self):
        league = League.objects.get(pk=self.kwargs['pk2'])
        queryset = league.divisions.all()
        return queryset
    
class DivisionDetailView(RetrieveAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    lookup_url_kwarg = 'pk3'

class TeamListView(ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        division = Division.objects.get(pk=self.kwargs['pk3'])
        queryset = division.teams.all()
        return queryset

class TeamDetailView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_url_kwarg = 'pk4'

class DivisionGamesListView(ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        organization = Organization.objects.get(pk=self.kwargs['pk'])
        league = organization.leagues.get(pk=self.kwargs['pk2'])
        division = league.divisions.get(pk=self.kwargs['pk3'])
        queryset = division.games.all()
        return queryset
