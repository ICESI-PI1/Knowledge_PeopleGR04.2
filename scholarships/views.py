from django.views import View
from django.shortcuts import get_object_or_404, render
from users.models import Beneficiary, Institution
from .models import Scholarship,Transaction
from datetime import datetime
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect


from users.views import BeneficiaryUpdateView,NaturalDonorUpdateView,LegalDonorUpdateView,InstitutionUpdateView

class ShowMenu(View):
    def get(self,request):
        return render(request,'menu.html')

class NewApplication(View):
    def get(self,request):
        institutions = Institution.objects.all()
        data = {'institutions':institutions}

        id_ben = request.user.id
        datos_solicitud = Scholarship.objects.filter(id_user = id_ben, active = 'AC')
        solicitud = datos_solicitud.first()

        if(solicitud == None):
            return render(request,'newscholarship.html',data)
        else:
            return render(request,'errorCreateNewScholarship.html')

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
        institutions = Institution.objects.all()

        if(solicitud != None):
            contexto = {
                'solicitud_activa': solicitud,
                'institutions': institutions,
            }
            return render(request, 'ActiveSolicitud.html', contexto)
        else:
            return render(request,'errorActiveScholarship.html')
    
class InsertScholarship(View):
    def post(self,request):
        if request.method == 'POST':
            name = request.POST['nombres']
            email = request.POST['correo']
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
                                        program_adm=program,application_type=optionnew,state='Pendiente',
                                        total_periods=totalP,active='AC',date_application=now,id_user=ben,institution=institutionvalue)
                scolarship.save()

                return render(request,'menu.html')
            else:
                scolarship = Scholarship(stratum=levels,photocopy_id=picturedoc, motivational_letter=letter,
                                        certificate=picturecer,value_period=valuesem,icfes_score=icfes,period_current=timeA,
                                        program_adm=program,application_type=optionnew,state='Pendiente',
                                        total_periods=totalP,active='IN',date_application=now,id_user=ben)
                scolarship.save()
  
                return render(request,'menu.html')

class EditSolicitud(View):
    def get(self,request):
        id_ben = request.user.id
        datos_solicitud = Scholarship.objects.filter(id_user=id_ben, active='AC')
        solicitud = datos_solicitud.first()
        institutions = Institution.objects.all()

        contexto = {
            'solicitud_activa': solicitud,
            'institutions': institutions,
        }
        return render(request, 'editionScholarship.html', contexto)

    def post(self,request):
        if request.method == 'POST':

            if 'inactivate_scholarship' in request.POST:
                id_ben = request.user.id
                solicitud = Scholarship.objects.filter(id_user=id_ben, active='AC')
                scholarshipToInactivate = solicitud.first()

                scholarshipToInactivate.active = 'IN'
                scholarshipToInactivate.state = 'Rechazada'
                scholarshipToInactivate.save()
                print(f"Solicitud del usuario {scholarshipToInactivate.id_user.name} ha sido inactivada.")
                return render(request, 'menu.html')

            institute = request.POST['instituc']
            program = request.POST['programa']
            valuesem = request.POST['valorS']
            timeA = request.POST['periodoActual']
            totalP = request.POST['totalPeriodos']
            icfes = request.POST['puntajeI']
            levels = request.POST['estrato']
            optionnew = request.POST['ingresoEstudiante']
            picturedoc = None
            picturecer = None
            try:
                picturedoc = request.FILES['src-file1']
                picturecer = request.FILES['src-file2']
            except:
                print('error')

            now = datetime.now()
            letter = request.POST['cartaMotivacional']

            id_ben = request.user.id
            solicitud = Scholarship.objects.filter(id_user=id_ben, active='AC')
            scholarshipUpdated = solicitud.first()

            scholarshipUpdated.stratum = levels
            scholarshipUpdated.photocopy_id = picturedoc if picturedoc != None else scholarshipUpdated.photocopy_id
            scholarshipUpdated.motivational_letter = letter
            scholarshipUpdated.certificate = picturecer if picturecer != None else scholarshipUpdated.certificate
            scholarshipUpdated.value_period = valuesem
            scholarshipUpdated.icfes_score = icfes
            scholarshipUpdated.period_current = timeA
            scholarshipUpdated.program_adm = program
            scholarshipUpdated.application_type = optionnew
            scholarshipUpdated.total_periods = totalP
            scholarshipUpdated.date_application = now
            institution = get_object_or_404(Institution, id=institute)
            scholarshipUpdated.institution = institution

            scholarshipUpdated.save()
            return render(request, 'menu.html')


