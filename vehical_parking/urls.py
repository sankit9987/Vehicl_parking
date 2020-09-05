from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('logout',views.ulogout,name='logout'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('addvehicle',views.addvehicle,name='addvehicle'),
    path('Addcatgroy',views.Addcatgroy,name='Addcatgroy'),
    path('managecategroy',views.managecategroy,name='managecategroy'),
    path('deletecategory/<int:id>',views.deletecategory,name='deletecategory'),
    path('manageinvehicle',views.manageinvehicle,name='manageinvehicle'),
    path('editinvehical/<int:id>',views.editinvehical,name='editinvehical'),
    path('manageoutvehicle',views.manageoutvehicle,name='manageoutvehicle'),
    path('viewcustomerdetails/<int:id>',views.viewcustomerdetails,name='viewcustomerdetails'),
    path('datesearch',views.datesearch,name='datesearch'),
    path('datesearchresult',views.datesearchresult,name='datesearchresult'),
]