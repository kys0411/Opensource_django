# Generated by Django 4.0.4 on 2022-05-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0002_question_answer1_question_answer2_question_answer3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_content',
            field=models.CharField(default='', max_length=200),
        ),
    ]
