











from django.shortcuts import render, redirect, get_object_or_404

from .models import Gastos

from django.contrib import messages

def lista_gastos(request):
    gastos = Gastos.objects.all()
    return render(request, 'gastos/visual.html', {'gastos': gastos})
 
def crear_gasto(request):
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        monto = request.POST['monto']
        fecha = request.POST['fecha']

        Gastos.objects.create (
            descripcion=descripcion,
            monto=monto,
            fecha=fecha
           )

        messages.success(request, "Gasto agregado  correctamente ❤")
           

        return redirect('lista')

    return render(request, 'gastos/crear.html', {'gasto': None})


def editar_gasto(request, id):
    gasto = get_object_or_404(Gastos, id=id)

    if request.method == 'POST':
        gasto.descripcion = request.POST['descripcion']
        gasto.monto = request.POST['monto']
        gasto.fecha = request.POST['fecha']
        gasto.save()
        messages.success(request, "Gasto actualizado correctamente ❤")
        return redirect('lista')

    return render(request, 'gastos/editar.html', {'gasto': gasto})


def eliminar_gasto(request, id):
    gasto = get_object_or_404(Gastos, id=id)
    gasto.delete()
    messages.success(request, "Gasto eliminado 🗑️")
    return redirect('lista')


# Create your views here.
