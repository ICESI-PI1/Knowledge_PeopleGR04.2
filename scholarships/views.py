from django.views import View
from django.shortcuts import render
from users.models import Beneficiary, Institution
from .models import Scholarship
from datetime import datetime
from django.views.generic import TemplateView, ListView

from users.views import BeneficiaryUpdateView,NaturalDonorUpdateView,LegalDonorUpdateView,InstitutionUpdateView

class ShowMenu(View):
    def get(self,request):
        return render(request,'menu.html')

class NewApplication(View):
    def get(self,request):
        institutions = Institution.objects.all()
        data = {'institutions':institutions}
        return render(request,'newscholarship.html',data)
    
class LookApplication(View):
    def get(self,request):
        id_ben = request.user.id
        scholarship = Scholarship.objects.filter(id_user=id_ben)
        data = {"scholarships":scholarship}
        return render(request,'historyapps.html',data)
    
class ActiveSolicitud(View):
     def get(self,request):
        id_ben = request.user.id
        datos_solicitud = Scholarship.objects.filter(id_user = id_ben, active = 'AC')
        solicitud = datos_solicitud.first()

        if(solicitud != None):
            contexto = {
                'solicitud_activa': solicitud,
            }
            return render(request, 'ActiveSolicitud.html', contexto)
        else:
            return render(request,'errorActiveScholarship.html')
    
class InsertScholarship(View):
    def post(self,request):
        if request.method == 'POST':
            name = request.POST['nombres']
            lastname = request.POST['apellidos']
            typedocument = request.POST['tipoid']
            numdoc = request.POST['numdoc']
            institute = request.POST['instituc']
            institutionvalue = Institution.objects.get(name=institute)
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

            if not Scholarship.objects.filter(id_user=id_ben, active='AC').exists():
                scolarship = Scholarship(stratum=levels,photocopy_id=picturedoc, motivational_letter=letter,
                                        certificate=picturecer,value_period=valuesem,icfes_score=icfes,period_current=timeA,
                                        program_adm=program,application_type=optionnew,state='P',
                                        total_periods=totalP,active='AC',date_application=now,id_user=ben,institution=institutionvalue)
                scolarship.save()

                return render(request,'menu.html')
            else:
                scolarship = Scholarship(stratum=levels,photocopy_id=picturedoc, motivational_letter=letter,
                                        certificate=picturecer,value_period=valuesem,icfes_score=icfes,period_current=timeA,
                                        program_adm=program,application_type=optionnew,state='P',
                                        total_periods=totalP,active='IN',date_application=now,id_user=ben)
                scolarship.save()
  
                return render(request,'menu.html')

class EditSolicitud(View):
    def get(self,request):
        id_ben = request.user.id
        datos_solicitud = Scholarship.objects.filter(id_user = id_ben   , active = 'AC')
        solicitud = datos_solicitud.first()
        contexto = {
            'solicitud_activa': solicitud,
        }
        return render(request, 'editionScholarship.html', contexto)

    def post(self,request):
        if request.method == 'POST':

            if 'inactivate_scholarship' in request.POST:
                id_ben = request.user.id
                solicitud = Scholarship.objects.filter(id_user = id_ben, active = 'AC')
                scholarshipToInactivate = solicitud.first()
                
                scholarshipToInactivate.active = 'IN'
                scholarshipToInactivate.save()
                print(f"Solicitud con del usuario {scholarshipToInactivate.id_user.name} ha sido inactivada.")
                return render(request,'menu.html')
            
            
            program =  request.POST['programa']
            valuesem = request.POST['valorS']
            timeA = request.POST['periodoActual']
            totalP = request.POST['totalPeriodos']
            icfes = request.POST['puntajeI']
            levels = request.POST['estrato']
            optionnew = request.POST['ingresoEstudiante']
            picturedoc =  None
            picturecer = None
            try:
                picturedoc = request.FILES['src-file1']
                picturecer = request.FILES['src-file2']
            except:
                print('error')

                
            now = datetime.now()
            letter = request.POST['cartaMotivacional']
                
            id_ben = request.user.id
            solicitud = Scholarship.objects.filter(id_user = id_ben, active = 'AC')
            scholarshipUpdated = solicitud.first()

            scholarshipUpdated.stratum = levels
            scholarshipUpdated.photocopy_id = picturedoc  if picturedoc != None else scholarshipUpdated.photocopy_id 
            scholarshipUpdated.motivational_letter = letter
            scholarshipUpdated.certificate = picturecer  if picturecer != None else scholarshipUpdated.certificate 
            scholarshipUpdated.value_period = valuesem
            scholarshipUpdated.icfes_score = icfes
            scholarshipUpdated.period_current = timeA
            scholarshipUpdated.program_adm = program
            scholarshipUpdated.application_type = optionnew
            scholarshipUpdated.total_periods = totalP
            scholarshipUpdated.date_application = now

            scholarshipUpdated.save()
            return render(request,'menu.html')

class LookBeneficiaries(ListView):
    def get(self, request):
        return render(request, 'lookbeneficiaries.html')

## Edit Profile

class BeneficiaryUpdateView(BeneficiaryUpdateView):
    pass 

class NaturalDonorUpdateView(NaturalDonorUpdateView):
    pass

class LegalDonorUpdateView(LegalDonorUpdateView):
    pass

class InstitutionUpdateView(InstitutionUpdateView):
    pass



## Donor

class NewDonation(TemplateView):
    template_name= 'new_donation.html'

#Aliados

from django.views.generic import ListView
from .models import Institution

class InstitutionListView(ListView):
    model = Institution
    template_name = 'aliados.html'  # Reemplaza "institution_list.html" con el nombre de tu plantilla
    context_object_name = 'institutions'  # Define el nombre de la variable de contexto que contendrá la lista de instituciones

