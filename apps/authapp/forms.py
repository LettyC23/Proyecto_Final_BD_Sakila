from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password'}))

class RegistrationForm(forms.Form):
    firstname = forms.RegexField(label='Enter Regex', label_suffix=" : ",
                             regex=r'^[a-zA-Z]+$',
                             required=True,
                             help_text="Please enter regex format should be[a-z, A-Z]", disabled=False,
                             error_messages={'required': "Please enter regex"})
    lastname = forms.RegexField(label='Enter Regex', label_suffix=" : ",
                             regex=r'^[a-zA-Z]+$',
                             required=True,
                             help_text="Please enter regex format should be[a-z, A-Z]", disabled=False,
                             error_messages={'required': "Please enter regex"})
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password'}))