from django.contrib import admin
from .models import Question, Comment, Game

admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Game)
