# Generated by Django 3.1.5 on 2024-03-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0004_auto_20240303_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('PRESENT', 'PRESENT'), ('NEW', 'NEW')], default='PRESENT', max_length=50),
        ),
    ]
