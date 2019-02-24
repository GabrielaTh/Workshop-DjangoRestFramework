from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.timezone import now
from django.db.models.signals import post_save,pre_save
# Create your models here.

class Group(models.Model):   
    Business_key = models.IntegerField() 
    company = models.CharField(null=True, blank=True,max_length=300)
    

    def __str__(self):
        return format(self.Business_key)

class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
    
        user = self.create_user(
            email,
            name,
            password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class Periode(models.Model):
    is_Done = models.BooleanField(default=False)
    date = models.DateTimeField(default=now, editable=False)
    session = models.CharField(max_length=300)
    # company = models.ManyToManyField( to='profiles_api.Group', related_name='business_key',
    #  ) 
    Businesskey = models.ManyToManyField( to='newapp.Group', related_name='key',
     ) 
    def __str__(self):
        return '{}'.format(self.session)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(null=True, blank=True,max_length=300)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'# Spécifie à DRF de s'identifier avec l'email au lieu du nom d'utilisateur
    REQUIRED_FIELDS = ['name']

    def update_Profile(sender,instance, **kwargs):
        false = UserProfile.objects.filter(is_staff=True)
        if false:
            false.update(is_staff=False)

    post_save.connect(update_Profile, sender=Periode)

    def __str__(self):

        return self.email


class TypeIncidents(models.Model):
    nomType = models.CharField(max_length=50)
    def __str__(self):
        return 'Type Incidents: {}'.format(self.nomType)
    
class Incidents(models.Model):
    nomIncident = models.CharField(max_length=50)
    idTypeIncidents = models.ForeignKey(TypeIncidents, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Incidents: {}'.format(self.nomIncident)

class Motivation(models.Model):
    choix = models.TextField()
    def __str__(self):
        return 'Motivation: {}'.format(self.choix)

class Transports(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return 'Transports: {}'.format(self.nom)

class Detail(models.Model):
    userId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    idTransport = models.ForeignKey(Transports, on_delete=models.CASCADE)
    idIncidents = models.ForeignKey(Incidents, on_delete=models.CASCADE)
    frequence = models.IntegerField()
    commentaire = models.TextField(null=True, blank=True)
    motivation = models.ForeignKey(Motivation, on_delete=models.CASCADE)
    created = models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return 'Incidents: {}'.format(self.userId)