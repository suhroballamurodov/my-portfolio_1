from django.urls import path, include
from .views import *
# from . import views
# from rest_framework import routers



# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', main, name='main'),
    path('portfolio_details/', portfolio_details, name='portfolio_details'),
    path('contact/', contact, name='contact'),
    path('contact/success/',contact_success, name='contact_success'),
    path('telegram_bot/', telegram, name='telegram_bot'),
    path('web/', web, name='web'),
    # path('motions', views.motions, name='motions'),
    # path('api/', include(router.urls)),  #API uchun link
] 