from django.shortcuts import render, redirect
from .models import Product
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView , UpdateAPIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import SignupForm , PasswordchangeForm , PasswordresetForm
from django.contrib.auth import update_session_auth_hash
import requests
from rest_framework.parsers import MultiPartParser, FormParser , FileUploadParser, JSONParser

# Create your views here.


def home(request):
    if request.user.is_authenticated :
        response = requests.get('http://localhost:8000/products/')
        data = response.json()
        # obj = Product.objects.all()
        return render(request,'home.html',{'data':data})
    return redirect('login')


def index(request):
    form = SignupForm
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your account is created successfully, you can login now',extra_tags='alert alert-success')
            return redirect('login')
    return render(request,'index.html',{'form':form})


def custlogin(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email.strip()=='' or password.strip()=="":
            messages.add_message(request,messages.ERROR,'Neither of the fields must be empty',extra_tags='alert alert-danger')
        else:
            user = authenticate(username=email,password=password)
            if (user is not None) and (user.is_admin==False):
                login(request,user)
                messages.add_message(request,messages.SUCCESS,'Login successfull',extra_tags='alert alert-success')
                return redirect('home')
            else:
                messages.add_message(request,messages.ERROR,"Email or password doesn't match",extra_tags='alert alert-danger')
    return render(request,'login.html')


def password_reset(request):
    form = PasswordresetForm
    if request.method=='POST':
        form = PasswordresetForm(request.POST)
        if form.is_valid():
            return redirect('password_reset_done')
    return render(request,'password_reset_form.html',{'form':form})


def password_reset_done(request):
    return render(request,'password_reset_done.html')


def password_reset_confirm(request):
    return HttpResponse('password reset form')


def password_reset_complete(request):
    return HttpResponse('password reset form')







@login_required(redirect_field_name='next')
def custlogout(request):
    logout(request) 
    messages.add_message(request,messages.SUCCESS,'You have been logged out successfully',extra_tags='alert alert-success')   
    return redirect('login')


@login_required(redirect_field_name='next')
def custchangepassword(request):
    form = PasswordchangeForm(request.user)
    if request.method=='POST':
        form = PasswordchangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
    return render(request,'passwordchange.html',{'form':form})


class Productlist(APIView):

    def get(self, request):
        obj = Product.objects.all()
        serializer = ProductSerializer(obj,many=True)
        return Response(serializer.data)


class Productdetail(APIView):

    def get(self, request, prod_id):
        try:
            obj = Product.objects.get(id=prod_id)
            serializer = ProductSerializer(obj)
            return Response(serializer.data)
        except:
            return Response({'message':'Product not found'},status=status.HTTP_400_BAD_REQUEST)


class Productadd(APIView):
    serializer_class= ProductSerializer
    # parser_classes = (JSONParser, FileUploadParser, MultiPartParser, FormParser)


    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        file_obj = request.data.get('file')
        print(file_obj)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['prod_image']=file_obj
            serializer.save()
            return Response({'message':'Product is added successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Productdelete(APIView):

    def delete(self, request, prod_id):
        try:
            obj = Product.objects.get(id=prod_id)
            obj.delete()
            return Response({'message':'Product deleted successfully'},status=status.HTTP_200_OK)
        except:
            return Response({'message':'Product not found'},status=status.HTTP_400_BAD_REQUEST)


class Productupdate(APIView):
    serializer_class= ProductSerializer

    def post(self, request, prod_id):
        try:
            obj = Product.objects.get(id=prod_id)
        except :
            return Response({'message':'Product not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(instance=obj,data=request.data)
        if serializer.is_valid(raise_exception=True):
            obj.updated_on = datetime.now()
            serializer.save()
            return Response({'message':'Product updated successfully'},status=status.HTTP_200_OK)

