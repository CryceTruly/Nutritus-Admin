# Generated by Django 2.1.7 on 2019-04-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_auto_20190430_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendedfood',
            name='agegroup',
            field=models.CharField(choices=[('0-12 Months', '0-12 Months'), ('1-2 Years', '1-2 Years'), ('2-3 Years', '2-3 Years')], default='2-3 Years', max_length=255),
        ),
    ]