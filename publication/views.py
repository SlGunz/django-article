from django.shortcuts import render
from django.views import generic
from .models import Article, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


class ArticleListView(generic.ListView):
    """
    Generic class-based view for a list of articles.
    """
    model = Article


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


def article_detail(request, pk):
    """
    View function. Retrieves an article, create article comment
    """
    article = get_object_or_404(Article, pk=pk)

    comment_form = CommentForm(request.POST)

    if request.method == 'POST' and request.user.is_authenticated:
        if comment_form.is_valid():
            user = django.contrib.auth.models.User.objects.get(pk=1)
            comment = Comment(article=article,
                              message=comment_form.cleaned_data['comment'],
                              owner=request.user)

        return HttpResponseRedirect(reverse('article-detail'))

    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'form': comment_form,
    }

    return render(request, 'publication/article_detail.html', context)
