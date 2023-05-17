from django.shortcuts import render

def app(request):
    return render(request, 'app/app.html')
# Create your views here.
