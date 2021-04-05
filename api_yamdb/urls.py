from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('admin/',
                    admin.site.urls),
               path('redoc/',
                    TemplateView.as_view(template_name='redoc.html'),
                    name='redoc'),
               path('api/',
                    include('api.users.urls')),
               path('api/',
                    include('api.categories.urls')),
               path('api/',
                    include('api.genres.urls')),
               path('api/',
                    include('api.titles.urls')),
               path('api/',
                    include('api.reviews.urls')),
               path('api/',
                    include('api.comments.urls')),
               ] + static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
