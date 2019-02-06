from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Url
from .forms import UrlForm, DecodeForm
from .utils import create_shortcode


def encode(request):
	form = UrlForm()
	if request.method == 'POST':
		form = UrlForm(request.POST)

		if form.is_valid():
			obj = Url()
			code = create_shortcode(Url)
			obj.url=form.cleaned_data['url']
			obj.shortcode=code
			obj.save()
			
		
			return HttpResponse("http://localhost:8000/{sc}".format(sc=code))
	

	return render(request,'urlapp/create.html',{'form':form})

def decode(request):
	form = DecodeForm()
	# obj = Url()
	if request.method == 'POST':
		form = UrlForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			shorturl = form.cleaned_data['url']
			shortcode = shorturl.replace('http://localhost:8000/', '')
			print(shortcode)
		
			qs = Url.objects.filter(shortcode=shortcode).first()
			
			original_url = str(qs)
			if original_url is None:
				return HttpResponse('URL is: '+original_url)
			return HttpResponse('URL not in db')

	return render(request,'urlapp/decode.html',{'form':form})
