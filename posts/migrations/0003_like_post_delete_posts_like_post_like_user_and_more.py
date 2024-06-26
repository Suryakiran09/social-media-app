# Generated by Django 4.2.7 on 2024-03-30 10:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inst_profile', '0002_alter_profile_date_of_birth'),
        ('posts', '0002_alter_posts_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_description', models.CharField(blank=True, max_length=500, null=True)),
                ('post_image', models.ImageField(upload_to='posts')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='inst_profile.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='inst_profile.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post')},
        ),
    ]
