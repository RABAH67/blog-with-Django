from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib import messages
from django.views import View
from .forms import CustemRegistrationForm









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