# Generated by Django 2.1.1 on 2019-04-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLWebService', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingtask',
            name='oid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trainingtask',
            name='traingName',
            field=models.CharField(max_length=200),
        ),
    ]