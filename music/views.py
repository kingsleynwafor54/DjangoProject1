from django.http import HttpResponse
from django.template import loader

from music.models import Album


def index(request):
    all_albums=Album.objects.all()
    # html=""
    # for album in all_albums:
    #     url='/music/' + str(album.id) +'/'
    #     html+='<a href="' + url + '">' + album.album  +'</a><br>'
    template=loader.get_template("music/index.html")
    context={
        "all_albums":all_albums
    }
    return HttpResponse(template.render(context,request))


def detail(request,album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")