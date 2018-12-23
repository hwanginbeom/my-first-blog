from django.conf.urls import url

from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings
from .views import ApiEndpoint

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), ## r'^ 기본 url에 post 방식에 pk를 받아온다.
    url(r'^post/new/$', views.post_new, name='post_new'),##그다음 views.post.new로 넘겨준다.
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^join/$', views.join, name='signup'), ## views에서 join 부분으로 간다. signup은 정해져 있는 명령어 같은 느낌
    url(r'^login/$', views.signin, name='login'),

##^은 "시작"을 뜻합니다.
##post/란 URL이 post 문자를 포함해야 한다는 것
## (?P<pk>\d+)는 조금 까다롭습니다.
## 이 정규표현식은 장고가 pk변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻입니다.
#  \d은 문자를 제외한 숫자 0부터 9 중, 한 가지 숫자만 올 수 있다는 것을 말합니다.
#  +는 하나 또는 그 이상의 숫자가 올 수 있습니다.. 따라서 http://127.0.0.1:8000/post/라고 하면
## /은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
## $는 "마지막"을 말합니다. 그 뒤로 더는 문자가 오면 안 됩니다.
]
