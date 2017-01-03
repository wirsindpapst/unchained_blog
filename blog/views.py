from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Like, Category
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
# Additional imports for users:
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from .forms import RegistrationForm, CommentForm, CategoryForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template.context import RequestContext
from django.db.models import Count


#profile
from .models import Blogger
from .forms import UserForm, ProfileForm

try:
    from django.utils import simplejson as json
except ImportError:
    import json

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_draft_list(request):
    posts = Post.objects.filter( author__in=[request.user.id], published_date__isnull=True).order_by('created_date').reverse()
    if posts.count() == 0:
        return render(request, 'blog/post_draft_list.html', {'posts': None})
    else:
        return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.id == post.author_id:
        post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.id == post.author_id:
        post.delete()
    return redirect('post_list')

def post_detail(request, pk):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = get_object_or_404(Post, pk=pk)
            new_comment.created_date = timezone.now()
            new_comment.save()
            return redirect('post_detail', pk= new_comment.post.id)
        if category_form.is_valid():
            new_category = category_form.save(commit=False)
            new_category.post = get_object_or_404(Post, pk=pk)
            new_category.save()
            return redirect('post_detail', pk=new_category.post.id)
        else:
            return redirect('post_detail', pk=pk)
    else:
        post = get_object_or_404(Post, pk=pk)
        likes = Like.objects.filter(post_id=pk).count()
        comments = Comment.objects.filter(post_id=pk)
        categories = Category.objects.filter(post_id=pk)
        comment_form = CommentForm()
        category_form = CategoryForm()
        if request.user.is_authenticated():
            liked = Like.objects.filter(user=request.user, post_id=pk)
        else:
            liked = False
        if not comments:
            return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories, 'comment_form': comment_form, 'category_form': category_form, 'likes': likes, 'liked': liked})
        else:
            return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories, 'comments': comments, 'comment_form': comment_form, 'category_form': category_form, 'likes': likes, 'liked': liked})


def post_new(request):
    if request.user.id:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post_summary_array = []
                post_summary_array.append(post.text[:95])
                post_summary_array.append("... ")
                post_summary = " ".join(post_summary_array)
                post.summary = post_summary
                post.image = form.cleaned_data['image']
                if 'draft' in request.POST:
                    post.save()
                elif 'publish' in request.POST:
                    post.publish()
                    post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        return redirect('post_list')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.id == post.author_id:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post_summary_array = []
                post_summary_array.append(post.text[:95])
                post_summary_array.append("... ")
                post_summary = " ".join(post_summary_array)
                post.summary = post_summary
                post.image = form.cleaned_data['image']
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            print('is valid')
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return redirect('post_detail', pk=post.pk)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            profile = Blogger()
            profile.user = new_user
            profile.save()
            return HttpResponseRedirect('/')

    else:
        form = RegistrationForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')



def comment_delete(request, comment_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if (comment.author_id == request.user.id) or (post.author_id == request.user.id):
        comment.delete()
        return redirect('/post/'+post_id)
    else:
        messages.info(request, "You cannot delete this comment.")
        return redirect('/post/'+post_id)

def home(request):
    context = RequestContext(request,
                       {'request': request,
                        'user': request.user})
    return render_to_response('blog/home.html',
                         context_instance=context)

def get_category(request, category_text):
    categories = Category.objects.filter(text=category_text)
    post_ids = list(category.post_id for category in categories)
    posts = Post.objects.filter( id__in=post_ids).order_by('created_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})

def logged_out(request):
    return render(request, 'blog/logged_out.html')


@login_required
@transaction.atomic
def update_profile(request):
    check = Blogger.objects.filter(user_id=request.user.id).exists()
    if request.user.id and check == False:
        profile = Blogger()
        profile.user = request.user
        profile.save()
    profile = get_object_or_404(Blogger, user_id=request.user.id)
    if request.method == 'POST':
        user_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid():
            profile.user_id = request.user.id
            profile.save()
            return redirect('show_profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
    })

def show_profile(request):
    check = Blogger.objects.filter(user_id=request.user.id).exists()
    if request.user.id and check == False:
        profile = Blogger()
        profile.user = request.user
        profile.save()
    profile = get_object_or_404(Blogger, user_id=request.user.id)
    posts = Post.objects.filter(author_id=request.user.id).order_by('published_date').reverse()
    user = get_object_or_404(User, id=request.user.id)
    return render(request, 'profiles/show_profile.html', {'profile': profile, 'posts': posts, 'user': user})



def user_profile(request, pk):
    profile = get_object_or_404(Blogger, user_id=pk)
    posts = Post.objects.filter(author_id=pk).order_by('published_date').reverse()
    user = get_object_or_404(User, id=pk)
    return render(request, 'profiles/show_profile.html', {'profile': profile, 'posts': posts, 'user': user})


def like(request, pk):
# if request.method == 'POST':
#     new_like, created = Like.objects.get_or_create(user=request.user, post_id=pk)
#     likes = Like.objects.filter(post_id=pk).count()
#     ctx = {'likes': likes}
#     return HttpResponse(json.dumps(ctx), content_type='application/json')
    liked = Like.objects.filter(user=request.user, post_id=pk)
    if liked:
        liked.delete()
    else:
        Like.objects.create(user=request.user, post_id=pk)
    # new_like, created = Like.objects.get_or_create(user=request.user, post_id=pk)
    return redirect('post_detail', pk=pk)

def unlike(request, pk):
    liked = Like.objects.filter(user=request.user, post_id=pk)
    if liked:
        liked.delete()
    return redirect('post_detail', pk=pk)

def most_popular(request):
    likes_dictionary = {}
    posts = Post.objects.all()
    ordered_by_likes = Post.objects.annotate(num_likes=Count('like')).order_by('-num_likes')
    print(ordered_by_likes)
    return render(request, 'blog/most_popular.html', {'ordered_by_likes': ordered_by_likes  })
