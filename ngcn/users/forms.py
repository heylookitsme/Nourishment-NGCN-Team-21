from django import forms
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

class AdminUserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label=_('password'),widget=forms.PasswordInput,min_length=8,max_length=30)
    password2 = forms.CharField(label=_('confirm your password'),widget=forms.PasswordInput,min_length=8,max_length=30)

    class Meta:
        model = User
        fields = ('username','email','location',)

        error_messages = {
			'email':{
				'unique':_("the giving email is taken"),
				'required':_("plase you have to write an email")
			},
			'username':{
				'unique':_('the giving username is taken'),
				'required':_('plase you have to write an username')
			}            
        }


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('two passwords must match')
        return password2

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class AdminUserUpdateForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ('username','email','location','password','active','staff','superuser')

        def clean_password(self):
            return self.initial["password"]



class RegisterForm(forms.ModelForm):
	password1 = forms.CharField(label=_('password'), widget=forms.PasswordInput,min_length=8,max_length=30)
	password2 = forms.CharField(label=_('confirm your password'), widget=forms.PasswordInput,min_length=8,max_length=30)
	class Meta:
		model = User
		fields = ('username','email','location',)
		error_messages = {
			'email':{
				'unique':_("the giving email is taken"),
				'required':_("plase you have to write an email")
			},
			'username':{
				'unique':_('the giving username is taken'),
				'required':_('plase you have to write an username')
			} 

		}

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password2 and password1 and password1 !=password2:
			return forms.ValidationError(_('two passwords must match'))

		return password2
	
	def save(self , commit=True):
		user = super(RegisterForm,self).save(commit=False)
		user.set_password(self.cleaned_data['password2'])
		user.active = True

		if commit:
			user.save()
		return user
	

class UpdateRegisterForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','location']

