import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

def _get_next_day():
    next_day = datetime.datetime.now() + datetime.timedelta(days=1)
    return next_day

class Note(models.Model):

    # STATE = (  # todo models.IntegerChoices
    #     (0, 'Активно'),
    #     (1, 'Отложено'),
    #     (2, 'Выполнено'),
    # )

    class STATE(models.IntegerChoices):
        ACTIVE = 0, _('Активно')
        NOT_ACTIVE = 1, _('Отложено')
        DONE = 2, _('Выполнено')


    title = models.CharField(max_length=255, verbose_name='Заголовок')
    desc = models.TextField(default='', verbose_name='Описание')
    state = models.IntegerField(default=STATE.ACTIVE, choices=STATE.choices, verbose_name='Состояние')
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    important = models.BooleanField(default=False, verbose_name='Важное')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    pub_date = models.DateTimeField(auto_now=_get_next_day, verbose_name='Дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

