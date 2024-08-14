# Generated by Django 5.1 on 2024-08-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('tipId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('language', models.CharField(choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Java', 'Java'), ('C++', 'C++')], max_length=50)),
                ('tags', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
