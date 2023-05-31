# Generated by Django 4.2.1 on 2023-05-31 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_document_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['name'], 'verbose_name': 'Исполнительный документ', 'verbose_name_plural': 'Исполнительная документация'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(db_index=True, max_length=150, unique=True, verbose_name='Наименование'),
        ),
    ]
