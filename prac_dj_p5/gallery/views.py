from django.shortcuts import render
from .models import Album
from .forms import AlbumForm

# Create your views here.
def gallery(request):
    if request.method == 'POST':
        forms = AlbumForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
    album = Album.objects.all()
    forms = AlbumForm()
    return render(request, 'gallery/gallery.html', {
        'album': album,
        'forms': forms,
    })