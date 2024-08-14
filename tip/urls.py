from django.urls import path
from .views import TipListCreateView, TipByLanguageView, TipSearchView

urlpatterns = [
    path('tips/', TipListCreateView.as_view(), name='tip-list-create'),
    path('tips/<str:language>/', TipByLanguageView.as_view(), name='tip-by-language'),
    path('find-tips/', TipSearchView.as_view(), name='tip-search'),
]