from django.shortcuts import render, redirect
from django.views.genreic import View
from .forms import RegistroForm, LoginForm
from django,contrib.auth import login, authenticate

class Registro(View):
    def get(self, request):
        template_name = 'registro.html'
        form = RegistroForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def  post(self,request):
        form = RegistroForm(request.POST)
        username = request.POST.get('usuario')
        password = request.POST.get('contra')
        if form.is_valid():
            form.save()
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
        else:
            return redirect('/registro')

class Login(View):
    def get(self, request):
        template_name = 'login.html'
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            uusername = request.POST.get('usuario')
            password = request.POST.get('contra')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login')
