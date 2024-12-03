from django.http import HttpResponse
from django.template import loader
from .models import Member,Learn,Akshada,Fil,Mohan
from django.shortcuts import render, redirect
from .form import UserInputForm, learninput, Akshada,Moha,Filf
from django.db import models
from django.contrib.auth import authenticate, login
import subprocess
from django.core.files.storage import FileSystemStorage
from subprocess import run, PIPE
import json
from django.conf import settings


def mohan(req):
   if req.method == 'POST':
     # with form
     #read
    dic = Mohan.objects.all()

    if req.POST.get('submit') == 'create':
         #create
         m1 = Moha(req.POST)
         if m1.is_valid():
            m1.save()
            msg = "success"
         else:
            msg = "failure"
         return render(req,'mohan.html',{'msg':msg,'dic':dic})
    
    elif req.POST.get('submit') == 'Update':
        #update
        instan = Mohan.objects.get(id=req.POST.get('id'))  
        m1 = Moha(req.POST,instance=instan)
        m1.save()
        return render(req,'mohan.html',{'dic':dic})
    
    elif req.POST.get('submit') == 'delete':
        #delete
        instan = Mohan.objects.get(id=req.POST.get('id'))  
        instan.delete()
        return render(req,'mohan.html',{'dic':dic})
    

     # without form
    #  if req.POST.get('submit') == 'Update': 
    #   # update
    #   id = req.POST.get('id')
    #   name = req.POST.get('name')
    #   instan = Mohan.objects.get(id=id)
    #   instan.name = name
    #   instan.save()
    #   print(name)
    #   dic = Mohan.objects.all()
    #   return render(req,'mohan.html',{'dic':dic})
     
    #  elif req.POST.get('submit') == 'create':
    #     #create
    #     name = req.POST.get('name')
    #     Mohan.objects.create(name = name)
    #     dic = Mohan.objects.all()
    #     return render(req,'mohan.html',{'dic':dic})
       
     
    #  elif req.POST.get('submit')== 'delete':
    #     #delete
    #     id = req.POST.get('id')
    #     name = req.POST.get('name')
    #     instan = Mohan.objects.get(id=id)
    #     instan.delete()   
    #     return render(req,'mohan.html')
     
    #  #read
    #  dic = Mohan.objects.all()
    #  return render(req,'mohan.html',{'dic':dic})
   else:
      dic = Mohan.objects.all()
      return render(req,'mohan.html',{'dic':dic})
      

def members(req):
  template = loader.get_template('home.html')   
  return HttpResponse(template.render())


def learn(request):
   if request.method == 'POST':
        fname = request.POST.get('name')
        lname = request.POST.get('email')
        # email = request.POST.get('email')
        passw = request.POST.get('pass')
        # obj = Member.objects.all().values()
        form = learninput(request.POST)
        # print(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Learn.objects.filter(email=email).exists():
                return render(request, 'learnlaugh.html', {'form': form, 'error_message': 'Member with this email already exists.'})
            else:
                form.save()
                return redirect('learnlaugh.html')  # Redirect to a success page
        # else:
        #     print("yess")
        #     form = UserInputForm()
        #     return render(request, 'register.html', {'form': form})    
   else:
        print("yess")
        form = learninput()
        return render(request, 'learnlaugh.html', {'form': form})
   template = loader.get_template('learnlaugh.html')   
   return HttpResponse(template.render())

def back(req):
  template = loader.get_template('back.jpg')   
  return HttpResponse(template.render())


def navbar(req):
  template = loader.get_template('navbar.html')   
  return HttpResponse(template.render())



def login(req):
  if req.method == 'POST':
     email = req.POST.get('email')
     passw = req.POST.get('password')
     obj = Member.objects.all().values()

     for x in obj:
        if x['email'] == email and x['password'] == passw:
         id = x['id']
         return render(req,'hashs.html',{'id':id,'msg':'Welcome To Hashware ' + x['firstname']})    
     error_message = "Invalid email or password. Please try again."
     return render(req, 'logins.html', {'error_message': error_message})
  template = loader.get_template('logins.html')   
  return HttpResponse(template.render())


