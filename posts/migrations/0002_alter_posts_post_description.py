# Generated by Django 4.2.7 on 2024-03-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
