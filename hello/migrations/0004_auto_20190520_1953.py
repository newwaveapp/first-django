# Generated by Django 2.2.1 on 2019-05-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20190520_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='Entry',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='Tags',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Entries',
        ),
        migrations.DeleteModel(
            name='TagModel',
        ),
    ]
