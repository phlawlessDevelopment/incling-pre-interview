from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    order = models.IntegerField()
    
    class task_types(models.TextChoices):
        SURVEY = 'survey', 'Survey'
        DISCUSSION = 'discussion', 'Discussion'
        DIARY = 'diary', 'Diary'

    _type = models.CharField(choices=task_types.choices, max_length=20, default=task_types.SURVEY)
    tile = models.ForeignKey('Tile', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f'{self.title} - {self._type}'

class Tile(models.Model):
    launch_date = models.DateField()

    class statuses(models.TextChoices):
        LIVE = 'live', 'Live'
        PENDING = 'pending', 'Pending'
        ARCHIVED = 'archived', 'Archived'
    
    status = models.CharField(choices=statuses.choices, max_length=20, default=statuses.PENDING)

    def __str__(self):
        return f'{self.launch_date} - {self.status}'
