from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = 'productapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:item>/<int:item_id>', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('update/<str:item>/<int:item_id>', views.update, name='update'),
    path('delete/<str:item>/<int:item_id>', views.delete, name='delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
