from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCreateView, CarDetailView, CarUpdateView, CarDeleteView, city_search
from accounts.views import register_view,login_view, logout_view, termos_view, privacidade_view

urlpatterns = [
    path('', CarsListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/',login_view, name='login'),
    path('logout',logout_view, name='logout'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCreateView.as_view(), name='new_car'),
    path('termos/', termos_view, name='termos'),
    path('privacidade/', privacidade_view, name='privacidade'),
    path('car/<int:pk>/',CarDetailView.as_view(), name='car_detail' ),
    path('car/<int:pk>/update/',CarUpdateView.as_view(), name='car_update' ),
    path('car/<int:pk>/delete/',CarDeleteView.as_view(), name='car_delete'),
    path('sellers/', include('sellers.urls')),
    path('api/cities/', city_search, name='city_search'),
    ] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
