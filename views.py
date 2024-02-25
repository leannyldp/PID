from django.shortcuts import render, redirect 
from .models import Trabajador, NivelEscolaridad, CategoriaDocente, CategoriaCientifica
from .forms import TrabajadorAddForm

# Create your views here.
def home(request):
    return render(request, "trabajador.html")

def index(request):
    o_all = Trabajador.objects.order_by('-id').all()
    context = { "o_all": o_all }
    return render(request, 'trabajador.html', context=context)

def add(request):
    context = {
        'nombre_form': request.POST.get('nombre', ''),
        'apellidos_form': request.POST.get('apellidos', ''),
        'ci_form': request.POST.get('ci', ''),
        'direccion_form': request.POST.get('direccion', ''),
        'nivel_escolaridad_form': request.POST.get('nivel_escolaridad', ''),
        'categoria_docente_form': request.POST.get('categoria_docente', ''),
        'categoria_cientifica_form': request.POST.get('categoria_cientifica', ''),
    }
    if request.method == 'POST':
        form = TrabajadorAddForm(request.POST)
        if form.is_valid():
            nivel_escolaridad = NivelEscolaridad.objects.get(id=form.cleaned_data['nivel_escolaridad'])
            categoria_docente = CategoriaDocente.objects.get(id=form.cleaned_data['categoria_docente'])
            categoria_cientifica = CategoriaCientifica.objects.get(id=form.cleaned_data['categoria_cientifica'])
            trabajador = Trabajador.objects.create(
                nombre=form.cleaned_data['nombre'], 
                apellidos=form.cleaned_data['apellidos'], 
                ci=form.cleaned_data['ci'], 
                direccion=form.cleaned_data['direccion'], 
                nivel_escolaridad=nivel_escolaridad, 
                categoria_docente=categoria_docente,
                categoria_cientifica=categoria_cientifica
            )


        return redirect('trabajador')


        if trabajador is not None:
                messages.success(request, 'Se ha agregado el trabajador correctamente', 'alert alert-success alert-lng')
                return redirect('trabajador')
        else:
                messages.error(request, 'Ha ocurrido un error al crear el trabajador', 'alert alert-danger alert-lng')

    return render(request, 'add.html', context=context)


def edit(request, pk = None):
    o = trabajador.objects.filter(id=pk)
    if not o.exists():
        messages.error(request, 'No se ha encontrado el trabajador a modificar', 'alert alert-danger alert-lng')
        return redirect('trabajador')
    o = o.first()
    if request.method == 'POST':
        form = trabajadorEditForm(request.POST, instance=o)
        if form.is_valid():
            o.nombres= form.cleaned_data['nombres']
            o.apellidos = form.cleaned_data['apellidos']
            o.ci = form.cleaned_data['ci']
            o.direccion = form.cleaned_data['direccion']
            o.nivel_escolaridad = form.cleaned_data['nivel_escolaridad']
            o.categoria_docente = form.cleaned_data['categoria_docente']
            o.categoria_cientifica = form.cleaned_data['categoria_cientifica']
            o.save()
            messages.success(request, 'Se ha modificado el trabajador correctamente', 'alert alert-success alert-lng')
            return redirect('user')
        else:
            messages.error(request, list(form.errors.as_data().values())[0][0].message, 'alert alert-danger alert-lng')
            return redirect('user-edit', o.id)
    return render(request, 'edit.html', {'o': o})


def delete(request, pk = None):
    o = trabajador.objects.filter(id=pk)
    if not o.exists():
        messages.error(request, 'No se ha encontrado el trabajador a eliminar', 'alert alert-danger alert-lng')
        return redirect('trabajador')
    o = o.first()
    if o.apellidos == 'Administrador':
        messages.error(request, 'No se ha encontrado el trabajador a eliminar', 'alert alert-danger alert-lng')
        return redirect('trabajador')
    o.status = False
    o.save()
    messages.success(request, 'Se ha eliminado el trabajador correctamente', 'alert alert-success alert-lng')
    return redirect('trabajador')
    