from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from . models import Links



def home(request):
    if request.method== "POST":
        link_new=request.POST.get('page','')
        urls=requests.get(link_new)
        beautifulsoup=BeautifulSoup(urls.text,'html.parser')

        for link in beautifulsoup.find_all('a'):
            li_address=link.get('href')
            li_name=link.string
            Links.objects.create(address=li_address,stringname=li_name)
        return HttpResponseRedirect('/')
    else:
        data_value=Links.objects.all()

    return render(request,'home.html',{'data_value':data_value})
