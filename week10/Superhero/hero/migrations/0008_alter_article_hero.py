# Generated by Django 3.2.6 on 2021-10-25 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0007_auto_20211023_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.hero'),
        ),
    ]