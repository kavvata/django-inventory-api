# Generated by Django 5.1.2 on 2024-10-30 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ativos', '0004_alter_software_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='version',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
