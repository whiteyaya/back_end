# Generated by Django 4.1.2 on 2022-11-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='down_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='up_num',
            field=models.IntegerField(default=0),
        ),
    ]
