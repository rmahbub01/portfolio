# Generated by Django 3.1.7 on 2021-03-18 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20210318_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='bullet1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='bullet2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='bullet3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='summary',
            name='bullet1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='summary',
            name='bullet2',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='summary',
            name='bullet3',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='summary',
            name='some_word',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Bullet',
        ),
    ]