# Generated by Django 4.1 on 2022-09-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        ('mohdrate_DB', '0002_session_db_time_zone_alter_session_db_seen_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_db',
            name='akhtbar',
            field=models.ManyToManyField(blank=True, null=True, to='auth_app.akhtbar'),
        ),
    ]
