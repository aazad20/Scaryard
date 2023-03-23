# Generated by Django 3.1.4 on 2021-02-20 18:00

import Items.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_delete_tbl_creativeitems_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_crtimages',
            name='crt_img_url',
            field=models.ImageField(max_length=150, null=True, upload_to=Items.models.product_photo, validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]
