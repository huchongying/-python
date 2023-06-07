# Generated by Django 3.2 on 2023-05-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nike_name', models.CharField(blank=True, default='', max_length=50, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], max_length=6, verbose_name='性别')),
                ('adress', models.CharField(blank=True, max_length=100, verbose_name='地址')),
            ],
            options={
                'verbose_name': '用户数据',
                'verbose_name_plural': '用户数据',
            },
        ),
    ]
