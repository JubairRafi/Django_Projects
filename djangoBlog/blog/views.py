from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import post

# dictionary for dumy data
# posts =[
#     {
#         'author': 'CoreyMS',
#         'title': 'blog post 1',
#         'content': 'First post content',
#         'date_posted': 'jan 12, 2020'
#     },
#     {
#         'author': 'pial',
#         'title': 'blog post 2',
#         'content': 'second post content',
#         'date_posted': 'jan 13, 2020'
#     }
# ]

# Create your views here.
def home(request):
    #dictionary that holds all the dictionary
    context={
        'posts':post.objects.all() #from database
    }
    return render(request, 'blog/home.html', context) #context arg is used for access data 

#class view
class PostListView(ListView):
    model = post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields = [ 'title', 'content' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    fields = [ 'title', 'content' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request, 'blog/about.html', {'title':'About'}) #solo dictionary

