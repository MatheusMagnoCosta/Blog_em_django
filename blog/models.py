from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.CharField(max_length=255)
    conteudo = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo