# Generated by Django 4.2.17 on 2025-01-04 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_views', models.IntegerField(default=0)),
                ('animal_likes', models.IntegerField(default=1)),
                ('animal_name', models.CharField(max_length=255)),
                ('animal_description', models.TextField()),
                ('animal_slug', models.SlugField(max_length=255, unique=True)),
                ('animal_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalBreed',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_breed', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalColor',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_color', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalLocation',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_location', models.CharField(max_length=255)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='App.animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalImages',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_image', models.ImageField(upload_to='Animals/')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='App.animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_breed',
            field=models.ManyToManyField(blank=True, to='App.animalbreed'),
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='App.category'),
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_color',
            field=models.ManyToManyField(blank=True, to='App.animalcolor'),
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to=settings.AUTH_USER_MODEL),
        ),
    ]
