from django.shortcuts import get_object_or_404, render
from .models import Album
from django.db.models import Q
from .models import Album, NewsPost

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

def news_list(request):
    news_posts = NewsPost.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'label_list/news_list.html', {'news_posts': news_posts})