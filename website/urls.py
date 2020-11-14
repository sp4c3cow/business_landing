from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio-details', views.porftfolio_details, name='portfolio_details'),
    path('inner-page', views.inner_page, name='inner_page'),
    path('contact/', views.contact_form, name='contact')
]