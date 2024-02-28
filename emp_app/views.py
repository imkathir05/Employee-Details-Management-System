from django.shortcuts import render,HttpResponse
from .models import Employee,Department,Role
import datetime
from django.db.models import Q

def index(request):
    return render(request,'index.html')

def all_emp(request):
    employee=Employee.objects.all()
    return render(request,'view_all_emp.html',{'emps':employee})
    

def add_emp(request):
    if request.method == 'POST':
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        salary=int(request.POST["salary"])
        bonus=int(request.POST["bonus"])
        phone=int(request.POST["phone"])
        dept=int(request.POST["dept"])
        role=int(request.POST["role"])
        new_emp=Employee(first_name = first_name,last_name = last_name,salary = salary,bonus = bonus,phone = phone,dept_id = dept,role_id = role,hire_date = datetime.datetime.now() )
        new_emp.save()
        return HttpResponse('Employee Details Added Successfully')
    else:  
        return render(request,'add_emp.html')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Successfully Removed')
        except:
            return HttpResponse('Please Enter Valid EMP ID')
    employees=Employee.objects.all()
    return render(request,'remove_emp.html',{'empss':employees})

def filter_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if first_name:
            emps=emps.filter(first_name=first_name)
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        return render(request,'view_all_emp.html',{'emps':emps})
    elif request.method=='GET':
        return render(request,'filter_emp.html')


