# Generated by Django 5.1.5 on 2025-01-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('noticias', '0002_delete_noticia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
