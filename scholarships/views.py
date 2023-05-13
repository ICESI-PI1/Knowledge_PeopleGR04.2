from django.views import View
from django.shortcuts import render
from users.models import Beneficiary
from .models import Scholarship
from datetime import datetime
from users.views import BeneficiaryUpdateView,NaturalDonorUpdateView,LegalDonorUpdateView,InstitutionUpdateView

class ShowMenu(View):
    def get(self,request):
        return render(request,'menu.html')

class NewApplication(View):
    def get(self,request):
        return render(request,'newscholarship.html')
    
class LookApplication(View):
    def get(self,request):
        id_ben = request.user.id
        scholarship = Scholarship.objects.filter(id_user=id_ben)
        data = {"scholarships":scholarship}
        return render(request,'historyapps.html',data)
    
class ActiveSolicitud(View):
    def get(self,request):
        id_ben = request.user.id
        datos_solicitud = Scholarship.objects.filter(id_user = id_ben, active = "AC")
        
        contexto = {
            'solicitud_activa': datos_solicitud,
        }
        return render(request, 'ActiveSolicitud.html', contexto)
    
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
                                    program_adm=program,application_type=optionnew,state='P',
                                    total_periods=totalP,active='AC',date_application=now,id_user=ben)
            scolarship.save()
        
            return render(request,'menu.html')

def active_scholarships(request):
    user = request.user.id
    active_scholarships = Scholarship.objects.filter(id_user=user, active='AC')
    context = {'active_scholarships': active_scholarships}
    return render(request, 'active_scholarships.html', context)

   
class BeneficiaryUpdateView(BeneficiaryUpdateView):
    pass 

class NaturalDonorUpdateView(NaturalDonorUpdateView):
    pass

class LegalDonorUpdateView(LegalDonorUpdateView):
    pass

class InstitutionUpdateView(InstitutionUpdateView):
    pass
