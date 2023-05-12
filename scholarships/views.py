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
                                    total_periods=totalP,active='Activo',date_application=now,id_user=ben)
            scolarship.save()
        
            return render(request,'menu.html')
        
class BeneficiaryUpdateView(BeneficiaryUpdateView):
    pass 

class NaturalDonorUpdateView(NaturalDonorUpdateView):
    pass

class LegalDonorUpdateView(LegalDonorUpdateView):
    pass

class InstitutionUpdateView(InstitutionUpdateView):
    pass
