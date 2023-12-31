# Generated by Django 4.1.2 on 2023-06-24 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("tech", "0002_techmodel_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="techmodel",
            name="created_at",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name="作成日"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="techmodel",
            name="updated_at",
            field=models.DateField(auto_now=True, verbose_name="更新日"),
        ),
        migrations.AlterField(
            model_name="techmodel",
            name="text",
            field=models.TextField(verbose_name="テキスト"),
        ),
        migrations.AlterField(
            model_name="techmodel",
            name="title",
            field=models.CharField(max_length=100, verbose_name="タイトル"),
        ),
    ]
