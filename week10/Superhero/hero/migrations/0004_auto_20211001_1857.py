# Generated by Django 2.2.6 on 2021-10-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_auto_20211001_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='identity',
            field=models.CharField(default='Who is this??', max_length=100),
        ),
        migrations.AddField(
            model_name='hero',
            name='weakness',
            field=models.CharField(default='no Weaknesses?', max_length=100),
        ),
        migrations.AlterField(
            model_name='hero',
            name='description',
            field=models.TextField(default='Nothing to describe'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='strengths',
            field=models.CharField(default='No Strengths? Not much of a Superhero', max_length=100),
        ),
    ]