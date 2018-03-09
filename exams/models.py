from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name="tests", on_delete=models.CASCADE)


QUESTION_TYPES = [('mc', 'Multiple Choice')]

class Question(models.Model):
    type = models.CharField(choices=QUESTION_TYPES, max_length=10, default='mc')
    question = models.TextField()
    answers = models.TextField()
    score = models.PositiveSmallIntegerField()
    test = models.ForeignKey(Test, related_name="questions", on_delete=models.CASCADE)