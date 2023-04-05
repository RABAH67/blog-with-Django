from django.shortcuts import render ,get_object_or_404,redirect
from .models import Post ,Comment
from .forms import NewComment
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
    comments = post.comments.filter(active=True)
    comment_form = NewComment()
    
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