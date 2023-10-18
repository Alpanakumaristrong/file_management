from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from fileapp.models import file_column,file_upload

import pandas as pd

from django.shortcuts import render, redirect
from .models import file_upload, file_column
import pandas as pd
from .forms import FileColumnForm


def upload_file(request):
    if request.method=='POST':
        file2=request.FILES["file"]
  
        # document=file_upload.objects.create(file=file2)
        # document.save()
        # # df.save()
        df=pd.read_excel(file2)
        print(df,"_______________")

        try:
                # df=pd.read_excel(file2)
                for index,row in df.iterrows():
   
                    objs=file_column.objects.create(
                        OEM=row['OEM'],
                        Hardware_Type=row['Hardware Type'],
                        Equipment_description=row['Equipment description(BBU & RRU NAME AS PER C Column SELECTION )'],
                        Supported_Cards=row['Supported Cards'],
                        Technology_Supported=row['Technology Supported'],
                        Techninal_Description=row['Techninal Description'],
                        Capacity=row['Capacity'],
                        MAX_POWER=row['MAX POWER'],
                        Remarks=row['Remarks'],
                    )
                    objs.save()
                    # objs_all = file_column.objects.all()
                    # context={
                    #     'objs':objs_all
                    #     }
                return redirect('show_database')
        except Exception as e:
                pass
               
    return render(request,'home.html')

def show_database(request):

    objs_all = file_column.objects.all()
    context={
        'objs':objs_all
        }
        
    return render(request,'base.html',context)
  

def delete(request,id):
    if request.method=='POST':
        try:
            item=file_column.objects.get(pk=id)
            # item=get_object_or_404(file_column,pk=id)
            item.delete()
            return redirect("show_database")
        except file_column.DoesNotExist:
            pass
      
    return render(request,'base.html')  

def edit(request,id):

    edit_data=file_column.objects.get(pk=id)
    form=FileColumnForm(request.POST,instance=edit_data)
    
    if request.method=='POST':
        if form.is_valid():
            form.save()
            print("successfully") 
            return redirect('show_database')  
   
    context={
                'form':form,
              'edit_data':edit_data
         }
    return render(request,'edit.html',context)   
        
def create(request):
    if request.method=='POST':
        OEM=request.POST.get('OEM')
        Hardware_Type=request.POST.get('Hardware_Type')
        Equipment_description=request.POST.get('Equipment_description')
        Supported_Cards=request.POST.get('Supported_Cards')
        Technology_Supported=request.POST.get('Technology_Supported')
        Techninal_Description=request.POST.get('Techninal_Description')
        Capacity=request.POST.get('Capacity')
        MAX_POWER=request.POST.get('MAX_POWER')
        Remarks=request.POST.get('Remarks')
        obj=file_column.objects.create(
            OEM= OEM,
            Hardware_Type= Hardware_Type,
            Equipment_description=Equipment_description,
            Supported_Cards=Supported_Cards,
            Technology_Supported=Technology_Supported,
            Techninal_Description= Techninal_Description,
            Capacity= Capacity,
            MAX_POWER=MAX_POWER,
            Remarks= Remarks,
             
        )
        obj.save()
        return redirect('create')
        
        # return render(request,'create.html')
    # return redirect('show_database')    
    return render(request, 'create.html')            
    # return redirect('show_database')

# def dashboard(request):
#     obj=file_upload.objects.all()
#     return render (request,'base.html',{'obj':obj})

# def stu_file(request):
#     obj=file_upload.objects.all()
#     context={
#         "data":obj
#     }
#     return render(request,'base.html',context)

    