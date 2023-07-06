from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.auth.models import User
from .models import categoria,subir_proyecto,usuariocliente,proyecto,proyecto_categoria

# Create your views here.
def inicio(request):
    return render(request,'index.html')


def proyectos(request):
    return render(request, 'proyectos.html')


def Contactos(request):
    if request.method == 'POST':
        asunto = request.POST['opcion-contacto']
        mensaje = request.POST['message']
        
        destinatario = request.POST['gmail-contacto']

        send_mail(asunto, mensaje, 'infobaselltech@gmail.com', [destinatario])
        return render(request, 'contactos.html')
    
    return render(request, 'contactos.html')

def subirprojec(request):
    if request.method == 'POST':
        campo1 =request.POST.get('nombre')
        campo3 =request.POST.get('descripcion-de-proyecto')
        campo4 =request.POST.get('inversion-proyecto')
        campo5 =request.POST.get('repositorio')
        campo6 =request.POST.get('archivo-proyecto')

        mi_objeto=subir_proyecto(titulo_proyecto=campo1, descripcion=campo3, precio=campo4, repositorio=campo5, imagen=campo6)

        mi_objeto.save()
        datos={'r':'aceptado !!'}
        return render(request, 'subir-proyecto.html',datos)

    else:
        datos={'r2':'Nose puedes procesar su solicitud !!'}
        return render(request, 'subir-proyecto.html',datos)


def usuario_existe(correo,contraseña):
    return User.objects.filter(email=correo,contraseña=contraseña).exists()


def inicioDeSesion(request):
    if request.method == 'POST':
        try:
            detalleUsuario=usuariocliente.objects.get(correo=request.POST['gmail'],contraseña=request.POST['contraseña'])
            print("usuario=",detalleUsuario)
            request.session['correo']=detalleUsuario.correo
            messages.info(request, "Aceptado")
            
            return render(request,'index.html')
        except  usuariocliente.DoesNotExist as e:
            messages.error(request, "Nombre del usuario o password no existe en la base e datos")
    return render(request,'inicioDeSesion.html')     




def registro(request):
    if request.method == 'POST':
        nombre1 = request.POST.get('nombre-cliente')
        apellido2 = request.POST.get('apellido-cliente')
        correo3 = request.POST.get('gmail-cliente')
        fecha_nacimiento4 = request.POST.get('fecha-cliente')
        ciudad5 = request.POST.get('ciudad')
        direccion6 = request.POST.get('direccion')
        telefono7 = request.POST.get('telefono-cliente')
        contraseña8 = request.POST.get('contraseña')
        numeracion9 = request.POST.get('numeracion')

        

        mi_objeto=usuariocliente(nombre=nombre1,apellido=apellido2,correo=correo3,fecha_nacimiento=fecha_nacimiento4,ciudad=ciudad5,direccion=direccion6,telefono=telefono7,contraseña=contraseña8,numeracion=numeracion9)

        mi_objeto.save()
        datos={'r':'aceptado !!'}
        return render(request, 'inicioDeSesion.html',datos)

    else:
        datos1={'r2':'Nose puedes procesar su solicitud !!'}
        return render(request, 'registro.html',datos1)



    
def carrito(request):
    return render(request, 'carrito.html')

