from django.shortcuts import render, redirect
from django.http import Http404
from .models import UrlShortener

# Create your views here.
def home(request):
    if request.method == "POST":
        complete_url = request.POST.get("complete_url")

        if UrlShortener.complete_url_errors(request, complete_url):
            return redirect("home")

        short_url = UrlShortener.shorten_url()

        url = UrlShortener.objects.create(complete_url=complete_url, short_url=short_url)

        return render(request, "shortener/index.html", {"url":url})

    return render(request, "shortener/index.html")


def redirect_url(request, short_url):
    if UrlShortener.invalid_url(request, short_url):
        raise Http404("The Short Url is Invalid")

    url = UrlShortener.objects.get(short_url=short_url)
    url.increase_visit()

    return redirect(url.complete_url)
