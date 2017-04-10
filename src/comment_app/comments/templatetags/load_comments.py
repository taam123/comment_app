from django import template 

register  = template.Library()

from comments.models import Comment 


@register.inclusion_tag("comment/snippets/load_comment.html")
def load_comments(url):
	qs = Comment.objects.filter(url=url)
	return {"comments":qs}