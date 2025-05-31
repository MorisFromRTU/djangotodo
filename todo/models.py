from django.db import models

class Task(models.Model):
    title = models.CharField('Задача', max_length=200)
    completed = models.BooleanField('Выполнено', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'