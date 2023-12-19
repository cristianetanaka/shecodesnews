from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import NewsStory
from .forms import Storyform
from users.models import CustomUser
from django.shortcuts import get_object_or_404



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

def index(request):
    all_stories = NewsStory.objects.all()
    context = {'all_stories': all_stories}
    return render(request, 'news/index.html', context)


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
   
class AddStoryView(generic.CreateView):
    form_class = Storyform
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# detail view for 1 particular user
class AuthorDetailView(generic.DetailView):
    model = CustomUser
    template_name = 'news/author.html'
    context_object_name = 'author'
    #get user
    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
        
   