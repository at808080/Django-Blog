from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#python manage.py makemigrations ; generates the file with sql commands 
#python manage.py migrate ; runs the sql
#migrations allow us to make changes to sql database at any time 
#python manage.py shell ; allows us to open a shell to run sql commands and eplore the database 
#   this can also be done in the admin page

class BlogPost(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now) #automatically set to the current datetime using the python timezone module
    date_last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + str(self.date_added)

    #redirect redirects to a url
    #reverse returns the url as a string
    def get_absolute_url(self):
        return reverse('blogpost-detail', kwargs={'pk': self.pk})