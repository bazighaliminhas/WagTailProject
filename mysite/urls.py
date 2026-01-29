from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls

from search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add language prefix to Wagtail URLs
urlpatterns += i18n_patterns(
    # Wagtail URLs with language prefix
    re_path(r"", include(wagtail_urls)),
)

# Also add Wagtail URLs without language prefix (fallback)
urlpatterns += [
    re_path(r"", include(wagtail_urls)),
]
