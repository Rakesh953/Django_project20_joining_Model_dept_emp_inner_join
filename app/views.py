from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
# def equi_join(request):
#     LEDO=Emp.objects.select_related('deptno').all()
#     d={'LEDO':LEDO}
#     return render(request,'equi_join.html',d) 



def equi_join(request):
    LEDO=Emp.objects.select_related('deptno').all() # it will fetch all the data from the table

    LEDO=Emp.objects.select_related('deptno').filter(job='selling') # who's job is selling

    LEDO = Emp.objects.select_related('deptno').filter(comm__isnull=True) # who is not getting comm 

    LEDO = Emp.objects.select_related('deptno').filter(comm__isnull=False) # who is getting comm 

    LEDO = Emp.objects.select_related('deptno').filter(sal__gt=5000) # who is getting >5000 salary

    LEDO = Emp.objects.select_related('deptno').filter(deptno__dname='renewal') # who are working in renewal department 

    LEDO = Emp.objects.select_related('deptno').filter(Q(dname='renewal') & Q(sal__gt=9000))# who are manager is ranjit and earning >9000 
 

    d={'LEDO':LEDO}
    return render(request,'equi_join.html',d) 

def self_join(request):
    LEDMO=Emp.objects.select_related('deptno','mgr').all()

    LEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='renewal') # department name renewal
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='ranjit')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(ename='Rakesh')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='h')  #whose manager name start with h
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__endswith='t')  #whose manager name start with t
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__contains='ji')  #whose manager name character t
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='Design Card') | Q(deptno__dname='Fast Card')) # department name Design Card and Fast Card
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__in=['Design Card', 'Fast Card']) # department name Design Card and Fast Card

    D={'LEDMO':LEDMO}
    return render(request,'self_join.html',D)