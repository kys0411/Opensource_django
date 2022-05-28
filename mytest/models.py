from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_content = models.CharField(max_length=200, default='')
    answer1 = models.CharField(max_length=100, default='')
    answer2 = models.CharField(max_length=100, default='')
    answer3 = models.CharField(max_length=100, default='')
    answer4 = models.CharField(max_length=100, default='')
    correct = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text
