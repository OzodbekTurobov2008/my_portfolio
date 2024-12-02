from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def category_view(request):
    return render(request, 'category.html')

def work_view(request):
    return render(request, 'work.html')
