# Generated by Django 4.0.3 on 2022-03-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaaniapp', '0008_alter_profile_neighbourhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
