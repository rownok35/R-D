from django.contrib import admin
from .models import year_publications, Publication
# Register your models here.

class admin_publication(admin.ModelAdmin):
    list_display = ('authors', 'title', 'document_type', 'publishing_year' )
    list_display_links = ('authors', 'title', 'document_type', 'publishing_year' )
    search_fields = ('authors', 'title', 'document_type', 'publishing_year')
    list_filter = ('document_type', 'publishing_year')


admin.site.register(year_publications)
admin.site.register(Publication, admin_publication)