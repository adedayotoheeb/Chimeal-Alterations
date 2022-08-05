# Generated by Django 4.0.6 on 2022-08-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_product_alter_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('P', 'Pending'), ('SH', 'Shipping'), ('C', 'Complete')], default='P', max_length=100),
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(blank=True, to='store.comment'),
        ),
    ]