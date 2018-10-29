from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class Signup:
    def __init__():
        pass
    
    def create_user(request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    
    def create_form():
        return UserCreationForm()



