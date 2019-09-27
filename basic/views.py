from django.shortcuts import render
from django.http import HttpResponse
from b.models import Post





# Create your views here.
def BasicView(request):
    list = Post.objects.all()
    context = {'list': list}
    template = 'BasicView.html'
    return render(request, template, context)
