from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Women(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    content = models.TextField(blank=True,verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,null=True,verbose_name='Категория')
    slug = AutoSlugField(populate_from='title',null=True,verbose_name='URL',unique=True,editable=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug}) #вернет url   site/post/post_id

    class Meta: #класс meta нужен для админ панели
        verbose_name = 'Известные актеры' #название в единственном числе с добавлением s в коцне
        verbose_name_plural = 'Известные актеры' #название в множественном числе
        ordering = ['title','time_create'] #сортировка по параметрам по порядку||работает не только для админки но и для сайта
        #если значения равные то сортируется по последующим параметрам||
        # мождно указать - в начале элемента списка чтобы сортировка пошла наоборот'''

    

class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True,verbose_name='Категория')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk}) # абсолютный url будет равен self.pk каждого экземпляра класса category(каждой записи),можно изменить на любой аттрибут маршрут с именем category||cat_id будет подставлен по шаблону из url category/<int:cat_id> вернет url  site/category/cat_id
    
    class Meta: #класс meta нужен для админ панели
        verbose_name = 'Категория' #название в единственном числе с добавлением s в коцне
        verbose_name_plural = 'Категории' #название в множественном числе
        ordering = ['id'] #сортировка по параметрам по порядку||работает не только для админки но и для сайта
        #если значения равные то сортируется по последующим параметрам||
        # мождно указать - в начале элемента списка чтобы сортировка пошла наоборот'''