from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from .models import Post  # Ensure you have a Post model defined


# Create your views here.
def index(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)  # Fetch the post with the given primary key
    return render(request, 'post.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        photo = request.FILES.get('photo')
        content = request.POST.get('content')
        if title and content:  # Ensure both fields are filled
            # Create a new post instance
            new_post = Post(title=title, photo=photo, content=content)
            new_post.save()  # Save the post to the database
            return redirect('index')  # Redirect to the index page after creation
        else:
            return render(request, 'create.html', {'error': 'All fields are required.'})
    return render(request, 'create.html')  # Render the form for creating a new post

def update(request, pk):
    post = Post.objects.get(id=pk)  # Fetch the post to be updated
    if request.method == 'POST':
        title = request.POST.get('title')
        photo = request.FILES.get('photo')
        content = request.POST.get('content')
        if title and content:  # Ensure both fields are filled
            post.title = title  # Update the title
            post.content = content  # Update the content
            if photo:
                post.photo = photo
            post.save()  # Save the changes to the database
            return redirect('index')  # Redirect to the index page after updating
        else:
            return render(request, 'update.html', {'post': post, 'error': 'All fields are required.'})
    return render(request, 'update.html', {'post': post})  # Render the form for updating a post

def delete(request, pk):
    post = Post.objects.get(id=pk)  # Fetch the post to be deleted
    if request.method == 'POST':
        post.delete()  # Delete the post from the database
        return redirect('index')  # Redirect to the index page after deletion
    return render(request, 'delete.html', {'post': post})  # Render the confirmation page for deletion