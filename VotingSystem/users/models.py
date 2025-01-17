
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique

    USERNAME_FIELD = 'email'  # Use email to log in
    REQUIRED_FIELDS = ['username']  # Keep the username field if necessary


# Voting session model
class VotingSession(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



# Candidate model
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    session = models.ForeignKey(VotingSession, on_delete=models.CASCADE, related_name="candidates")
    image = models.ImageField(upload_to='candidates/')
    manifesto = models.TextField()
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Session: {self.session.title})"


class Voter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    eligible = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email






# Role-based user extension
class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Voter', 'Voter')],
        default='Voter'
    )

    def __str__(self):
        return f"{self.user.username} ({self.role})"



'''
# Vote model
class Vote(models.Model):
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    session = models.ForeignKey(VotingSession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.voter.username} voted for {self.candidate.name}"

    class Meta:
        unique_together = ('voter', 'session')  # Ensure one vote per session per user
'''


# Results model (for analytics)
class VotingResult(models.Model):
    session = models.OneToOneField(VotingSession, on_delete=models.CASCADE)
    total_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Results for {self.session.title}"




class Vote(models.Model):
    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the custom user model
        on_delete=models.CASCADE,
        related_name="votes"
    )
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="votes")
    session = models.ForeignKey(VotingSession, on_delete=models.CASCADE, related_name="votes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'session')  # Prevent duplicate votes in a session