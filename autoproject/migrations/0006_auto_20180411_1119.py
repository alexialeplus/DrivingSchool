# Generated by Django 2.0.4 on 2018-04-11 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoproject', '0005_auto_20180410_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_appointment', to='autoproject.Student'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_appointment', to='autoproject.Teacher'),
        ),
    ]
