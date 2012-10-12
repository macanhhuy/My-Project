from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from blog.models import Post

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization= Authorization()