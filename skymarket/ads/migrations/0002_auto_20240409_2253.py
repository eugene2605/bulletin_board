# Generated by Django 3.2.6 on 2024-04-09 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ('created_at',), 'verbose_name': 'объявление', 'verbose_name_plural': 'объявления'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_at',), 'verbose_name': 'отзыв', 'verbose_name_plural': 'отзывы'},
        ),
        migrations.AddField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='автор объявления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время и дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.TextField(default=None, verbose_name='описание товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='цена товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='title',
            field=models.CharField(default=' ', max_length=50, verbose_name='название товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='ad',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='ads.ad', verbose_name='объявление'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='автор отзыва'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время и дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=' ', verbose_name='текст отзыва'),
            preserve_default=False,
        ),
    ]