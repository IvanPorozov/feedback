
from django.db import models
from django.core.validators import RegexValidator


class Record(models.Model):
    username = models.CharField(max_length=100, verbose_name='User Name',
                                validators=[RegexValidator(r'^[a-zA-Z0-9]+$')])
    email = models.EmailField(verbose_name='E-mail')
    homepage = models.URLField(verbose_name='Home Page', blank=True, null=True)
    text = models.TextField(verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
