from django.db import models
from api.models import *
from django.db.models.signals import post_save

# Managers
class UserProfileManager(models.Manager):

    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset()

# Users
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    phone_number = models.CharField(max_length=9, null=True, blank=True)
    address = models.CharField(max_length=240, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_referee = models.BooleanField(default=False)

    # override objects with manager
    objects = UserProfileManager()

    def __str__(self):
        return self.user.__str__()
    
    def to_string(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)

# Signal to create UserProfile when a new User is created
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        user_profile = UserProfile.objects.create(user=user)
        if user.is_staff:
            user_profile.is_admin = True
            user_profile.save()

post_save.connect(create_profile, sender=User)
