# Generated by Django 2.2.1 on 2019-05-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='Comments',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
