from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post, Category, Comment
from .form import Postform


class Home(ListView):
    model = Post
    template_name = 'blog_apps/home.html'
    ordering = ['-post_date']


class Article(DetailView):
    model = Post
    template_name = 'blog_apps/article.html'

    def get_context_data(self,*args, **kwargs):
        likes = get_object_or_404(Post, id=self.kwargs['pk'])
        context = super(Article, self).get_context_data(*args, **kwargs)
        likes_total = likes.likes_count()
        liked = False
        if likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = likes_total
        context['liked'] = liked
        return context


class Addpost(CreateView):
    model = Post
    form_class = Postform
    template_name = 'blog_apps/addpost.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'


class Editpost(UpdateView):
    model = Post
    form_class = Postform
    template_name = 'blog_apps/editpost.html'


class Addcategory(CreateView):
    model = Category
    template_name = 'blog_apps/addcategory.html'
    fields = ('name',)


class Deletepost(DeleteView):
    model = Post
    template_name = 'blog_apps/deletepost.html'
    success_url = reverse_lazy('home')


def category(request, name):
    post_under_this = Post.objects.filter(category=name.replace('-', ' '))
    return render(request, 'blog_apps/category.html', {'name': name.replace('-', ' '),
                                                       'post_under_this': post_under_this})


def category_listview(request):
    cat_menu = Category.objects.all()
    return render(request, 'blog_apps/category_listview.html', {'cat_menu': cat_menu})


def Likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


class Addcomment(CreateView):
    model = Comment
    template_name = 'blog_apps/addcomment.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
