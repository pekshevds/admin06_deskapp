# Generated by Django 4.2.1 on 2023-05-30 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_document_created_alter_document_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='app.project', verbose_name='Проект'),
        ),
    ]
