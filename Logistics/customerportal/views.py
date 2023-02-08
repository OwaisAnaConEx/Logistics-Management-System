from django.shortcuts import render,redirect
from .models import * 
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate

## Signup
def signupuser(request):
    
    if request.method == 'POST':
            print("IN")
            u_name= request.POST.get('username')
            u_pass= request.POST.get('password')
            u_email = request.POST.get('email')
            cnic = request.POST.get('cnic')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            postal = request.POST.get('postal')
            city = request.POST.get('city')
            province = request.POST.get('province')
            state = request.POST.get('state')
            
            x= [u_name,u_email,u_pass,state,cnic,city,address,province,postal,phone]
            
            print(x)

            user = User.objects.create(username = u_name,email = u_email)
            user.set_password(u_pass)
            user.save()
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            customer = Customer.objects.create(userid  = user,
                                            address=address,
                                            state=state,
                                            contact = phone,
                                            city = city,
                                            province = province,
                                            postal = postal,
                                            cnic = cnic,
                                          )
            customer.save()
            return redirect("login")            
            
    return render(request,'signup.html')

## login

def Login(request):
    if request.method == 'POST':
        try:
            u_name= request.POST.get('username')
            u_pass1= request.POST.get('password')
            user= authenticate(request,username=u_name,password=u_pass1)
            print(user,u_name,u_pass1)
            if user is not None:
                login(request,user)
                
                if user.groups.filter(name='admin').exists():
                    return redirect('main')
            
                elif user.groups.filter(name='rider').exists():
                    return redirect('riderDash')
                else:
                    return redirect('dashboardCus')

            else:
                return render(request,'login.html')

        except:
            print("Login Failed")
            
    return render(request,'login.html')



### Home Page

def main(request):
    if request.method == 'POST':
        number = request.POST.get("trackOrder")
        print("Number")
        original = number[7:]
        try:
            parcel = Parcel.objects.get(id=int(original))
            print(parcel.id,parcel.status.name)
            print(original)
        except:
             return render(request,"home.html")
        status = Status.objects.all()    
        context = {'parcel': parcel,'status':status}
        return render(request,"track.html",context)
    return render(request,'home.html')


# Order PArcel

def requestParcel(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='customer').exists():
           
            x = ServiceType.objects.all()
            if request.method == 'POST':
                weight=float(request.POST.get('weight'))
                qty=request.POST.get('qty')
                service=request.POST.get('serviceType')
                deliverAddress=request.POST.get('consigneeaddress')
                pickupAddress=request.POST.get('pickupaddress')
                state=request.POST.get('state')
                consigneeName=request.POST.get('consigneename')
                consigneeEmail=request.POST.get('consigneeemail')
                consigneeContact=request.POST.get('consigneephone')
                city=request.POST.get('city')
                country=request.POST.get('country')
                pcity=request.POST.get('pcity')
                pcountry=request.POST.get('pcountry')
                pstate=request.POST.get('pstate')
                total = 0
                customer = Customer.objects.get(userid=request.user.id)
                serviceType = ServiceType.objects.get(id=service)
                total = (weight * float(qty)) + float(serviceType.charges)
                status = Status.objects.get(id=6)
                data = {
            'customer': customer,
            'status': status,
            'service': serviceType,
            'weight' : weight,
            'qty' : qty,
            'pickuplocation' :pickupAddress,
            'deliverlocation' :deliverAddress,
            'city' :city,
            'country' :country,
            'state' :state,
            'total':total,
            'consigneeName' :consigneeName,
            'consigneeEmail' :consigneeEmail,
            'consigneeContact' :consigneeContact,
            'PaymentStatus' : "Pending",
            'pcity' : pcity,
            'pcountry' :pcountry,
            'pstate': pstate
                }
                
                parcel = Parcel.objects.create(**data)
                x=parcel.save()
                print(x)
                print(parcel.consigneeName)
                return redirect('invoice',pk=parcel.id)
                
            return render(request,'requestParcel.html',{'service':x})
        return redirect('login')
    else:
            return redirect('login')
            
        
# Invoice        
def getInvoice(request,pk):
    parcel = Parcel.objects.get(id=pk)
    i = parcel.customer.userid.id
    return render(request,'invoice.html',{'parcel':parcel})
    
