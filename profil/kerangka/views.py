from turtle import title
from django.shortcuts import render, HttpResponse

# Create your views here.
def awal(request):
    return HttpResponse('berhasil diinstal')

def home(request):
    context={
        'title':title
    }
    return render(request, 'home.html', context)

def kontak(request):
    context={
        'title':title
    }
    return render(request, 'kontak.html', context)

def profil(request):
    context={
        'title':title
    }
    return render(request, 'profil.html', context)

def organisasi(request):
    context={
        'title':title
    }
    return render(request, 'organisasi.html', context)

def portofolio(request):
    context={
        'title':title
    }
    return render(request, 'portofolio.html', context)