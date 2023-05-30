from django.contrib import admin
from app.models import Project
from app.models import Document


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name', )


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated', 'project',)
    search_fields = ('name', )
    list_filter = ['project']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
