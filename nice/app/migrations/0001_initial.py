# Generated by Django 2.2.2 on 2019-10-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrugIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=100, verbose_name='Trade Name')),
                ('generic_name', models.CharField(max_length=100, verbose_name='Generic Name')),
                ('uses', models.TextField(default='', verbose_name='Uses')),
                ('dosage', models.TextField(default='', verbose_name='Dosage')),
                ('img', models.ImageField(default='default.jpg', upload_to='drugimg', verbose_name='Drug Images')),
            ],
            options={
                'ordering': ('-trade_name',),
            },
        ),
    ]