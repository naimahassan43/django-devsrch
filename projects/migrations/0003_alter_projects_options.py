# Generated by Django 4.0 on 2022-01-01 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projects_options_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
