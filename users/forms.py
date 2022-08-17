from allauth.account.forms import LoginForm, SignupForm
from django import forms

class MyLoginForm(LoginForm):
    error_css_class = 'error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        # self.fields['login'].widget = forms.TextInput(
        #     attrs={
        #         'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
        #     })
        # self.fields['password'].widget = forms.PasswordInput(
        #     attrs={
        #         'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline'
        #     })
    

class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget = forms.TextInput(
        #     attrs={
        #         'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline'
        #     }
        # )
        # self.fields['email'].widget = forms.EmailInput(
        #     attrs={
        #         'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline'
        #     })
        # self.fields['password1'].widget = forms.PasswordInput(
        #     attrs={
        #         'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline'
        #     })
        # self.fields['password2'].widget = forms.PasswordInput(
        #     attrs={
        #         'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-2 leading-tight focus:outline-none focus:shadow-outline'
        #     })
    
    