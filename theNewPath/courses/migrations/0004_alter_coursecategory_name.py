# Generated by Django 4.2.17 on 2024-12-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_coursecategory_alter_courses_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]