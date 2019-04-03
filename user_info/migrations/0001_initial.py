# Generated by Django 2.1.7 on 2019-03-31 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='GroupKind',
            fields=[
                ('kid', models.AutoField(primary_key=True, serialize=False)),
                ('shortName', models.CharField(max_length=4, unique=True)),
                ('fullName', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('langCode', models.CharField(max_length=4, unique=True)),
                ('cname', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=32, unique=True)),
                ('desciption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=64, unique=True)),
                ('nickname', models.CharField(max_length=64)),
                ('userSex', models.CharField(max_length=6)),
                ('userPhoto', models.CharField(max_length=1000)),
                ('skill', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=320)),
                ('description', models.CharField(max_length=72)),
                ('groupKind',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='users',
                     to='user_info.GroupKind')),
                ('lang',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='users',
                     to='user_info.Lang')),
            ],
        ),
    ]