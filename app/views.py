from django.shortcuts import render, redirect
from .models  import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
def redirect_user(request):

    if request.user.is_superuser:
        return redirect('admin_dash')
    elif request.user.is_staff:
        pass
    else:
        return redirect('user_dash')


def index(request):
    return render(request,'index.html' )
    

@login_required
@permission_required('is_superuser')
def admin_dash(request):
    context =  {}
    context['foods'] = Repas.objects.all()

    return render(request, 'admin_dash/respas.html', context)

@login_required
def user_dash(request):
    context =  {}
    context['foods'] = Repas.objects.all()

    return render(request, 'client_dash/index.html', context)

#  vues des repas

@login_required
@permission_required('is_superuser')
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


@login_required
@permission_required('is_superuser')
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

@login_required
@permission_required('is_superuser')
def delete_repas(request, id):
    food = Repas.objects.get(pk = id)
    food.delete()

    return redirect('admin_dash')
@login_required

def commander_repas(request, id):
    context = {}
    form = CommandeForm(request.POST or None)
    repas = Repas.objects.get(pk = id)
    if request.method == 'POST':
        if form.is_valid():
            command = form.save(commit = False)
            command.client = request.user
            command.plat = repas
            command.save()
            return redirect('menu_page')
    context['message'] = "Commander"
    context['form'] = form
    return render(request, 'commander.html', context)




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


#  Command management
@login_required
@permission_required('is_superuser')
def command_list(request):

    context = {}
    context['commande_repas'] = Commande.objects.all()
    context['commande_menu'] = Commande_menu.objects.all()
    return render(request, 'admin_dash/commandes.html', context)


#  Menu Management
@login_required
@permission_required('is_superuser')
def menu(request):
    context = {}
    menu = Menu.objects.all()
   
    context['menu'] = menu
    return render(request, 'admin_dash/menu.html', context)
@login_required 
@permission_required('is_superuser')
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

@login_required
@permission_required('is_superuser')
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

@login_required
@permission_required('is_superuser')
def delete_menu(request, id):
    menu = Menu.objects.get(pk = id).delete()
    
    return redirect('menu')
   

def menu_page(request):
    context = {}
    context['menu'] = Menu.objects.all()
    context['message'] = 'Menu'
    return render(request,'menu_list.html', context)


def menu_details(request, id):
    context = {}
    context['menu'] = Menu.objects.get(pk = id)
    context['message'] = f'Details sur le menu : {context["menu"].Nom_du_menu}'
    return render(request, 'menu_details.html', context)

@login_required
def commander_menu(request, id):
    context = {}
    form = Commande_menuForm(request.POST or None)
    menu = Menu.objects.get(pk = id)
    if request.method == 'POST':
        if form.is_valid():
            command = form.save(commit = False)
            command.client = request.user
            command.menu = menu
            command.save()
            return redirect('menu_page')
    context['message'] = "Commander"
    context['form'] = form
    return render(request, 'commander.html', context)


@login_required
def command_list_user(request):

    context = {}
    context['commande_repas'] = Commande.objects.filter(client = request.user)
    context['commande_menu'] = Commande_menu.objects.filter(client = request.user)
    return render(request, 'client_dash/user_command.html', context)

@login_required
def resrvation_list_user(request):

    context = {}
    
    return render(request, 'client_dash/reservation.html', context)
