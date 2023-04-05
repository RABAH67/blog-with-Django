from django.shortcuts import render ,get_object_or_404
from .models import Post ,Comment

# Create your views here.



def home(request):
    
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.html',context)





def about(request):
    
    return render(request, 'blog/about.html')





def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    context = {
        'post':post,
        'comments':comments
    }
    
    return render(request, 'blog/detail.html', context)