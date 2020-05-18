# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post
from . forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
		
	return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))

# def LikeHome(request, pk):
# 	post = get_object_or_404(Post, id=request.POST.get('post.id'))
# 	post.likes.add(request.user)
# 	return HttpResponseRedirect(reverse('home'), args=[str(pk)])


class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-id']

class articleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self, *args, **kwargs):
		context = super(articleDetailView, self).get_context_data()
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True
		
		context['total_likes'] = total_likes
		context['liked'] = liked
		return context


class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

class UpdatePostView(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'update_post.html' 

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