def hash(req):
  if req.method == 'POST': 
     que = req.POST.get('hash')
     try:
      # Run the command with subprocess.run and capture output
      result = subprocess.run('curl --data "query=get_info&hash="'+que+'"" https://mb-api.abuse.ch/api/v1/', capture_output=True, text=True,shell=True)
      # result = subprocess.run('curl --data "query=get_info&hash=7de2c1bf58bce09eecc70476747d88a26163c3d6bb1d85235c24a558d1f16754 https://mb-api.abuse.ch/api/v1/', capture_output=True, text=True,shell=True)

      output = result.stdout
      print(type(output))
      # Check for errors
      if result.returncode != 0:
          print("nope"+str(result.returncode))
          context={
             'err': "Unknown Hash"
          }
          return render(req,'hashs.html',context)
      else:    
          data = json.loads(output)
          d = data['data']
          rdata = d[0]
          vendor = rdata['vendor_intel']
          revlab = vendor['ReversingLabs']
          
          print(data)
          context = {
             'd': data['data'],
             'file_name' : rdata['file_name'],
              'file_size' : rdata['file_size'],
               'file_type' : rdata['file_type'],
                'file_type_mime' : rdata['file_type_mime'],
                 'first_seen' : rdata['first_seen'],
                  'origin_country' : rdata['origin_country'],
                   'signature' : rdata['file_name'],
                    'imphash' : rdata['file_name'],
                     'tlsh' : rdata['tlsh'],
                     'telfhash' : rdata['telfhash'],
                     'ssdeep' : rdata['ssdeep'],
                      'archive_pw' : rdata['archive_pw'],
                     'delivery_method': rdata['delivery_method'],
                       'threat_name': revlab['threat_name'],
                       'status' : revlab['status']

          }
          print(context)
          return render(req,'table.html',context)
      # Return the output as a response (sanitize if needed)
      # print(output)
     except (subprocess.CalledProcessError, PermissionError) as e:
       print(f"Exception bolte {e}")
      #  response = result.stdout
      #  return render(req, 'hash.html', {'response': response})
    # except Exception as e:
    #     return HttpResponse(str(e), status=500)
  template = loader.get_template('hashs.html')   
  return HttpResponse(template.render())



def style(req):
  template = loader.get_template('style.css')   
  return HttpResponse(template.render())


def malhome(req):
  template = loader.get_template('malhome.html')   
  return HttpResponse(template.render())


def akshada(req):
  template = loader.get_template('Akshada.html')   
  return HttpResponse(template.render())


def feed(request): 
   if request.method == 'POST' and 'file' in request.FILES:
      # in db
      obj = Filf(request.POST,request.FILES)
      all = Fil.objects.all()

      if obj.is_valid():
         obj.save()
         print("got in")

         # using filesystemsstorage class
      # file = FileSystemStorage(location=r"C:\Users\Parth\OneDrive\Desktop\Academics\Software Engineering\django\hashware\file\Media")
      # fs = request.FILES['file']
      # name = file.save(fs.name,fs)
      # up = file.url(name)
      # print(up)
      return render(request, 'FeedBack.html',{'all':all})
   else:      
        request.session['parc'] = 10
        # request.set_cookie('cook','cook',max_age=3600)
        sess = request.session.get('parc')
        print("yess")
        # form = Akshada()
        c = request.COOKIES.get('cook')
        res = render(request, 'FeedBack.html',{'s':sess,'c':c})
        res.set_cookie('cook','cook',max_age=10) 
        return res
   
   

def table(req):
  obj = Member.objects.all().values()
  template = loader.get_template('table.html')
  context = {
     'objs' : obj,
  }   
  return HttpResponse(template.render(context,req))


 

def user_input_view(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        # email = request.POST.get('email')
        passw = request.POST.get('pass')
        # obj = Member.objects.all().values()
        form = UserInputForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Member.objects.filter(email=email).exists():
                return render(request, 'hashs.html', {'form': form, 'error_message': 'Member with this email already exists.'})
            else:
                form.save()
                return redirect('logins.html')  # Redirect to a success page
        # else:
        #     print("yess")
        #     form = UserInputForm()
        #     return render(request, 'register.html', {'form': form})    
    else:
        print("yess")
        form = UserInputForm()
    return render(request, 'registers.html', {'form': form})









