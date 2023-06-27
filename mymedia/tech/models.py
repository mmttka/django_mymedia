from django.db import models

class TechModel(models.Model):
    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('テキスト')
    thumbnail = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    #今後カテゴリ追加

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    