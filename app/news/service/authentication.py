from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class Signup:
    def __init__(self):
        pass
    
    def create_user(self, form):
        form.save()
    
    def create_form(self):
        return UserCreationForm()
    
    def login_user(self, form, request):
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)




