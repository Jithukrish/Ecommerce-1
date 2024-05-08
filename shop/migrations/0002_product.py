# Generated by Django 3.1.5 on 2024-01-02 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('colour', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('availability', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category')),
            ],
        ),
    ]