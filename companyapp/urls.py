from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage, all_category, all_companies, detail, category

urlpatterns = [
    path('', HomePage, name='home'),
    path('all-companies', all_companies, name='all-companies'),
    path('all-companies/<int:id>/detail/', detail, name='detail'),
    path('all-category', all_category, name='all-category'),
    path('category/<int:id>/', category, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
