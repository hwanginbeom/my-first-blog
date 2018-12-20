from django.db import models
from django.utils import timezone


# html이라는 정적인 페이지에 동적으로 정보를 주려면 데이터가 아닌 html에 맞게 줘야한다.
class Post(models.Model):  # 모델을 정의하는 코드 # Post라는 클래스명을 가지곤 있는곳에 models.model이라는 매개변수를 받는다.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # 이 뒤에 부분이 쿼리셋 부분이다.
    title = models.CharField(max_length=200)  #

    text = models.TextField()

    created_date = models.DateTimeField(
        default=timezone.now)

    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
