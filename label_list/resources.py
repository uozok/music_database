
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Label, Artist, Format, Album

class AlbumResource(resources.ModelResource):
    artist = fields.Field(
        column_name='artist',
        attribute='artist',
        widget=ForeignKeyWidget(Artist, 'id')  # 'id'を参照
    )
    format = fields.Field(
        column_name='format',
        attribute='format',
        widget=ForeignKeyWidget(Format, 'id')  # 'id'を参照
    )
    label = fields.Field(
        column_name='label',
        attribute='label',
        widget=ForeignKeyWidget(Label, 'id')  # 'id'を参照
    )

    class Meta:
        model = Album
        fields = ('id', 'artist', 'title', 'format', 'release_date', 'notes', 'label', 'catalog_number')

class LabelResource(resources.ModelResource):
    class Meta:
        model = Label
        fields = ('id', 'label')

class ArtistResource(resources.ModelResource):
    class Meta:
        model = Artist
        fields = ('id', 'artist')

class FormatResource(resources.ModelResource):
    class Meta:
        model = Format
        fields = ('id', 'format')

