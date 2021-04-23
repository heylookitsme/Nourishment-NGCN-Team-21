from django.urls import path

from . import views
app_name = 'campagins'
urlpatterns = [
    path('', views.home, name='index'), 

    path('campagins', views.listCampagin, name='lists'), 
    path('create-campagin', views.createCampagin, name='create-campagin'),
    path('campagins/update-campagin/<int:id>', views.updateCampagin, name='update-campagin'),
    path('campagins/<int:id>', views.detailCampagin, name='detail'),


]

