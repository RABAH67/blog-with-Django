from django.urls import path 
from .forms import LoginForm
from django.contrib.auth import views as auth_view
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    path('login/',auth_view.LoginView.as_view(template_name='user/register.html',authentication_form=LoginForm),name="login"),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/',views.CustemRegistrationView.as_view(),name="registration"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



