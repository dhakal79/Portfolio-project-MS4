# Generated by Django 3.2.12 on 2022-02-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(),
        ),
    ]
