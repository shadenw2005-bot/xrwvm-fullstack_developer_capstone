from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('dealers', TemplateView.as_view(template_name="Home.html")),
    path('added_review', TemplateView.as_view(template_name='added_review_mock.html')),
    path('postreview/8', TemplateView.as_view(template_name='post_review_mock.html')),
    path('dealer/8', TemplateView.as_view(template_name='dealer_reviews_mock.html')),
    path('dealer/<int:dealer_id>', TemplateView.as_view(template_name="Home.html")),
    path('register', TemplateView.as_view(template_name="Home.html")),
    path('login', TemplateView.as_view(template_name="Home.html")),
    path('postreview/<int:dealer_id>', TemplateView.as_view(template_name="Home.html")),
    path('dealers_mock', TemplateView.as_view(template_name='dealers_mock.html')),
    path('searchcars/<int:dealer_id>', TemplateView.as_view(template_name="Home.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
