from django.contrib import admin
from django import forms

from .models import User


# Register your models here.
# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('email',)
#
#     def clean_password2(self): # validacijos metodas
#         cd = self.cleaned_data # cleaned_data - tai yra validuoti duomenys
#         if cd['password1'] != cd['password2']: # jei duomenys neatitinka
#             raise forms.ValidationError('Slaptažodžiai nesutampa.') # išmeta klaidą
#         return cd['password2'] # jei duomenys sutampa, grąžina duomenis
#
#     def save(self, commit=True): # save metodas
#         user = super(UserCreationForm, self).save(commit=False) # išsaugo duomenis
#         user.set_password(self.cleaned_data['password1']) # nustato slaptažodį
#         if commit: # jei commit yra True
#             user.save() # išsaugo duomenis į duomenų bazę per modelį User
#         return user # grąžina duomenis į formą
#
# class UserChangeForm(forms.ModelForm): # formos klasė kuri paveldi ModelForm ir ledžia redaguoti duomenis
#     password = forms.CharField(label='Password', widget=forms.PasswordInput) # slaptažodis
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'is_admin', 'is_employee') # laukai
#
#     def clean_password(self): # validacijos metodas patikrina ar slaptažodis yra teisingas
#         return self.initial['password'] # grąžina slaptažodį
#

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'id', 'is_admin', 'is_employee')
    list_filter = ('is_admin', 'is_employee')
    search_fields = ('email', 'id')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_employee')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin', 'is_employee')}
            ),
    )



admin.site.register(User, UserAdmin)
