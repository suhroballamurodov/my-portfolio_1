from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import ContactForm
from django.views.generic.edit import CreateView
from .models import *
from django.urls import reverse_lazy
from .serializer import *
from rest_framework import viewsets, generics
from django.views.decorators.csrf import csrf_protect


def portfolio_details(request):
    return render(request, 'portfolio_details.html', {})

def main(request):
    return render(request, 'index.html', {})

def telegram(request):
    return render(request, 'telegram.html',{})

def web(request):
    return render(request, 'web.html', {})

# def motions(request):
#     return render(request, 'motions.html', {})


# @csrf_protect
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_success')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES)
        if contact_form.is_valid():
            information = contact_form.save()
            return redirect('contact_success')
    form = ContactForm()
    return render(request, "contact.html", {'form':form})


def contact_success(request):
    return render(request, 'contact_success.html')


# @api_view(['POST'])
# def updateDataOne(request, pk):
#     post = Post.objects.get(id=pk)
#     serializers = DataSerializer(post, data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#     return Response(serializers.data)

# API uchun

# @api_view(['GET', 'POST'])
# def get(request):
#     if request.method == 'GET':
#         post = Post.objects.all()
#     # app = ContactModel.objects.all()
#         serializer = DataSerializer(post, many=True)
#     return Response(serializer.data)


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
 


''' Bu ikkinchi yo'l'''
# def contact(request):
#     form = ContactForm()

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             # Boshqa qanday ma'lumotlarni olish va validatsiya
#             # fuqarolarga xabar berish uchun
#             form = ContactForm()

#     return render(request, 'contact.html', {'form': form})

# def contact_success(request):
#     return render(request, 'contact_success.html')


# class ContactView(CreateView):
#     model = ContactModel
#     template_name = 'contact.html'
#     fields = ('ism','email','subyect','xabar')
#     success_url = reverse_lazy('contact_success')