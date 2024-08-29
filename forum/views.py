
# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from .models import Forum, Discusion, Post, User
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum/forum_list.html', {'forums': forums})

def discusions_list(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    discusions = Discusion.objects.filter(forum=forum)
    return render(request, 'forum/discusions_list.html', {'forum': forum, 'discusions': discusions})

def post_list(request, discusion_id):
    discusion = get_object_or_404(Discusion, id=discusion_id)
    posts = Post.objects.filter(discussion=discusion).order_by('-created_at')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'forum/post_list.html', {'discusion': discusion, 'posts': posts})

def add_post(request, discusion_id):
    discusion = get_object_or_404(Discusion, id=discusion_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:  # Vérifie si le contenu n'est pas vide
            post = Post(
                content=content,
                discussion=discusion,
                created_by=request.user if request.user.is_authenticated else None
            )
            post.save()
            return redirect('forum:post_list', discusion_id=discusion.id)
    return render(request, 'forum/add_post.html', {'discusion': discusion})

# def add_post(request,discusion_id):
#     discusion = get_object_or_404(Discusion, id=discusion_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.discussion = discusion
#             post.created_by = request.user
#             post.save()
#             return redirect('forum:post_list', discusion_id=discusion.id)
#     else:
#         form = PostForm()
#     return render(request, 'forum/add_post.html', {'discusion': discusion, 'form': form})