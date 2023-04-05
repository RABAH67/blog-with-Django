from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib import messages
from django.views import View
from .forms import CustemRegistrationForm
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage




class CustemRegistrationView(View):
    
    def get(self,request):

        form = CustemRegistrationForm()
        
        return render(request,"user/CustemRegistrationForm.html",locals())
    def post(self,request):
        
        form = CustemRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Login! Registration Successfully")
            
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"user/CustemRegistrationForm.html",locals())
    
    
    
    
    
def profile(request):
    
    posts= Post.objects.filter(author=request.user)
    posts_list= Post.objects.filter(author=request.user)

    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_page)
    context = {
        'posts':posts,
        'page':page,
        'posts_list':posts_list,
    }
    return render(request,'user/profile.html',context)