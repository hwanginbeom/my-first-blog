from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



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
            post.auㅂthor = request.user # author 사용자계정
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
