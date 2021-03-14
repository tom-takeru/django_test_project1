# models.py
from django.db import models


class Tag(models.Model):
    name = models.CharField(
        verbose_name='タグ名',
        max_length=127,
    )
    def __str__(self):
        return self.name

class Memo(models.Model):
    title = models.CharField(
        verbose_name='タイトル',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='本文',
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='タグ',
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='作成日時',
        auto_now=True,
    )

    def __str__(self):
        return self.title
