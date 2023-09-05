from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from customers.models import Customer
from orders.forms import CustomerForm

# Create your views here.
################################### Klientų sąrašas #########################################
@login_required

def customer_list(request):
    customers = Customer.objects.all()
    order_id = request.GET.get('order_id')  # Gauti užsakymo ID iš GET parametrų
    context = {
        'customers': customers,
        'order_id': request.GET.get('order_id')  # Gauti užsakymo ID iš GET parametrų
    }
    return render(request, 'customer_list.html', context)

#################################Kliento ištrynimas #########################################
@login_required

def customer_delete(request, pk):
    customer = Customer.objects.get(pk=pk)

    if request.method == 'POST':
        # Delete the related orders and then delete the customer
        customer.order_set.all().delete()
        customer.delete()
        return redirect('customer_list')
    else:
        customer_form = CustomerForm(instance=customer)
        # Assuming you have the ForeignKey relationship, get the related orders
        orders = customer.order_set.all()

    context = {
        'customer_form': customer_form,
        'orders': orders,
        'customer_id': pk,
    }
    return render(request, 'customer_delete.html', context)