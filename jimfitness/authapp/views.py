from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact

# Create your views here.
def Home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>9 or len(username)<9:
            messages.info(request,"El numero de celular tiene que tener 9 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Su contraseña no coincide")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"El número de celular ya existe")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email ya existe")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"Su usuario ya ha sido creado satisfactoriamente")
        return redirect('/login')
        
        
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Registro Satisfactorio")
            return redirect('/')
        else:
            messages.error(request,"Credenciales Inválidas")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Cierre de sesión exitoso")    
    return redirect('/login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Gracias por contactarnos, nos pondremos en contacto con usted pronto")
        return redirect('/contact')
        
    return render(request,"contact.html")