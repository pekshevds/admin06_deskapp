from django.urls import path
from app.views import (index, project_content,
                       project_new, project_edit,
                       document_new, document_edit)

urlpatterns = [
    path('', index, name='show-index-page'),
    path('project/<str:project_id>/documents', project_content, name='show-project-documents-page'),

    path('project/<str:project_id>/edit', project_edit, name='show-project-edit-page'),
    path('project/new', project_new, name='show-project-new-page'),

    path('document/<str:document_id>/edit', document_edit, name='show-document-edit-page1'),
    path('document/new', document_new, name='show-document-new-page'),
]

"""path('project', project_content, name='show-project-documents-page'),
    path('project/<str:project_id>/delete', project_content, name='show-project-documents-page'),

    path('document/<str:document_id>', project_content, name='show-project-documents-page'),
    path('document/new', project_content, name='show-project-documents-page'),
    path('document/<str:document_id>/edit', project_content, name='show-project-documents-page'),
    path('document/<str:document_id>/delete', project_content, name='show-project-documents-page'),"""
