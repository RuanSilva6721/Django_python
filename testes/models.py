from django.db import models

class Teste(models.Model):

    STATUS = (
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length= 5,
        choices= STATUS,

    )
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

