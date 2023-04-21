from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm

def persona_detail(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'webapp/persona_detail.html', {'persona': persona})

def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
    else:
        form = PersonaForm()
    return render(request, 'webapp/persona_form.html', {'form': form})

def persona_update(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'webapp/persona_form.html', {'form': form})

def persona_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona_list')
    return render(request, 'webapp/persona_confirm_delete.html', {'persona': persona})
