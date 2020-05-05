from .models import Post
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

class  LatestPostsFeed(Feed):
    title = 'My Blog'
    link = '/blog'
    description = 'New posts of my blog'

    def items(self):
        return Post.published.all()[:3]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatewords(item.body, 10)