# tracking
def track(request,trackOrder):
    try:
        print(trackOrder)
        parcel = Parcel.objects.get(id=pk)
        status = Status.objects.all()
        return render(request,'track.html')
        
    except:
        return render(request,'track.html')
# customer dashboard
def cus_dashboard(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='customer').exists():
            userid=request.user.id
            customer = Customer.objects.get(userid=userid)
            parcel = Parcel.objects.filter(customer = customer.id)
            return render(request,'customerDash.html',{'parcel':parcel})
        
# admin Dashboard
def mainAdmin(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin').exists():
            allParcels = Parcel.objects.all()

            process = Status.objects.get(id=6)
            deliver = Status.objects.get(id=4)

            booked = Status.objects.get(id=1)
            booked = allParcels.filter(status=booked).count()

            inwarehouse = Status.objects.get(id=2)
            inwarehouse = allParcels.filter(status=inwarehouse).count()
            pickedup = Status.objects.get(id=5)
            pickedup = allParcels.filter(status=pickedup).count()
            outfordelivery = Status.objects.get(id=3)
            outfordelivery = allParcels.filter(status=outfordelivery).count()


            rider = Rider.objects.all().count()

            print(deliver.name)
            delivered = allParcels.filter(status=deliver)
            newOrders = Parcel.objects.filter(status=process)
            newCount = newOrders.count()
            allParcels.count()
            
            st = Status.objects.all()
            for i in st:
                print(i.id,i.name)
            
        
            return render(request,'adminPanel.html',{'newOrders':newOrders,
                                                    'allParcelCount':allParcels.count(),
                                                    'newCount':newCount,
                                                    'inwarehouse':inwarehouse,
                                                    'booked':booked,
                                                    'pickedup':pickedup,
                                                    'outfordelivery':outfordelivery,
                                                    'delivered':delivered.count(),
                                                    'rider':rider})
    else:
            return redirect('login')
            

def allParcel(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin').exists():
            x=Parcel.objects.all()
            return render(request,'viewAllParcels.html',{'parcels':x})
        else:
            return redirect('login')


# Add Rider     

def addRider(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin').exists():
            if request.method == 'POST':
                    u_name= request.POST.get('username')
                    u_pass= request.POST.get('password')
                    u_email = request.POST.get('email')
                    cnic = request.POST.get('cnic')
                    phone = request.POST.get('contact')

                    user = User.objects.create(username = u_name,email = u_email)
                    user.set_password(u_pass)
                    user.save()
                    
                    group = Group.objects.get(name="rider")
                    user.groups.add(group)
                    
                    rider = Rider.objects.create(user=user,contact=phone,cnic=cnic,name=u_name)
                    rider.save()
            return render(request,'addRider.html')
            
        else:
            return redirect('login')
                                



def AssignParcelToRider(request,pk):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin').exists():
            x = Rider.objects.all()
            status = Status.objects.all()
            parcel = Parcel.objects.get(id=pk)
            if request.method == 'POST':
                    rider=request.POST.get('rider')
                    ride = Rider.objects.get(id=rider)
                    assign = AssignParcel.objects.create(parcel=parcel,rider=ride )
                    st = Status.objects.get(id=1)
                    parcel.status = st
                    parcel.save()
            print(x)
            return render(request,'assignParcel.html',{'riders':x})
    else:
            return redirect('login')
     

def RiderDashboard(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='rider').exists():
            user = request.user
            rider = Rider.objects.get(user=user)
            assignparcel = AssignParcel.objects.filter(rider = rider )
            parcels=[]
            for i in assignparcel:
                parcels.append(i.parcel)
            print(parcels)
        return render(request, 'riderPanel.html',{'parcels':parcels})
    else:
            return redirect('login')

def changeStatus(request,pk):
    if request.user.is_authenticated:
            status = Status.objects.all()
            parcel = Parcel.objects.get(id=pk)
            st = parcel.status.id
            print(st)
            if request.method == 'POST':
                st = request.POST.get('status')
                sta = Status.objects.get(id=st)
                parcel.status=sta
                parcel.save()
                if request.user.groups.filter(name='rider').exists():
                    return redirect('riderDash')
                elif request.user.groups.filter(name='admin').exists():
                    return redirect('main')
                    
        
            return render(request,'updateParcelStatus.html',{'currSta':st,'all':status})
    else:
            return redirect('login')

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login') 