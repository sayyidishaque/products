from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import fruits, vegetables, kidsitem
from .forms import fruitsform, vegform, kidform


# Create your views here.
def index(request):
    fruit = fruits.objects.all()
    veg = vegetables.objects.all()
    kid = kidsitem.objects.all()
    context = {
        'fruits': fruit,
        'veg': veg,
        'kid': kid
    }
    return render(request, 'index.html', context)


def details(request, item, item_id):
    item_models = {
        'fruits': fruits,
        'vegetables': vegetables,
        'kidsitem': kidsitem
    }

    item_model = item_models.get(item)
    if item_model:
        data = item_model.objects.get(id=item_id)
        context = {'data': data, 'group': item}
        return render(request, 'details.html', context)
    else:
        return HttpResponse('invalid item')


def add(request):
    if request.method == 'POST':
        group = request.POST.get('group', '')
        name = request.POST.get('name', '')
        disc = request.POST.get('disc', '')
        rate = request.POST.get('rate', '')
        image = request.FILES.get('image', '')

        if group == 'fruits':
            new_product = fruits(name=name, disc=disc, rate=rate, pic=image)
        elif group == 'vegetables':
            new_product = vegetables(name=name, disc=disc, rate=rate, pic=image)
        elif group == 'kidsitem':
            new_product = kidsitem(name=name, disc=disc, rate=rate, pic=image)
        else:
            messages.warning(request, 'Invalid category')
            return redirect('add')

        new_product.save()
        messages.success(request, 'Product added successfully')
        return redirect('/')
    else:
        return render(request, 'add.html')


def update(request, item, item_id):
    group = item
    if group == "fruits":
        item_nu = fruits.objects.get(id=item_id)
        form = fruitsform(request.POST or None, request.FILES, instance=item_nu)
    elif group == "vegetables":
        item_nu = vegetables.objects.get(id=item_id)
        form = vegform(request.POST or None, request.FILES, instance=item_nu)
    elif group == "kidsitem":
        item_nu = kidsitem.objects.get(id=item_id)
        form = kidform(request.POST or None, request.FILES, instance=item_nu)
    else:
        return HttpResponse('no data to edit')
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'up_id': item_nu, })


def delete(request, item, item_id):
    if request.method == 'POST':
        group = item
        if group == 'fruits':
            obj_del = fruits.objects.get(id=item_id)
            obj_del.delete()
        elif group == 'vegetables':
            obj_del = vegetables.objects.get(id=item_id)
            obj_del.delete()
        elif group == 'kidsitem':
            obj_del = kidsitem.objects.get(id=item_id)
            obj_del.delete()
        return redirect('/')
    else:
        return render(request, 'delete.html', {'item': item, 'item_id': item_id})
