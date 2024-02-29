# Generated by Django 5.0.2 on 2024-02-27 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_exam'),
        ('library', '0002_alter_module_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=5)),
                ('correct', models.CharField(max_length=5)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.question')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(through='exam.Breakdown', to='library.question'),
        ),
        migrations.CreateModel(
            name='ExamModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('score', models.FloatField(default=0.0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='modules',
            field=models.ManyToManyField(through='exam.ExamModule', to='library.module'),
        ),
    ]
