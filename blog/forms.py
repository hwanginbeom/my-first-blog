from django import forms ##장고내부에 있는 forms를 넣는다.
from .models import Post ## models 파일에 있는 Post 클래스를 넣는다.
from django.contrib.auth.models import User
##장고 안에 있는 django.contrib.auth.models에 있는 User를 넣는다.
##auth - 회원 가입 구현하기

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def save(self, commit=True):  # 저장하는 부분 오버라이딩
            user = super(UserForm, self).save(commit=False)  # 본인의 부모를 호출해서 저장하겠다.
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']  # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.