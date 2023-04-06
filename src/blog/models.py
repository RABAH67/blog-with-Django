from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    like = models.ManyToManyField(User,related_name='likes',blank=True)
    dislike = models.ManyToManyField(User,related_name='dislikes',blank=True)
    views = models.PositiveIntegerField(default=0)
    
    def total_likes(self):
        
        return self.likes.count()

    def total_dislike(self):
        
        return self.dislike.count()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])
    
    class Meta:
        ordering = ('-post_date', )
        
        
        
        
class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    email = models.EmailField(verbose_name=' email')
    body = models.TextField(verbose_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
        

    def __str__(self):
        return 'comment {} on {}.'.format(self.name, self.post)

    class Meta:
        ordering = ('-comment_date',)