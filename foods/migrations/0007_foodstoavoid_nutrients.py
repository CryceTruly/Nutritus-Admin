# Generated by Django 2.1.7 on 2019-04-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_auto_20190429_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodstoavoid',
            name='nutrients',
            field=models.ManyToManyField(related_name='_foodstoavoid_nutrients_+', to='foods.FoodsToAvoid'),
        ),
    ]
