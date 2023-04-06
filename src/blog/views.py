from django.shortcuts import render ,get_object_or_404,redirect
from .models import Post ,Comment
from .forms import NewComment ,PostCreateForm
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.








def home(request):

    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    
    context = {
        'posts':posts,
        'page':page,
    }
    return render(request, 'blog/index.html',context)





def about(request):
    
    return render(request, 'blog/about.html')





def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter()
    comment_form = NewComment()
    post.views +=1
    post.save()
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            return redirect('detail', post_id)
    else:
        comment_form = NewComment()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    
    return render(request, 'blog/detail.html', context)




class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/new_post.html'
    #form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    
class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required()
def like(request,post_id):
    
    post = Post.objects.get(pk=post_id)

    if request.user in post.like.all() or post.dislike.all():
        post.like.remove(request.user)
        post.dislike.remove(request.user)
        post.like.add(request.user)

    else:
        post.like.add(request.user)
    return redirect('detail', post_id)

@login_required()
def dislike(request,post_id):
    
    post = Post.objects.get(pk=post_id)

    if request.user in post.dislike.all() or post.like.all():
        post.dislike.remove(request.user)
        post.like.remove(request.user)
        post.dislike.add(request.user)

    else:
        post.dislike.add(request.user)
    return redirect('detail', post_id)