class LookBeneficiaries(ListView):
    def get(self, request):
        semester = []
        for i in range(1,13):
            semester.append(i)

        intervals = [(0,2000000),(2000001,5000000),(5000001,10000000),(10000001,20000000),(20000000,50000000)]
        institutions = Institution.objects.all()
        scholarships = Scholarship.objects.all()
        data = {'semesters':semester,'scholarships':scholarships,'institutions':institutions,'intervals':intervals}
        return render(request, 'lookbeneficiaries.html',data)



class FilterSemester(ListView):
    def get(self,request,id):
        semester = []
        for i in range(1,13):
            semester.append(i)
        
        intervals = [(0,2000000),(2000001,5000000),(5000001,10000000),(10000001,20000000),(20000000,50000000)]
        institutions = Institution.objects.all()
        scholarships = Scholarship.objects.filter(period_current=id)
        data = {'scholarships':scholarships,'semesters':semester,'institutions':institutions,'intervals':intervals}
        return render(request,'lookbeneficiaries.html',data)
## Edit Profile

class FilterInstitution(ListView):
    def get(self, request, id):
        semester = []
        for i in range(1,13):
            semester.append(i)

        intervals = [(0,2000000),(2000001,5000000),(5000001,10000000),(10000001,20000000),(20000000,50000000)]
        actualinst = Institution.objects.get(id=id)
        institutions = Institution.objects.all()
        scholarships = Scholarship.objects.filter(institution=actualinst)
        data = {'scholarships':scholarships,'semesters':semester,'institutions':institutions,'intervals':intervals}
        return render(request,'lookbeneficiaries.html',data)

class FilterInterval(ListView):
    def get(self, request, min_value, max_value):
        semester = []
        for i in range(1,13):
            semester.append(i)
        
        intervals = [(0,2000000),(2000001,5000000),(5000001,10000000),(10000001,20000000),(20000000,50000000)]
        scholarships = Scholarship.objects.filter(value_period__gte=min_value, value_period__lte=max_value)
        institutions = Institution.objects.all()
        data = {'scholarships':scholarships,'semesters':semester,'institutions':institutions,'intervals':intervals}
        return render(request,'lookbeneficiaries.html',data)

class FilterProgram(ListView):
    def get(self, request, program_name):
        semester = []
        for i in range(1,13):
            semester.append(i)

        intervals = [(0,2000000),(2000001,5000000),(5000001,10000000),(10000001,20000000),(20000000,50000000)]
        if program_name == 'ingenieria-informatica':
            scholarships = Scholarship.objects.filter(Q(program_adm__icontains=program_name) | Q(program_adm__icontains='sistemas')
                                                      | Q(program_adm__icontains='tecnologia'))
        elif program_name == 'administracion-empresas':
            scholarships = Scholarship.objects.filter(Q(program_adm__icontains=program_name) | Q(program_adm__icontains='marketing')
                                                      | Q(program_adm__icontains='emprendimiento') | Q(program_adm__icontains='contabilidad'))
        elif program_name == 'medicina':
            scholarships = Scholarship.objects.filter(Q(program_adm__icontains=program_name) | Q(program_adm__icontains='salud')
                                                   | Q(program_adm__icontains='enfermeria') | Q(program_adm__icontains='cirujano'))
        elif program_name == 'ingenieria-civil':
            scholarships = Scholarship.objects.filter(Q(program_adm__icontains=program_name) | Q(program_adm__icontains='constructor')
                                                   | Q(program_adm__icontains='arquitecto') | Q(program_adm__icontains='operario'))
        elif program_name == 'psicologia':
            scholarships = Scholarship.objects.filter(Q(program_adm__icontains=program_name) | Q(program_adm__icontains='terapeuta')
                                                | Q(program_adm__icontains='antropologia')    )
        elif program_name == 'derecho':
            scholarships = Scholarship.objects.filter(Q(program_adm__icontains=program_name) | Q(program_adm__icontains='juez')
                                                   | Q(program_adm__icontains='fiscal') | Q(program_adm__icontains='investigador'))
        elif program_name == 'ingenieria-industrial':
            scholarships = Scholarship.objects.filter(Q(program_adm__icontains=program_name) | Q(program_adm__icontains='logistica')
                                                   | Q(program_adm__icontains='calidad') | Q(program_adm__icontains='analisis'))
        elif program_name == 'comunicacion-social':
            scholarships = Scholarship.objects.filter(Q(program_adm__icontains=program_name) | Q(program_adm__icontains='periodismo')
                                                   | Q(program_adm__icontains='reportero') | Q(program_adm__icontains='entrevistador'))
        else :
            scholarships = None

        institutions = Institution.objects.all()
        data = {'scholarships':scholarships,'semesters':semester,'institutions':institutions,'intervals':intervals}
        return render(request,'lookbeneficiaries.html',data)


