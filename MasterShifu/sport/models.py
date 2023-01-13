from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import now


class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    view = models.ForeignKey('View', on_delete=models.PROTECT, verbose_name="Вид единоборств")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    price = models.PositiveIntegerField(default=2000, verbose_name="Цена")
    hall_number = models.PositiveIntegerField(verbose_name="Номер зала")
    max_numb = models.PositiveIntegerField(verbose_name="Максимум")
    numb = models.PositiveIntegerField(auto_created=True, default=0, verbose_name="Текущее")
    duration = models.PositiveIntegerField(default=90, verbose_name="Длительность")
    photo = models.ImageField(upload_to="sections", verbose_name="Фото")
    trainer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Тренер")
    days = models.ManyToManyField('Days', verbose_name="Дни проведения")
    start_time = models.TimeField(verbose_name="Время начала")
    is_action = models.BooleanField(default=True, blank=True, verbose_name="Активно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.name + self.view.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'sec_slug': self.slug})

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'
        ordering = ['time_create']


class View(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view', kwargs={'view_slug': self.slug})

    class Meta:
        verbose_name = 'Вид единоборства'
        verbose_name_plural = 'Виды единоборств'
        ordering = ['name']


class Days(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни нендели'
        ordering = ['id']


class Records(models.Model):
    section = models.ForeignKey('Section', on_delete=models.PROTECT, verbose_name="Секция")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Тренирующийся")
    start_date = models.DateField(verbose_name="Дата начала")
    is_paid = models.BooleanField(default=False, verbose_name="Оплата")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.user.username + str(self.section.view)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['id']
