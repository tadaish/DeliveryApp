# Generated by Django 4.2 on 2023-04-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_address',
            field=models.TextField(null=True, verbose_name='from'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Huỷ '), (1, 'Hoàn Thành'), (2, 'Đang Giao')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_address',
            field=models.TextField(null=True, verbose_name='to'),
        ),
    ]
