# Generated by Django 4.0.3 on 2022-03-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaaniapp', '0003_post_post_name_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_description',
            field=models.TextField(null=True),
        ),
    ]
