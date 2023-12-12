from django.shortcuts import render, redirect


from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def home(request):
    return render(request, "home.html")
