# Generated by Django 4.0.3 on 2022-03-18 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtaani_name', models.CharField(max_length=30, null=True)),
                ('mtaani_location', models.CharField(max_length=30, null=True)),
                ('mtaani_occupants', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mtaaniapp.neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(null=True, upload_to='posts/')),
                ('post_description', models.TextField(null=True)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mtaaniapp.neighbourhood')),
                ('profile_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mtaaniapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_contact', models.CharField(max_length=30, null=True)),
                ('hospital_contact', models.CharField(max_length=30, null=True)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mtaaniapp.neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30, null=True)),
                ('business_email', models.EmailField(max_length=254, null=True)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mtaaniapp.neighbourhood')),
            ],
        ),
    ]
