from .                          import views
from django.conf                import settings
from django.conf.urls.static    import static
from django.contrib             import admin
from django.urls                import path

urlpatterns = [
    path('test',                                        views.test,         name='test'),

    path('',                                            views.home,         name='home'),
    path('fight',                                       views.fight,        name='fight'),
    path('fight/check/<int:attack_index>/<slug:verb>',  views.fight_check,  name='check'),
    path('player',                                      views.player,       name='player'),
    path('sentence',                                    views.sentence,     name='sentence'),

    path('admin',                                       admin.site.urls,    name='admin'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
