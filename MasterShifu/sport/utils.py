from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        view = View.objects.annotate(Count('section'))

        context['menu'] = menu

        context['views'] = view
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
