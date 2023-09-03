import logging
import sys
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from customers.models import Customer
from orders import forms
from orders.forms import OrderForm, CustomerForm, EmailForm
from orders.models import Order
from django import forms

# Create your views here.

def hello_view(request):
    return HttpResponse('Hello World!')
    pass


def success_page(request):
    return render(request, 'success_page.html')
    pass

def home(request):
    return render(request, 'home.html')
    pass


############################# sukuriu loggerį #########################################
# Sukurkite logger objektą
logger = logging.getLogger(__name__)

# Nustatykite norimą žurnalo lygį (Debug, Info, ir kt.)
logger.setLevel(logging.DEBUG)

# Sukurkite StreamHandler ir priskirkite jį logger'io išvesties valdikliui
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

# Sukurkite formato objektą (galite nurodyti norimą išvesties formatą)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Pridėkite valdiklį prie loggerio
logger.addHandler(handler)
logger = logging.getLogger(__name__)


################################### užsakymo forma #########################################
def create_order(request):


    logger = logging.getLogger(__name__)  # Sukurkite logger'į šioje funkcijoje

    logger.debug("Entering create_order function")  # Pavyzdinė žinutė apie funkcijos pradžią

    customer_form = CustomerForm()
    order_form = OrderForm()
    customer = None

    if request.method == 'POST':
        logger.debug("POST request detected")  # Žinutė apie POST užklausą

        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)

        if customer_form.is_valid():
            logger.debug("Customer form is valid")  # Žinutė apie sėkmingą kliento formos validaciją
            customer = customer_form.save()

        if order_form.is_valid():
            logger.debug("Order form is valid")  # Žinutė apie sėkmingą užsakymo formos validaciją
            order = order_form.save(commit=False)
            if customer:
                order.customer = customer
            order.save()

            logger.debug("Order saved")  # Žinutė apie sėkmingą užsakymo išsaugojimą
            return redirect('success_page')

    context = {
        'customer_form': customer_form,
        'order_form': order_form,
    }
    # išsaugojus formos duomenis, atidaromas success_page.html

    logger.debug("Leaving create_order function")  # Pavyzdinė žinutė apie funkcijos pabaigą

    return render(request, 'order.html', context)

    pass
################################### Užsakymų sąrašas #########################################

def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'order_list.html', context)
    pass
#################################### Užsakymo redagavimas #########################################
def order_edit(request, pk):
    order = Order.objects.get(pk=pk)
    customer = order.customer

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        order_form = OrderForm(request.POST, instance=order)

        if customer_form.is_valid() and order_form.is_valid():
            customer_form.save()
            order_form.save()
            return redirect('order_list')
    else:
        customer_form = CustomerForm(instance=customer)
        order_form = OrderForm(instance=order)

    context = {
        'customer_form': customer_form,
        'order_form': order_form,
        'order_id': pk,  # Perduodu order_id šablonui, kad jis žinotų, kurį užsakymą redaguojame
    }

    return render(request, 'order_edit.html', context)
    pass
################################### el laiško siuntimas #########################################
def send_email(request, pk):
    order = Order.objects.get(pk=pk)
    customer = order.customer
    email_form = EmailForm()

    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            subject = email_form.cleaned_data['subject']
            message = email_form.cleaned_data['message']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [customer.customer_email]  # Corrected line
            send_mail(subject, message, email_from, recipient_list)
            return redirect('order_list')
    else:
        email_form = EmailForm()

    context = {
        'email_form': email_form,
        'order_id': pk,
    }
    return render(request, 'send_email.html', context)
    pass
################################### Užsakymo trynimas #########################################
def order_delete(request, pk):
    order = Order.objects.get(pk=pk)
    customer = order.customer

    if request.method == 'POST':
        # Delete the order and customer instances
        order.delete()
        customer.delete()
        return redirect('order_list')
    else:
        # Handle the GET request here
        customer_form = CustomerForm(instance=customer)
        order_form = OrderForm(instance=order)

    context = {
        'customer_form': customer_form,
        'order_form': order_form,
        'order_id': pk,
    }
    return render(request, 'order_delete.html', context)




################################# Rūšiavimas pagal stutusą #########################################
def order_list(request):
    orders = Order.objects.all().order_by('order_status')  # Order the queryset by order_status
    context = {'orders': orders}
    return render(request, 'order_list.html', context)
    pass

################################## Laikrodis ir Data #############################################
def laikas_ir_data(request):
    dabartinis_laikas = datetime.datetime.now()
    return render(request, 'laikas_ir_data.html', {'dabartinis_laikas': dabartinis_laikas})
    pass


