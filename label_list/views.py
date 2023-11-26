from django.shortcuts import get_object_or_404, render
from .models import Album
from django.db.models import Q
from .models import Album, NewsPost
from django.shortcuts import redirect

#review用
from .models import Album, NewsPost, Review
from .forms import ReviewForm

def album_list(request):

  #  request.session.clear()

    if 'HTTP_REFERER' in request.META and '/album/' in request.META['HTTP_REFERER']:
        search_term = request.session.get('search_term', '')
    else:
        search_term = request.GET.get('search', '')
        request.session['search_term'] = search_term

    if search_term:
        albums = Album.objects.all()
        query = None
        for term in search_term.split():
            q = Q(title__icontains=term) | \
                Q(artist__artist__icontains=term) | \
                Q(label__label__icontains=term) | \
                Q(format__format__icontains=term) | \
                Q(notes__icontains=term) | \
                Q(keywords__icontains=term) | \
                Q(songs__icontains=term)

            if query is None:
                query = q
            else:
                query = query & q

        albums = albums.filter(query) if query else albums
    else:
        albums = Album.objects.none()  # 検索語がない場合は何も取得しない

 # セッションから最近訪れたアルバムを取得
 #   recent_albums_ids = [id for id in request.session.get('recent_albums', []) if isinstance(id, int)]
 #    recent_albums = Album.objects.filter(id__in=recent_albums_ids)

    recent_albums_ids = request.session.get('recent_albums', [])
    recent_albums = Album.objects.filter(id__in=recent_albums_ids)

    return render(request, 'label_list/album_list.html', {
        'albums': albums, 
        'search_term': search_term,
        'recent_albums': recent_albums,# 追加
        })


#review追加
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    # レビュー投稿フォームの処理
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.album = album
            review.save()
            return redirect('album_detail', album_id=album_id)
    else:
        form = ReviewForm()

    # アルバムに対する全てのレビューを取得
    reviews = Review.objects.filter(album=album).order_by('-created_date')

    # 既存のメタデータおよび検索語
    search_term = request.GET.get('search', '')
    meta_title = f"{album.title} by {album.artist.artist if album.artist else 'Unknown Artist'}"
    meta_description = f"{album.notes[:155]}..." if album.notes else "No description available."
    meta_image = request.build_absolute_uri(album.image.url) if album.image else None

    # コンテキストにレビュー関連の情報を追加
    context = {
        'album': album,
        'form': form,  # レビュー投稿フォーム
        'reviews': reviews,  # 投稿されたレビュー
        'search_term': search_term,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_image': meta_image,
    }

    # 最近訪れたアルバムをセッションに保存
    recent_albums = request.session.get('recent_albums', [])
    if album_id not in recent_albums:
        recent_albums.insert(0, album_id)
        if len(recent_albums) > 5:  # 例えば、最新の5件を保持
            recent_albums.pop()
    request.session['recent_albums'] = recent_albums

    return render(request, 'label_list/album_detail.html', context)


def news_list(request):
    news_posts = NewsPost.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'label_list/news_list.html', {'news_posts': news_posts})