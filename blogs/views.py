from django.views import generic

from .models import Blog


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'

#
# class BlogDetailView(generic.DetailView):
#     model = Blog
#     template_name = 'blogs/blog_detail.html'
#     context_object_name = 'blog'
