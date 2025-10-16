from django.shortcuts import render
from .models import Audio, HomeContent, Audio, Gallery, Shop, Tour
# Create your views here.

def home(request):
    home_content = HomeContent.objects.all()
    return render(request, 'home.html', {
        'home_content': home_content,
    })

def bio(request):
    return render(request, 'bio.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    gallery_images = Gallery.objects.all()
    return render(request, 'gallery.html', {
        'gallery_images': gallery_images,
    })

def music(request):
    audio_list = Audio.objects.all()
    return render(request, 'music.html', {
        'audio_list': audio_list,
    })

# def music_view(request):
#     audio_list = Audio.objects.all()  # Fetch all audio files from the database
#     return render(request, 'music.html', {'audio_list': audio_list})

def shop(request):
    shop_items = Shop.objects.all()
    return render(request, 'shop.html', {
        'shop_items': shop_items,
    })

def tour(request):
    tours = Tour.objects.all()
    return render(request, 'tour.html', {
        'tours': tours,
    })


