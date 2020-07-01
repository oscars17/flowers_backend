# Generated by Django 3.0.7 on 2020-06-27 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text_materials', '0003_article_important'),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerimage',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='header_image', to='text_materials.Article', verbose_name='article'),
        ),
    ]
