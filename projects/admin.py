from django.contrib import admin
from . import models

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'language', 'url')
    list_filter = ('technology', 'language')
    search_fields = ['title', 'technology']


class ImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')
    search_fields = ['project__title']


class SertificatesAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ['title',]


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Images, ImageAdmin)
admin.site.register(models.Certificates, SertificatesAdmin)
