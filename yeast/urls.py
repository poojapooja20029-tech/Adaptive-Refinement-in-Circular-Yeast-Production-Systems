from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('production-data/', views.production_data, name='production_data'),
    path('production-data/edit/<int:id>/', views.edit_production_data, name='edit_production_data'),
    path('production-data/delete/<int:id>/', views.delete_production_data, name='delete_production_data'),
    path('prediction/', views.predict_biomass, name='prediction'),
    path('optimization/', views.process_optimization, name='optimization'),
    path('adaptive-refinement/', views.adaptive_refinement, name='adaptive_refinement'),
]
