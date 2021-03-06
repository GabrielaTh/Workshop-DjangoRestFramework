# Generated by Django 2.1.7 on 2019-02-23 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequence', models.IntegerField()),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomIncident', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Motivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeIncidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomType', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='incidents',
            name='idTypeIncidents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.TypeIncidents'),
        ),
        migrations.AddField(
            model_name='detail',
            name='idIncidents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.Incidents'),
        ),
        migrations.AddField(
            model_name='detail',
            name='idTransport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.Transports'),
        ),
        migrations.AddField(
            model_name='detail',
            name='motivation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.Motivation'),
        ),
        migrations.AddField(
            model_name='detail',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
