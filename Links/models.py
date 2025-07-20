from django.db import models

# Create your models here.
class User(models.Model):
  username=models.CharField(max_length=15)
  email=models.EmailField()
  password=models.CharField()
  profile_link=models.URLField(default="https://static.vecteezy.com/system/resources/previews/004/511/281/original/default-avatar-photo-placeholder-profile-picture-vector.jpg")
  def __str__(self):
    return f"{self.username} {self.email} {self.password} {self.profile_link}"
  
class Link(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="links")
  name=models.CharField(max_length=100)
  description=models.TextField(max_length=100,default="")
  link=models.URLField()
  def __str__(self):
    return f"{self.name} {self.link}"