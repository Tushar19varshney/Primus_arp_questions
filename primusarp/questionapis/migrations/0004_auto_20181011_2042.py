# Generated by Django 2.1.2 on 2018-10-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionapis', '0003_auto_20181011_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.TextField(default='No Information', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.TextField(default='No Information', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.TextField(default='No Information', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.TextField(default='No Information', max_length=100),
        ),
    ]
