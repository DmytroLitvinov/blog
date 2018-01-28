Title: Django Queryset: select and prefetch related.
Date: 2017-08-19 13:54
Category: Django
Tags: python, django, queryset, select_related, prefetch_related
Slug: django-queryset-select-and-prefetch-related
Summary: Some information for understanding Django Queryset  methods: select_related and prefetch_relateds

Today, we will learn more about Django Queryset methods **_select_related()_** and **_prefetch_related_()**. I decided to write an article after I [recommended](https://medium.com/@dmytrolitvinov/idea-for-the-djangotip-post-select-related-and-prefetch-related-with-new-object-prefetch-f1b8163eb5dd) to a blogger [Lucas Magnum](https://medium.com/@lucasmagnum). 

_While I wrote this post I see that a slogan of Lucas Magnum's blog is:
(I support this idea with both hands :blush:)_
> Learning through sharing. 



Before you start, you need to know about [**a problem N+1**](https://medium.com/@hakibenita/things-you-must-know-about-django-admin-as-your-app-gets-bigger-6be0b0ee9614).

If you just started programming on Django framework, you need to remember:

* _select_related_ - forward relationship
* _prefetch_related_ - reverse relationship

### List of links to read:
* Django docs about [select_related](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#select-related)
* Django docs about [prefetch_related](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#prefetch-related)
* Of course [Lucas Magnum's post](https://medium.com/@lucasmagnum/djangotip-select-prefetch-related-e76b683aa457)
* [Advanced usage of prefetch_related](http://kennethjiang.blogspot.com/2016/01/advanced-usage-of-prefetchrelated-and.html)
* [Solving Performance Problems in the Django ORM](https://medium.com/@hansonkd/performance-problems-in-the-django-orm-1f62b3d04785)