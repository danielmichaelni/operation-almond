# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodmarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.DecimalField(max_digits=3, decimal_places=1)),
                ('price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('allergy_info', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NowOrderDish',
            fields=[
                ('dish_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='foodmarket.Dish')),
                ('num_for_sale', models.IntegerField()),
            ],
            options={
            },
            bases=('foodmarket.dish',),
        ),
        migrations.CreateModel(
            name='PreOrderDish',
            fields=[
                ('dish_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='foodmarket.Dish')),
                ('deadline_to_order', models.DateTimeField()),
                ('availability_date', models.DateTimeField()),
                ('num_available', models.IntegerField()),
            ],
            options={
            },
            bases=('foodmarket.dish',),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('dish', models.ForeignKey(to='foodmarket.Dish')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.DecimalField(max_digits=3, decimal_places=1)),
                ('user', models.OneToOneField(to='foodmarket.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dish',
            name='vendor',
            field=models.ForeignKey(to='foodmarket.Vendor'),
            preserve_default=True,
        ),
    ]
