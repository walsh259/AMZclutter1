# Generated by Django 3.0.5 on 2020-04-19 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clutter', '0004_designer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('number', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Trademark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('number', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='asin',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='carton_height',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='carton_length',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='carton_weight',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='carton_width',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ean',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='lead_time',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='notes',
            field=models.TextField(max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prep_fees',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='units_carton',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipmark',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipmarks', to='clutter.Shipmark'),
        ),
        migrations.AddField(
            model_name='product',
            name='trademark',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trademarks', to='clutter.Trademark'),
        ),
    ]
