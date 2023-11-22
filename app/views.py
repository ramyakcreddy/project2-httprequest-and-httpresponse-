from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def jampandu(request):
    return HttpResponse('<h1><marquee>hi how are u</h1></marquee>')



def flowers(request):
    return HttpResponse("<h1><marquee>Flowers are beautifull,L love it at lot</h1></marquee>")


