# Generated by Django 3.1.7 on 2021-03-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20210319_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(height_field=2048, upload_to='', width_field=2048),
        ),
        migrations.AlterField(
            model_name='about',
            name='profile_img',
            field=models.ImageField(height_field=2048, null=True, upload_to='', width_field=2048),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(height_field=2048, upload_to='', width_field=2048),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(height_field=2048, upload_to='', width_field=2048),
        ),
    ]
