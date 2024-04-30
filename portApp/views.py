from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Devedores
import datetime
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        devedores = Devedores.objects.all()
        context = {'devedores': devedores}
        return render(request, "index.html", context)
    
    def post(self, request):
        pagou = request.POST.get('pago')
        n_pagou = request.POST.get('nao pagou')
        if pagou:
            dev = Devedores.objects.filter(id=pagou).update(pagou=True, data_modificacao=datetime.date.today())
            devedores = Devedores.objects.all()
            context = {'devedores': devedores}
            return render(request, "index.html", context)
        if n_pagou:
            dev = Devedores.objects.filter(id=n_pagou).update(pagou=False, data_modificacao=datetime.date.today())
            devedores = Devedores.objects.all()
            context = {'devedores': devedores}
            return render(request, "index.html", context)

class CadastrarView(TemplateView):
    template_name = "cadastrar.html"

    def post(self, request):
        nome = str(request.POST.get('nome'))
        descricao = str(request.POST.get('descricao'))
        valor = float(request.POST.get('valor'))

        if nome and descricao and valor:
            novo_devedor = Devedores(cliente=nome, divida=valor, descricao=descricao)
            novo_devedor.save()
            context = {'sucesso': 'devedor cadastrado com sucesso'}
            return render(request, "cadastrar.html", context)
        else:
            context = {'sucesso': 'Preencha todos os campos'}
            return render(request, "cadastrar.html", context)