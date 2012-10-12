from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from blog.models import *
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
import time
from calendar import month_name

def main(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)
  
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("index.html", dict(posts=posts, user=request.user,
                                            post_list=posts.object_list))

