# Generated by Django 4.2.1 on 2023-05-30 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Дата изменения')),
                ('created', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Дата изменения')),
                ('created', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Описание')),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='Содержимое')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Проект', to='app.project')),
            ],
        ),
    ]
