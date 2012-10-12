# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post, Category, Comment
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3
    
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_filter = ('title',) 
    search_fields = ('title', 'content')
#    def formfield_for_dbfield(self, db_field, **kwargs):
#        if db_field.name in ('content'):
#            return db_field.formfield(widget=TinyMCE(
#                attrs={'cols': 100, 'rows': 30},
#                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
#            ))  
#        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', 
                '/static/grappelli/tinymce_setup/tinymce_setup.js',]
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
