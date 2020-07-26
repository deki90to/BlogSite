from django import forms
from . models import Post, Comment


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'body', 'image', 'video',)

		widgets = {
			'author':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
			'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type here...', 'rows':3, 'cols':10}),
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin'}),
			'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type comment...', 'rows':3, 'cols':10}),
		}