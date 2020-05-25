from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django_resized import ResizedImageField



class Post(models.Model):
	# title = models.CharField(max_length = 255)
	# title_tag = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField(blank=True)
	post_date = models.DateField(auto_now_add=True)
	# image = models.FileField(null=True, blank=True)
	image = ResizedImageField(size=[700,500], upload_to='BlogSite/media/', blank=True, null=True)
	likes = models.ManyToManyField(User, related_name='blog_posts')


	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return str(self.author)


	def get_absolute_url(self):
		return reverse('home')
