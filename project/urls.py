from django.contrib import admin
from django.urls    import path
from .              import views

urlpatterns = [
    path('test',        views.test,         name='test'),

    path('',            views.home,         name='home'),
    path('fight',       views.fight,        name='fight'),
    path('fight/check/<int:attack_index>/<slug:verb>', views.fight_check,  name='check'),
    path('player',      views.player,       name='player'),
    path('sentence',    views.sentence,     name='sentence'),

    path('admin',       admin.site.urls,    name='admin'),
]
