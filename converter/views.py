# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Link
from .forms import LinkForm
import youtube_dl
from django.http import HttpResponse
from youtube_dl import YoutubeDL


def index(request):
    latest_link_list = Link.objects.order_by('-pub_date')
    context = {'latest_link_list': latest_link_list}
    return render(request, 'converter/index.html', context)

def download(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            url = link.link_text
            link.save()

            ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192', }], 'quiet': True, 'restrictfilenames': True }

            with YoutubeDL(ydl_opts) as ydl:
                video_info = ydl.extract_info(url, download=False)
                video_url = video_info['url']
                return redirect(video_url)
    else:
        form = LinkForm()
    return render(request, 'converter/link_new.html', {'form': form})