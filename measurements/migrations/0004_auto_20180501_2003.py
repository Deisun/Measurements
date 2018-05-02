# Generated by Django 2.0.4 on 2018-05-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0003_auto_20180501_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
