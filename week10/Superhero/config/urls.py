from django.contrib import admin
from django.urls import path
from hero.views import HeroView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView, HomeView
from hero.views_articles import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from django.urls.conf import include, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view()),
    path('hero/<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('hero/', HeroListView.as_view(), name='hero_list'),
    path('hero/add', HeroCreateView.as_view(), name='hero_add'),
    path('hero/<int:pk>/', HeroUpdateView.as_view(), name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(),  name='hero_delete'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/'), name='home'),
    path('doc/', include('doc.urls')),
    # path('doc/', DocumentView.as_view(), name='document'),
    # path('doc/<str:doc>', DocumentView.as_view()),
    path('article/',                   ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',           ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',                ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',          ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',    ArticleDeleteView.as_view(),  name='article_delete'),

]
