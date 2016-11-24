from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.models import User

# Additional imports for users:
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from .forms import RegistrationForm, CommentForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_draft_list(request):
    posts = Post.objects.filter( author__in=[request.user.id], published_date__isnull=True).order_by('created_date').reverse()
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
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = get_object_or_404(Post, pk=pk)
            new_comment.created_date = timezone.now()
            new_comment.save()
            return redirect('post_detail', pk= new_comment.post.id)
    else:
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post_id=pk)
        comment_form = CommentForm()
        if not comments:
            return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})
        else:
            return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def post_new(request):
    if request.user.id:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
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
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
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
