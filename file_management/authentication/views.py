from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login ,logout
from .models import CustomUser,File,Subject,Department,AcademicYear
from django.http import HttpResponse,HttpResponseRedirect,FileResponse
import os
from django.conf import settings
from django.urls import reverse
# Create your views here.


def login_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if  user is not None:
            login(request,user)
            return render(request,'profile.html')
        else:
            return HttpResponse(user)
    return render(request,'login_.html')


def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_'))


def user_details(uni_id,email,profession,is_staff,password,section,aca_year,department,name):
    user=CustomUser(
        username=uni_id,
        email=email,
        name=name,
        uni_id=uni_id,
        profession=profession,
        sections=section,
        academic_year=aca_year,
        department=department,
        )
    user.is_staff=is_staff
    user.set_password(password)
    user.save()

def userprofile(request):
    user=request.user
    context={
        'username':user.username,
        'name':user.name,
        'email':user.email,
        'uni_id':user.uni_id,
        'department':user.department,
        'profession':user.profession,
        'section':user.sections,
        'name':user.name,
        'year':user.academic_year
    }
    return render(request,'profile.html',context)


def upload(request):
    user = request.user
    subjects = Subject.objects.all()
    departments = Department.objects.all()
    academic_year=AcademicYear.objects.all()
    if request.method == 'POST':
        file = request.FILES['file']
        subject = request.POST['subject']
        file_name = request.POST['file_name']
        owner = user.uni_id
        department = request.POST['department']
        aca_year = request.POST['year']
        upload = File(file=file, subject=subject, owner=owner, file_name=file_name, department=department, academic_year=aca_year)
        upload.save()
        return HttpResponseRedirect(reverse(viewpage))
    
    return render(request, 'upload_file.html', {'uni_id': user.uni_id, 'subjects': subjects, 'departments': departments,'academic_year':academic_year})


def viewpage(request):
    user=request.user
    user_dep=user.department
    department=get_object_or_404(Department,name=user_dep)
    subjects=Subject.objects.filter(department=department)
    context={'subjects':subjects}
    return render(request,'viewpage.html',context)


def viewfile(request):
    sub_name = request.GET.get('sub_name', '')
    sub=get_object_or_404(Subject,name=sub_name)
    files=File.objects.filter(subject=sub)
    context={'files': files}
    return render(request,'view_file.html',context)


def download(request,filename):
    abs_path = os.path.normpath(os.path.join(settings.MEDIA_ROOT, filename))
    print(f"Absolute path: {abs_path}")
    if os.path.exists(abs_path):
        with open(abs_path, 'rb') as file:
            myfile=FileResponse(file)
            response = HttpResponse(myfile,content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(abs_path)}"'
            return response
    else:
        return HttpResponse('File not found', status=404)