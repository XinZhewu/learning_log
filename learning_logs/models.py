from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    # 用户学习的主题
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # 返回模型的字符串表示
        return self.text


class Entry(models.Model):
    # 学到的某个主题的知识
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # 返回模型的字符串表示
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:50] + '...'


class Pizza(models.Model):
    # pizzeria项目中的pizzas应用中的披萨模型被放在这里
    name = models.CharField(max_length=200)
    date_added_0 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    # 同上,这是配料模型
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added_0 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.name) <= 50:
            return self.name
        else:
            return self.name[:50] + '...'
