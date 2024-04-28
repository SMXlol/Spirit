# Generated by Django 5.0.4 on 2024-04-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.FloatField()),
                ('fodder', models.FloatField()),
                ('readme', models.TextField()),
                ('image_url', models.URLField()),
                ('all_rating', models.FloatField(default=0)),
                ('rating', models.JSONField(default=list)),
                ('count_rate', models.IntegerField(default=0)),
                ('walk', models.BooleanField(default=False)),
                ('recommended_food', models.JSONField(default=list)),
                ('recommended_food_weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pet', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('pets', models.ManyToManyField(to='volunteer.pet')),
            ],
        ),
    ]