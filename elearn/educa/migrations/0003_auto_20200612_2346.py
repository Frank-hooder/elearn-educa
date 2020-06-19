# Generated by Django 3.0.6 on 2020-06-13 06:46

from django.db import migrations
import educa.fields


class Migration(migrations.Migration):

    dependencies = [
        ('educa', '0002_content_file_image_text_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=educa.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=educa.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
