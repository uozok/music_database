from django.db import models

# Create your models here.

from django.db import models

class Label(models.Model):
    label = models.CharField(max_length=256, unique=True, blank=True)

    def __str__(self):
        return self.label

class Artist(models.Model):
    artist = models.CharField(max_length=256, unique=True, blank=True)

    def __str__(self):
        return self.artist

class Format(models.Model):
    format = models.CharField(max_length=64, unique=True, blank=True)

    def __str__(self):
        return self.format

class Album(models.Model):
    catalog_number = models.CharField(max_length=64, blank=True)  # 規格品番
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=256, blank=True)
    format = models.ForeignKey(Format, on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.PositiveIntegerField(blank=True, null=True)  # 発売日。0から99999999までの整数として扱う
    notes = models.TextField(blank=True)  # 備考
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True, blank=True)
    songs = models.TextField(blank=True)  # 収録曲
    performers = models.TextField(blank=True)  # 演奏者
    credits = models.TextField(blank=True)  # クレジット
    youtube_url = models.URLField(blank=True)
    spotify_url = models.URLField(blank=True)
    apple_music_url = models.URLField(blank=True)
    tower_records_music_url = models.URLField(blank=True)
    

    class Meta:
        unique_together = ('catalog_number', 'label')  # 同じレーベル内で規格品番が重複しないようにします。

    def __str__(self):
        return f"{self.catalog_number} - {self.artist.artist if self.artist else 'Unknown'} - {self.title}"

