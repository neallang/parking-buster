# Generated by Django 5.0.2 on 2024-04-08 21:21

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_admin', models.BooleanField(default=False, help_text='Designates whether a user is treated as a site admin.')),
                ('website', models.URLField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=100, verbose_name='Report Subject (Required)')),
                ('status', models.CharField(choices=[('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='New', max_length=50)),
                ('license_plate', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='License Plate')),
                ('color', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Color')),
                ('make_model', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Make/Model')),
                ('location', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Location')),
                ('description', models.TextField(default='', verbose_name='Description (Required)')),
                ('supportDocs', models.FileField(blank=True, null=True, upload_to='', verbose_name='Upload files')),
                ('notes', models.TextField(blank=True, default='', null=True, verbose_name='Admin Notes')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advising_app.userprofile')),
            ],
        ),
    ]
