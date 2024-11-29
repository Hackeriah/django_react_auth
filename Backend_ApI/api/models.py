from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    full_name = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    image = models.ImageField(default="default.jpg", upload_to="user_images")
    verified  = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name    
    
class Course(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Optional pricing field
    duration = models.IntegerField(help_text="Duration in hours")
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)  