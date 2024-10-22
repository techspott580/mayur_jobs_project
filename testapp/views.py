from django.shortcuts import render
from testapp.models import HydJobs
from testapp.models import PuneJobs
from testapp.models import BngJobs
# Create your views here.
def homepage_view(request):
    return render(request,'index.html')
def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'hydjobs.html',my_dict)
def Punejobs_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'Punejobs.html',my_dict)
def Bngjobs_view(request):
    jobs_list = BngJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'BngJobs.html',my_dict)