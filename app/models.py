from django.db import models


STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделанно'),
]

class Task(models.Model):
    description = models.TextField('Описание')
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
    )
    due_date = models.DateField('Дата выполнения')

    class Meta:
        ordering = ['due_date', 'id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.description[:50]
