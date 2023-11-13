from django.contrib import admin

# Register your models here.

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Artist, Format, Label, Album
from .models import NewsPost
from .models import Review


@admin.register(Artist)
class ArtistAdmin(ImportExportModelAdmin):
    list_display = ['id', 'artist']

@admin.register(Format)
class FormatAdmin(ImportExportModelAdmin):
    list_display = ['id', 'format']

@admin.register(Label)
class LabelAdmin(ImportExportModelAdmin):
    list_display = ['id', 'label']

@admin.register(Album)
class AlbumAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'artist', 'format', 'label', 'catalog_number', 'release_date', 'credits', 'keywords']

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # 一覧に表示するフィールド
    search_fields = ['title', 'text']  # 検索フィールド

admin.site.register(NewsPost, NewsPostAdmin)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('album', 'reviewer_name', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('album__title', 'reviewer_name')

