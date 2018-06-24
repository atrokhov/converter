# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponsePermanentRedirect
from .models import Link
from .forms import LinkForm
from youtube_dl import YoutubeDL
from django.contrib import messages

def index(request):
    latest_link_list = Link.objects.order_by('-pub_date')
    context = {'latest_link_list': latest_link_list}
    return render(request, 'converter/index.html', context)

def link_new(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.pub_date = timezone.now()
            url = link.link_text 
            link.save()
            ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]}
            with YoutubeDL(ydl_opts) as ydl:
                r = ydl.extract_info(url, download=False)
                video_url = r['url']
    else:
        form = LinkForm()
    return render(request, 'converter/link_new.html', {'form': form})