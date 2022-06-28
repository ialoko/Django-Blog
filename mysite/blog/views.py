from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

# Create your views here.
def post_share(request, post_id):
    #get by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        #post request means form submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url()) 
            subject = '{} ({}) recommends you reading" {}"'.format(cd['name'],	cd['email'], post.title)
            message	= 'Read "{}" at	{}\n\n{}\'s	comments: {}'.format(post.title, post_url,	cd['name'],	cd['comments'])
            send_mail(subject,	message, 'admin@myblog.com', [cd['to']])
            sent =	True
    else: #get request display empty form
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) #3 pages per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #then retrieve first pagge
        posts = paginator.page(1)
    except EmptyPage:
        #retrieve last page
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page':page, 'posts':posts})

#retreive post with given slug and date
def post_detail(request, year, month, day,post):
    post = get_object_or_404(Post, slug=post, 
    status ='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #create comment but not save to database
            new_comment = comment_form.save(commit=False)
            #assign current post to comment
            new_comment.post = post
            #save to database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post':post, 'comments':comments, 'new_comment': new_comment, 'comment_form': comment_form})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'blog/post/list.html'

