# Generated by Django 2.2.12 on 2023-01-05 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('skill_id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=10)),
                ('skill_domain', models.CharField(max_length=10)),
                ('skill_level', models.CharField(max_length=10)),
                ('skill_exp', models.CharField(max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
