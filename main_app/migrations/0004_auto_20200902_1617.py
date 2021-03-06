# Generated by Django 3.1 on 2020-09-02 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200902_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='finch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.finch'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='feeding date'),
        ),
    ]
