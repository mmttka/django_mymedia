from django.db import models

class TermModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)
    #今後カテゴリも追加

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    