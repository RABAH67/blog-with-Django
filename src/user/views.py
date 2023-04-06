from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib import messages
from django.views import View
from .forms import CustemRegistrationForm ,UserUpdateForm, ProfileUpdateForm
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



@login_required()
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(
                request, '   Profile Edited Successfull')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)