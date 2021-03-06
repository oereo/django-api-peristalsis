# Generated by Django 3.2 on 2021-04-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='post_images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('profileImage', models.CharField(default='/media/red.jpg', max_length=500)),
            ],
        ),
    ]
