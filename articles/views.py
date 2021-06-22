from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, CreateView
from .models import Article, Category
from django.views.generic.list import MultipleObjectMixin
from django.core.mail import send_mail, BadHeaderError
from blog_news.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


class Categorys:
    def get_category(self):
        return Category.objects.all()


class DetailArticleView(DetailView):
    model = Article
    context_object_name = "article"
    queryset = Article.objects.all()
    template_name = "articles/article_detail.html"


class ArticleList(Categorys, ListView):
    model = Article
    context_object_name = "articles"
    queryset = Article.objects.all()
    template_name = "articles/article_list.html"

    def get_ordering(self):
        if "ordering" in self.request.GET:
            status = self.request.GET["ordering"]
            if status == "old":
                self.ordering = "date"
            elif status == "new":
                self.ordering = "-date"

        return self.ordering


class CategoryCreate(CreateView):
    model = Category
    fields = "__all__"
    context_object_name = "category"
    success_url = "/article/add"
    template_name = "articles/article_add_category.html"


class ArticleCreateView(CreateView):
    model = Article
    fields = "__all__"
    context_object_name = "article"
    success_url = "/"
    template_name = "articles/article_add.html"


class ArticleByCategory(View, MultipleObjectMixin):
    def get(self, request, pk):
        articles = Article.objects.filter(category_id=pk)
        if self.get_ordering():
            articles = articles.order_by(self.get_ordering())
        return render(
            request, "articles/category.html", {"articles": articles, "pk": pk}
        )

    def get_ordering(self):
        if "ordering" in self.request.GET:
            status = self.request.GET["ordering"]
            if status == "old":
                self.ordering = "date"
            elif status == "new":
                self.ordering = "-date"
        return self.ordering


class FeedbackView(View):

    def get(self, request):
        return render(request, "articles/feedback.html",)

    def post(self, request):
        subject = 'рабочая тема'
        message = request.POST["text"]
        try:
            send_mail(f'{subject}от {request.POST["email"]}', message, DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
        except BadHeaderError:
            return render(request, "articles/feedback.html", )
        return redirect('/')
