from django.shortcuts import get_object_or_404, render
from .models import Album
from django.db.models import Q
from .models import Album, NewsPost


def album_list(request):
    # HTTP_REFERERが存在し、それがアルバムの詳細ページからのものであれば、
    # セッションから検索ワードを取得する。
    if 'HTTP_REFERER' in request.META and '/album/' in request.META['HTTP_REFERER']:
        search_term = request.session.get('search_term', '')
    else:
        # リファラーがアルバム詳細ページでない場合、またはHTTP_REFERERがない場合、
        # GETリクエストから検索ワードを取得する。
        search_term = request.GET.get('search', '')
        # 取得した検索ワードをセッションに保存する。
        request.session['search_term'] = search_term

    albums = Album.objects.none()  # デフォルトで何も取得しない

    if search_term:
        albums = Album.objects.filter(
            Q(title__icontains=search_term) |
            Q(artist__artist__icontains=search_term) |
            Q(label__label__icontains=search_term) |
            Q(format__format__icontains=search_term) |
            Q(notes__icontains=search_term) |
            Q(keywords__icontains=search_term) |
            Q(songs__icontains=search_term)  # 収録曲での検索を追加
         
        )

    return render(request, 'label_list/album_list.html', {'albums': albums, 'search_term': search_term})


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    search_term = request.GET.get('search', '')
    meta_title = f"{album.title} by {album.artist.artist if album.artist else 'Unknown Artist'}"
    meta_description = f"{album.notes[:155]}..." if album.notes else "No description available."
    meta_image = request.build_absolute_uri(album.image.url) if album.image else None
    context = {
        'album': album,
        'search_term': search_term,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_image': meta_image,
    }
    return render(request, 'label_list/album_detail.html', context)

def news_list(request):
    news_posts = NewsPost.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'label_list/news_list.html', {'news_posts': news_posts})