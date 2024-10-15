# Generated by Django 5.1.1 on 2024-09-20 09:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the challenge', max_length=255)),
                ('points', models.IntegerField()),
                ('flag', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'challenge',
            },
        ),
        migrations.CreateModel(
            name='ChallengeSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=25, null=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='challenge.challenge')),
                ('contestant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'challenge_submissions',
            },
        ),
    ]