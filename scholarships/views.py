"""from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user= User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1']) 
                user.save()
                login(request,user)
                return redirect('menu')
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    "error": "Username already exists"
                })                            
        return render(request, 'signup.html',{
            'form':UserCreationForm,
            "error": "Password do not match"
        })     

def menu(request):
     return render(request, 'menu.html')

def signout(request):
    logout(request)
    return redirect('home')

def sigin(request):
    if request.method == 'GET':
        return render(request, 'sigin.html',{
            'form':AuthenticationForm
        })
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'sigin.html',{
                'form':AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request,user)
            return redirect('menu')
            """
from django.views import View
from django.shortcuts import render
from users.models import Beneficiary
from .models import Scholarship
from datetime import datetime

class ShowMenu(View):
    def get(self,request):
        return render(request,'menu.html')

class NewApplication(View):
    def get(self,request):
        return render(request,'newscholarship.html')
    
class InsertScholarship(View):
    def post(self,request):
        if request.method == 'POST':
            name = request.POST['nombres']
            lastname = request.POST['apellidos']
            typedocument = request.POST['tipoid']
            numdoc = request.POST['numdoc']
            institute = request.POST['instituc']
            program = request.POST['programa']
            valuesem = request.POST['valorS']
            timeA = request.POST['periodoActual']
            totalP = request.POST['totalPeriodos']
            icfes = request.POST['puntajeI']
            levels = request.POST['estrato']
            optionnew = request.POST['ingresoEstudiante']
            try:
                picturedoc = request.FILES['src-file1']
                picturecer = request.FILES['src-file2']
            except:
                print('error')

        
            now = datetime.now()
            letter = request.POST['cartaMotivacional']
            id_ben = request.user.id
            ben = Beneficiary.objects.get(user_ptr_id=id_ben)
            scolarship = Scholarship(stratum=levels,photocopy_id=picturedoc, motivational_letter=letter,
                                    certificate=picturecer,value_period=valuesem,icfes_score=icfes,period_current=timeA,
                                    program_adm=program,application_type=optionnew,state='En Revision',
                                    total_periods=totalP,active='Activo',date_application=now,id_user=ben)
            scolarship.save()
        
            return render(request,'menu.html')
