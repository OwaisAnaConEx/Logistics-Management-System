from django.contrib import admin
from django.urls import path,include
from .views import * 

urlpatterns = [
    path('signup', signupuser,name="signup"),
    path('login', Login,name="login"),
    path('', main,name="dashboard"),
    path('newParcel', requestParcel,name="newParcel"),
    path('invoice/<int:pk>', getInvoice,name="invoice"),
    path('dashboard', cus_dashboard,name="dashboardCus"),
    path('mainAdmin', mainAdmin,name='main'),
    path('addRider', addRider,name='addrider'),
    path('assignRider/<int:pk>', AssignParcelToRider),
    path('riderDash', RiderDashboard,name='riderDash'),
    path('viewParcels', allParcel,name="viewParcels"),
    path('changeStatus/<int:pk>', changeStatus),
    path('logout', logoutPage),
    
    
]