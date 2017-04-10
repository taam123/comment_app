from django.conf.urls import url 

from .views import CommentListAPIView, CommentCreateAPIView


urlpatterns = [

	url(r'^$', CommentListAPIView.as_view(), name="comments"),
	url(r'^create/$', CommentCreateAPIView.as_view(), name="create"),

]