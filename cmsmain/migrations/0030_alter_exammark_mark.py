# Generated by Django 5.0.2 on 2024-04-22 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0029_alter_exammark_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammark',
            name='mark',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]