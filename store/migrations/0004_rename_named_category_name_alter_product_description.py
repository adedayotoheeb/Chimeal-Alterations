# Generated by Django 4.0.6 on 2022-07-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_is_availabele_product_is_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='named',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
