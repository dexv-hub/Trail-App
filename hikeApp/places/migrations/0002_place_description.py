# Generated by Django 4.2.20 on 2025-06-02 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
