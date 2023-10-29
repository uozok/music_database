from django.shortcuts import get_object_or_404, render
from .models import Album
from django.db.models import Q

def album_list(request):
    search_term = request.GET.get('search', '')
    albums = Album.objects.none()  # これにより、デフォルトで何も取得しない
    
    # 検索ワードが存在する場合のみ、アルバムを検索・フィルタリングする
    if search_term:
        albums = Album.objects.filter(
            Q(title__icontains=search_term) |
            Q(artist__artist__icontains=search_term) |
            Q(label__label__icontains=search_term) |
            Q(format__format__icontains=search_term) |
            Q(notes__icontains=search_term)  
        )
    return render(request, 'label_list/album_list.html', {'albums': albums, 'search_term': search_term})


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    search_term = request.GET.get('search', '')  # 追加
    return render(request, 'label_list/album_detail.html', {'album': album, 'search_term': search_term})  # search_termを追加
