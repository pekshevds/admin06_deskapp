from django.db import models
import uuid


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Наименование', max_length=150, db_index=True, unique=True)
    description = models.CharField(verbose_name='Описание', max_length=1024, blank=True, null=True, default='')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Наименование', max_length=150, db_index=True)
    description = models.CharField(verbose_name='Описание', max_length=1024, blank=True, null=True, default='')
    content = models.TextField(verbose_name='Содержимое', blank=True, null=True, default='')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    project = models.ForeignKey(Project, verbose_name='Проект', related_name='projects', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Исполнительный документ"
        verbose_name_plural = "Исполнительная документация"
