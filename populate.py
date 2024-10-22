import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelproject3.settings')
import django
django.setup()

from testapp.models import HydJobs
from testapp.models import PuneJobs
from testapp.models import BngJobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
    d1 = randint(6,9)
    num = ''+str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)
#['date','company','title','eligibility','address','email','phonenumber']
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd','Mahesh Sir Student'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_jobs_record = HydJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )
        Pune_jobs_record = PuneJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )
        Bng_jobs_record = BngJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )
n = int(input('Enter Number Of Records:'))
populate(n)
print(f'{n} Records inserted successfully')