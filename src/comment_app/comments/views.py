from django.shortcuts import render

# Create your views here.


def dashboard(request):
	template = "comment/dashboard.html"
	context = {}
	return render(request, template, context)