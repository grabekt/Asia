from django.db import models
from django.utils import timezone

class Post(models.Model):
	autor = models.ForeignKey('auth.user')
	tytul = models.CharField(max_length=200)
	tekst = models.TextField()
	publikowany = models.DateTimeField(default=timezone.now)
	utworzony = models.DateTimeField(auto_now_add=True)
	edytowany = models.DateTimeField(auto_now=True)


	# class Meta:
	# 	ordering = ('-publikowany',)


	def __str__(self):
		return self.tytul
