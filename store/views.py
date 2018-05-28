from django.shortcuts import render

def index(request):
    return render(request,'template.html')


def store(request):
    return render(request,'C:\Users\anny\Desktop\django\bookstore\store\store.html')
