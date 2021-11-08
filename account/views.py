from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# def sign_up(request):
#     return render(request, 'account/signup.html')


def sign_up(request):
    form = UserCreationForm()
    print(form)
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:home')
        

    return render(request, 'account/signup.html', context={'form': form})    
