# Generated by Django 3.0.6 on 2020-06-16 05:12

from django.db import migrations, models
import django.db.models.deletion
import educa.fields


class Migration(migrations.Migration):

    dependencies = [
        ('educa', '0005_ads'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('resource', models.FileField(upload_to='files')),
                ('text_description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Ads_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', educa.fields.OrderField(blank=True)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='educa.Ad')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.DeleteModel(
            name='Ads',
        ),
    ]
