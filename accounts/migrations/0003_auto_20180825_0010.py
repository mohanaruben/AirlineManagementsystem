# Generated by Django 2.0.1 on 2018-08-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='coach',
            new_name='flight',
        ),
        migrations.AddField(
            model_name='book',
            name='tclass',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
