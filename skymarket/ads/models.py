from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='название товара')
    price = models.PositiveIntegerField(verbose_name='цена товара')
    description = models.TextField(verbose_name='описание товара')
    image = models.ImageField(upload_to='ads/', null=True, blank=True, verbose_name='изображение товара')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, verbose_name='автор объявления')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='время и дата создания')

    def __str__(self):
        return f'Продается {self.title} по цене {self.price}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ('-created_at',)


class Comment(models.Model):
    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, verbose_name='автор отзыва')
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE, blank=True, verbose_name='объявление')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='время и дата создания')

    def __str__(self):
        return f'Отзыв {self.author} на объявление {self.ad}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ('created_at',)
