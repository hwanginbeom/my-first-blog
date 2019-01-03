
from .forms import UserForm
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404 ,redirect
from .forms import PostForm

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate




def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        data = {'username': request.user.username}
        if user is not None:
            login(request, user)
            return redirect('post_list') # 로그인이 되면 post로 넘어가게 끔
        else:
            return redirect('post_list')
    else:
        form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})



def loggedout(request):
    logout(request)
    return redirect('login')

# 여기서 재귀함수가 걸린이유는 logout이라는 함수와 이름이 같아 내가
# 생각한 기능으로 가지 않고 계속 해서 자기 자신을 부르는 무한루프에 빠져서 이다.


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})




def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid(): # 폼에 내용이 없으면
            new_user = User.objects.create_user(**form.cleaned_data) # new_user라는 것을 만드는데  form에 있는 데이터에  creat_user를 이용하여 넣어 만든다.
            login(request, new_user) # 만든 아이디로 로그인을 해준다.
            return redirect('post_list')
    else:
        form = UserForm()
    return render(request, 'blog/adduser.html', {'form': form}) # 폼 형태를 가지고 adduser.html로 던져준다.




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#쿼리셋
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})






def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # 아까 말씀하신 데이터베이스쪽과 연결 된 Post고 pk=pk 게시판 글 번호
    ## get_object_or_404() 함수는 장고 모델을 첫 번째 인자로 받습니다.
    # 두 번째 인자로는 키워드 인자를 받고 모델 메니저의 get() 함수에 전달합니다.
    # 그리고 이 모델 메니저는 오브젝트가 존재하지 않을 경우에 Http404 예외를 발생시킵니다.
    if request.method == "POST":    # POST 방식으로 받으면 바로 렌더 해버린다.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # request.POST : 폼 인스턴스 초기 데이터
            post = form.save(commit=False) # 중복 DB save를 방지
            post.author = request.user # author 사용자계정
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

