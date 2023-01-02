from django.shortcuts import render, redirect
from .models  import *
from .forms import *
# Create your views here.

def redirect_user(request):

    if request.user.is_superuser:
        return redirect('admin_dash')
    elif request.user.is_staff:
        pass
    else:
        return redirect('user_dash')


def index(request):
    return render(request,'index.html' )
    


def admin_dash(request):
    context =  {}
    context['foods'] = Repas.objects.all()

    return render(request, 'admin_dash/respas.html', context)

def user_dash(request):
    context =  {}
    context['foods'] = Repas.objects.all()

    return render(request, 'client_dash/index.html', context)

#  vues des repas

def create_repas(request):
    context =  {}
    form = RepasForm(request.POST or None, request.FILES or None)
    
    context['title'] = "Création "
    context['message'] = "Enregistrer"
    if request.method == 'POST':
        
        if (form.is_valid()):
            print('POST JS')
            form.save()
            return redirect('admin_dash')
    context['form'] = form
    return render(request, 'admin_dash/form_repas.html',context)


def update_repas(request, id):
    context =  {}
    food = Repas.objects.get(pk = id)
    form = RepasForm(request.POST or None, request.FILES or None, instance = food)
    
    context['title'] = "Modification "
    context['message'] = "Mettre à jour"
    if request.method == 'POST':
        
        if (form.is_valid()):
            print('POST JS')
            form.save()
            return redirect('admin_dash')
    context['form'] = form
    return render(request, 'admin_dash/form_repas.html',context)


def delete_repas(request, id):
    food = Repas.objects.get(pk = id)
    food.delete()

    return redirect('admin_dash')





#  

def create_account(request):
    form = RegistrationForm(request.POST or None)
    context = {}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    context['form'] = form


    return render(request, 'create_account.html',context)
    


#  Menu Management
def menu(request):
    context = {}
    menu = Menu.objects.all()
   
    context['menu'] = menu
    return render(request, 'admin_dash/menu.html', context)

def create_menu(request):
    context = {}
    form = MenuForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('menu')
    context['message'] = "Enregistrer"
    context['title'] = 'Création'
    context['form'] = form
    return render(request, 'admin_dash/menu_form.html', context)


def update_menu(request, id):
    context = {}
    menu = Menu.objects.get(pk = id)
    form = MenuForm(request.POST or None, instance = menu)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('menu')
    context['message'] = "Enregistrer"
    context['title'] = 'Modification '
    context['form'] = form
    return render(request, 'admin_dash/menu_form.html', context)

def delete_menu(request, id):
    menu = Menu.objects.get(pk = id).delete()
    
    return redirect('menu')
   