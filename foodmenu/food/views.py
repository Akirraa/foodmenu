from django.shortcuts import redirect, render
from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic import DeleteView,CreateView


# Create your views here.
"""def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request, 'food/index.html', context)"""

class indexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

"""
def detail(request,item_id):
    item_details = Item.objects.get(pk=item_id)
    context = {
        'item': item_details,
    }
    return render(request, 'food/details.html', context)
"""

class detailClassView(DeleteView):
    model = Item
    template_name = 'food/details.html'


def create(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render (request, 'food/form.html',{'form':form})

class createClassView(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def edit(request,item_id):
    item = Item.objects.get(id = item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    context = {
        'form':form,
        'item':item,
    }
    return render(request, 'food/form.html', context)

def delete(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete.html', {'item':item})
