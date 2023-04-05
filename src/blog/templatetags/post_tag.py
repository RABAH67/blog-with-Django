from django import template
from blog.models import Post ,Comment


register = template.Library()

@register.inclusion_tag('blog/last_post.html')
def latest_post():
    context = {
        
        'l_postes':Post.objects.all()[0:5]
    }
    return context


@register.inclusion_tag('blog/latest_comments.html')
def lastest_comments():
    
    context = {
        'l_comments':Comment.objects.filter(active=True)[0:5]
    }
    return context