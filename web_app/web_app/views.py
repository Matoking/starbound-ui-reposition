from django.shortcuts import render, redirect

from forms import DownloadModForm

from starbound_ui_reposition.patch import create_mod


def index(request):
    return render(request, "index.html")
