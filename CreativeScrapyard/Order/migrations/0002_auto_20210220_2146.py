# Generated by Django 3.1.4 on 2021-02-20 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0002_auto_20210220_2146'),
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_orders_details',
            name='crt_item_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Items.tbl_creativeitems_mst'),
        ),
    ]