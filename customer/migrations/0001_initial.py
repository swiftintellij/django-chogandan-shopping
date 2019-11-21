# Generated by Django 2.2.7 on 2019-11-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
            ],
            options={
                'verbose_name': '고객',
                'verbose_name_plural': '고객',
                'db_table': 'customer',
            },
        ),
    ]