class LookInstitutions(ListView):
    def get(self, request):
        institutions = Institution.objects.all()
        cities = []

        types = []
        types.append('Tecnica')
        types.append('Tecnologica')
        types.append('Pregrado')
        types.append('Posgrado')
        for i in institutions:
            city = i.city
            if city not in cities:
                cities.append(city)

        data = {'institutions':institutions,'cities':cities,'types':types}
        return render(request, 'lookinstitution.html',data)

class FilterCity(ListView):
    def get(self, request,city):
        institutions = Institution.objects.all()
        cities = []
        for i in institutions:
            cit = i.city
            if cit not in cities:
                cities.append(cit)

        types = []
        types.append('Tecnica')
        types.append('Tecnologica')
        types.append('Pregrado')
        types.append('Posgrado')
        institutions_f = Institution.objects.filter(city=city)
        data = {'institutions':institutions_f,'cities':cities,'types':types}
        return render(request, 'lookinstitution.html',data)

class FilterTypeI(ListView):
    def get(self, request,typeI):
        institutions = Institution.objects.all()
        cities = []
        for i in institutions:
            cit = i.city
            if cit not in cities:
                cities.append(cit)

        types = []
        types.append('Tecnica')
        types.append('Tecnologica')
        types.append('Pregrado')
        types.append('Posgrado')

        institutions_f = Institution.objects.filter(type_institution__contains=typeI)
        data = {'institutions':institutions_f,'cities':cities,'types':types}
        return render(request, 'lookinstitution.html',data)


class SrchView(ListView):
    def post(self, request):
        
            institutions = Institution.objects.all()
            cities = []
            for i in institutions:
                cit = i.city
                if cit not in cities:
                    cities.append(cit)

            types = []
            types.append('Tecnica')
            types.append('Tecnologica')
            types.append('Pregrado')
            types.append('Posgrado')

            value =  request.POST.get('inputsearch')

            institutions_f = Institution.objects.filter(Q(city__icontains=value)| Q(name__icontains=value))
            data = {'institutions':institutions_f,'cities':cities,'types':types}
            return render(request, 'lookinstitution.html',data)


class SrchBenView(ListView):
    def post(self, request):
        
        semester = []
        for i in range(1,13):
            semester.append(i)

        intervals = [(0,2000000),(2000001,5000000),(5000001,10000000),(10000001,20000000),(20000000,50000000)]
        institutions = Institution.objects.all()
        value =  request.POST.get('inputsearch')
        scholarships = Scholarship.objects.filter(Q(program_adm__icontains=value)| Q(id_user__name__icontains=value))
        data = {'semesters':semester,'scholarships':scholarships,'institutions':institutions,'intervals':intervals}
        return render(request, 'lookbeneficiaries.html',data)   




#Show Details
class ShowDetailsBen(TemplateView):
    def get(self,request,id):
        scholarship = Scholarship.objects.get(id=id)
        data = {'scholarship':scholarship}
        return render(request, 'beneficiaryDetailsToDonate.html',data)


class ShowDetailsIns(TemplateView):
    def get(self,request,id):
        institution = Institution.objects.get(id=id)
        data = {'institution':institution}
        return render(request, 'institutionDetails.html',data)
## Edit Profile

class DonationIns(TemplateView):
    def get(self,request,id):
        institution = Institution.objects.get(id=id)
        data = {'institution':institution}
        return render(request, 'institutionDonation.html',data)


class Payments(TemplateView):
    def get(self,request,id):
        institution = Institution.objects.get(id=id)
        data = {'institution':institution}
        return render(request, 'lookpayments.html',data)



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

class TransactionListView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.all()
        context['transactions'] = transactions
        return context

class DonationsListView(TemplateView):
    template_name = 'donationsList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.all()
        context['transactions'] = transactions
        return context

class ScholarshipListView(View):
    def get(self, request):
        state_filter = request.GET.get('state', '')  # Obtener el estado filtrado de la URL
        search_query = request.GET.get('search', '')  # Obtener el término de búsqueda

        scholarships = Scholarship.objects.all()

        if state_filter:
            scholarships = scholarships.filter(state__startswith=state_filter)

        if search_query:
            scholarships = scholarships.filter(Q(id_user__name__icontains=search_query) | Q(id_user__id__icontains=search_query))
        context = {
            'scholarships': scholarships,
            'state_filter': state_filter,
            'search_query': search_query,
        }
        return render(request, 'allScholarships.html', context)


    def post(self, request):
        scholarship_id = request.POST.get('scholarship_id')
        action = request.POST.get('action')

        scholarship = Scholarship.objects.get(pk=scholarship_id)

        if action == 'publicar':
            scholarship.state = 'Aceptada'
        elif action == 'rechazar':
            scholarship.state = 'Rechazada'

        scholarship.save()

        return redirect('scholarships:scholarships')  # Redirigir a la lista de becas
