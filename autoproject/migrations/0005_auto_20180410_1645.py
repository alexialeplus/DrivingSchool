# Generated by Django 2.0.4 on 2018-04-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoproject', '0004_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forfait',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='paid_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Forfait',
        ),
    ]
