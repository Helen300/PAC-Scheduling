from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.template.loader import render_to_string 
from django.conf.urls.static import static
from . import models, studio, hours
from .models import TimeSlot, Hours, ADRequest, CompanyChoice
from .studio import Studio



# Create your views here.

def index(request):
	#return HttpResponse("Hello, World")
	html = render_to_string('templates/pacApp/home.html')
	return HttpResponse(html)

def schedule(request):
	# t1 = models.TimeSlot(company_name="Sympoh", time_start=5, time_end=7,
		# studio="Wilcox")
	# context = {t1.company_name:t1}
	context = {'space_list' : TimeSlot.objects.all()}

	#{'Wilcox': [t1, t2]} t1 = company name, time start, time end 
	# context = {'Wilcox': TimeSlot.objects.all(), 'Bloomberg': TimeSlot.objects.all()}
	# context['space_list'] = TimeSlot.objects.all()
	return render(request, "templates/pacApp/home2.html", context)

def insert_space_item(request: HttpResponse):
	timeSlot = TimeSlot(company_name = request.POST['company_name'], time_start = request.POST['time_start'],
						time_end = request.POST['time_end'], studio = request.POST['studio'])
	timeSlot.save()
	return redirect('/schedule')

def insert_ad_request(request: HttpResponse):
	"""companyc1 = CompanyChoice(company_name=request.POST['company_name'],
							company_day=request.POST.get('company_day_1'),
							company_start_time=request.POST['company_start_time_1'],
							company_end_time=request.POST['company_end_time_1'],
							studio=request.POST.get('company_studio_1'))
	companyc2 = CompanyChoice(company_name=request.POST['company_name'],
							company_day=request.POST.get('company_day_2'),
							company_start_time=request.POST['company_start_time_2'],
							company_end_time=request.POST['company_end_time_2'],
							studio=request.POST.get('company_studio_2'))
	companyc3 = CompanyChoice(company_name=request.POST['company_name'],
							company_day=request.POST.get('company_day_3'),
							company_start_time=request.POST['company_start_time_3'],
							company_end_time=request.POST['company_end_time_3'],
							studio=request.POST.get('company_studio_3'))"""
	ad_req = ADRequest(name = request.POST['name'], 
		company_day_1 = request.POST.get('company_day_1'),
		company_start_time_1 = request.POST['company_start_time_1'],
		company_end_time_1 = request.POST['company_end_time_1'],
		company_studio_1 = request.POST.get('company_studio_1'),
		company_day_2 = request.POST.get('company_day_2'),
		company_start_time_2 = request.POST['company_start_time_2'],
		company_end_time_2 = request.POST['company_end_time_2'],
		company_studio_2 = request.POST.get('company_studio_2'),
		company_day_3 = request.POST.get('company_day_3'),
		company_start_time_3 = request.POST['company_start_time_3'],
		company_end_time_3 = request.POST['company_end_time_3'],
		company_studio_3 = request.POST.get('company_studio_3'),
		rank_1 = request.POST.get('rank1s'), 
		rank_2 = request.POST.get('rank2s'), 
		rank_3 = request.POST.get('rank3s'),
		rank_4 = request.POST.get('rank4s'),
		rank_5 = request.POST.get('rank5s'),
		num_reho = request.POST['num_reho'],
		num_members = request.POST['num_members'])
	ad_req.save()
	return redirect('/adminForm')

def adminForm(request):
	context = {'all_requests' : ADRequest.objects.all()}
	for item in context['all_requests']:
		print(item.name)
	return render(request, "templates/pacApp/adminForm.html", context)

def div(request):
	args = {}
	args['bac'] = [4,5,6]
	args['sympoh'] = [7,8,9]
	args['disiac'] = [9,10,11,12]
	wilcox = Studio('Wilcox', args)
	bloomberg = Studio('Bloomberg', args)
	studios = []
	studios.append(wilcox)
	studios.append(bloomberg)
	context = {'space_list' : studios}
	return render(request, "templates/pacApp/div.html", context)