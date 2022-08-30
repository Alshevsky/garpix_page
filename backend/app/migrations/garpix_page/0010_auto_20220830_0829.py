# Generated by Django 3.1 on 2022-08-30 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_page', '0009_basecomponent_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecomponent',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_components', to='garpix_page.basecomponent', verbose_name='Компонент'),
        ),
        migrations.AlterField(
            model_name='pagecomponent',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_components', to='garpix_page.basepage', verbose_name='Страница'),
        ),
    ]
