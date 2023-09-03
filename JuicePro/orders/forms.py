from django import forms

from customers.models import Customer
from .models import Order


################################# forma el. pašto siuntimui užsakyme nurodytu el paštu#########################################
class EmailForm(forms.Form):
    subject = forms.CharField(
        label='Tema',
        max_length=100,
        initial='Jūsų užsakymas įvykdytas')
    message = forms.CharField(
        label='Žinutė',
        max_length=500,
        widget=forms.Textarea,
        initial=(
            'Sveiki,\n\n'
            f'Jūsų užsakymas įvykdytas. \n\n'
            'Dėkojame, kad pasirinkote mūsų paslaugas.\n\n'
            'Linkime geros dienos.\n\n'
            'Su pagarba,\n\n'
            'jPro komanda'))
    pass

######################################  Kliento forma #############################################

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = '__all__'  # Jei norite visus laukus, arba galite išvardinti tik tuos, kuriuos norite įtraukti

    pass
######################################  Užsakymo forma #############################################
class OrderForm(forms.ModelForm):
    order_notes = forms.CharField(label='Pastabos', max_length=200, required=False)
    class Meta:
        model = Order
        fields = '__all__'

  # Jei norite visus laukus, arba galite išvardinti tik tuos, kuriuos norite įtraukti
    #     išvardinti laukus kurie nebus rodomi formoje
    #     exclude = ['customer']

    pass


