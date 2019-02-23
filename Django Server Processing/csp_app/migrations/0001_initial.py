# Generated by Django 2.1.3 on 2019-01-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='')),
                ('p_img', models.ImageField(null=True, upload_to='images/', verbose_name='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
