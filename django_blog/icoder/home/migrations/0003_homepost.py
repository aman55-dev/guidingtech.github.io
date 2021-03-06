# Generated by Django 3.0.7 on 2020-06-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='homePost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('auther', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
