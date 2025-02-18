from django.shortcuts import render, redirect
from . import models

def receipes(request):
    if request.method == 'POST':
        receipe_image = request.FILES.get('file')
        receipe_name = request.POST.get('name')
        receipe_desc = request.POST.get('desc')
        models.Receipe.objects.create(receipe_name= receipe_name, receipe_desc= receipe_desc, receipe_image= receipe_image)
        return redirect('receipes')
    
    query_set = models.Receipe.objects.all()

    if request.GET.get('search_re'):
        query_set = query_set.filter(receipe_name__icontains = request.GET.get('search_re'))

    context = {'receipes': query_set}

    return render(request, 'vege/receipes.html', context)


def delete_receipe(request, id):
    query_set = models.Receipe.objects.get(id= id)
    query_set.delete()
    
    return redirect('receipes')



def update_receipe(request, id):
    query_set = models.Receipe.objects.get(id= id)
    context = {'receipe': query_set}

    if request.method == 'POST':
        receipe_image = request.FILES.get('file')
        receipe_name = request.POST.get('name')
        receipe_desc = request.POST.get('desc')

        query_set.receipe_name = receipe_name
        query_set.receipe_desc = receipe_desc

        if receipe_image:
            query_set.receipe_image = receipe_image

        query_set.save()

        return redirect('receipes')



    
    
    return render(request, 'vege/update.html', context)