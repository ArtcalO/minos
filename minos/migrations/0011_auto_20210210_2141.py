# Generated by Django 3.1.3 on 2021-02-10 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minos', '0010_auto_20210210_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ulttoken',
            name='token_bank_number2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='minos.banktokenpaid'),
        ),
    ]
