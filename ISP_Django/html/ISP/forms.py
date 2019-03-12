from django import forms
from database.models import *
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    #name = forms.CharField(max_length=30)
    #date = forms.DateField()
    #start_time = forms.TimeField()
    #end_time = forms.TimeField()
    #event_type = forms.ChoiceField(choices=['Photo', 'Video', 'Booth', 'MTC'])
    #extra_info = forms.CharField(max_length=500)

    class Meta:
        model  = Event
        exclude = ['completed', 'assigned']



class SignupForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.EmailField()
    password = forms.CharField(max_length=32, min_length=5, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=32, min_length=5, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'repeat_password']

    def clean_repeat_password(self):
        password = self.cleaned_data.get('password',None)
        repeat_password = self.cleaned_data.get('repeat_password',None)

        if repeat_password and password:
            if password != repeat_password:
                msg = "The two password fields must match."
                raise forms.ValidationError(msg)
        return repeat_password
    
    def clean_username(self):
        username=self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            msg = "A user with that email already exists."
            raise forms.ValidationError(msg)
        return username

class LoginForm(forms.Form):
    username = forms.EmailField(widget= forms.EmailInput
                                (attrs={'class':'login',
				                'id':'login_username'}))
    password = forms.CharField(max_length=32, min_length=5, widget=forms.PasswordInput
                                (attrs={'class':'login',
				                'id':'login_pass'}))

    def clean_username(self):
        username=self.cleaned_data.get('username', None)
        password = self.cleaned_data.get('password', None)

        if username and password:
            if User.objects.filter(username=username).exists():
                if User.objects.filter(username=username).password == password:
                    return username
                msg = "Password is incorrect."
                raise forms.ValidationError(msg)
            msg = "User doesn't exist."
            raise forms.ValidationError(msg)
        return username
        