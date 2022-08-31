from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    content = RichTextField()
    likes = models.ManyToManyField(User, related_name='question_post')
    date_created = models.DateTimeField(default=timezone.now)   
    
    def __str__(self):
        return f'{self.user.username} - Question'
    
    def get_absolute_url(self):
        return reverse('forumbase:question-detail', kwargs={'pk':self.pk})
    
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    question = models.ForeignKey(Question, related_name="comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    content = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)   

    def __str__(self):
        return '%s - %s' % (self.question.title, self.question.user)

    def get_success_url(self):
        return reverse('forumbase:question-detail', kwargs={'pk':self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Game(models.Model):
    name = models.CharField(max_length=128)
    studio = models.CharField(max_length=64)

    tags = TaggableManager()

    def __str__(self):
        return self.name