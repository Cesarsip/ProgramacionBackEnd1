from django.db import models

# Create your models here.
class programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.fullname} ({self.nickname}) - {self.language}"

    class Meta:
        verbose_name = "Programador"
        verbose_name_plural = "Programadores"
