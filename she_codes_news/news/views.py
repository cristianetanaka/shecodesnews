from typing import Any
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsStory
from .forms import Storyform
from users.models import CustomUser

def like_post(request, post_id):
    post = get_object_or_404(NewsStory, pk=post_id)
    post.likes.add(request.user)
    return redirect('news:story', pk=post_id)

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context
    
class AddStoryView(generic.CreateView):
    form_class = Storyform
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateStoryView(generic.UpdateView):
    model = NewsStory
    template_name = 'news/updatestory.html'
    fields = ['title', 'image_url', 'pub_date', 'content']
    success_url = reverse_lazy('news:index')

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deletestory.html'
    success_url = reverse_lazy('news:index')

class AuthorDetailView(generic.DetailView):
    model = CustomUser
    template_name = 'news/author.html'
    context_object_name = 'author'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
