# Generated by Django 3.2.7 on 2021-09-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postimage',
            field=models.ImageField(default='default/blog-1.jpg', upload_to='image/'),
        ),
    ]