from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django_resized import ResizedImageField
from django.utils import timezone
import math
from ckeditor.fields import RichTextField


class Post(models.Model):
	author = models.ForeignKey(User, on_delete =models.CASCADE)
	# body = models.TextField(blank = True)
	body = RichTextField(blank = True, null = True)
	post_date = models.DateField(auto_now_add = True)
	pub_date = models.DateTimeField(auto_now_add = True)
	image = ResizedImageField(size = [600, 400], upload_to = 'BlogSite/media/', blank = True, null = True)
	video = models.FileField(upload_to ='BlogSite/media/', null = True, blank = True)
	likes = models.ManyToManyField(User, related_name = 'blog_posts')


	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return str(self.author)

	def get_absolute_url(self):
		return reverse('home')

	def whenpublished(self):
		now = timezone.now()

		diff = now - self.pub_date
		if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
			seconds= diff.seconds
			if seconds == 1:
				return str(seconds) +  "second ago"
			else:
				return str(seconds) + " seconds ago"

		if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
			minutes= math.floor(diff.seconds/60)
			if minutes == 1:
				return str(minutes) + " minute ago"
			else:
				return str(minutes) + " minutes ago"

		if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
			hours= math.floor(diff.seconds/3600)
			if hours == 1:
				return str(hours) + " hour ago"
			else:
				return str(hours) + " hours ago"

		if diff.days >= 1 and diff.days < 30:
			days= diff.days
			if days == 1:
				return str(days) + " day ago"
			else:
				return str(days) + " days ago"

		if diff.days >= 30 and diff.days < 365:
			months= math.floor(diff.days/30)

			if months == 1:
				return str(months) + " month ago"
			else:
				return str(months) + " months ago"

		if diff.days >= 365:
			years= math.floor(diff.days/365)
			if years == 1:
				return str(years) + " year ago"
			else:
				return str(years) + " years ago"