from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    # {'form': form}の'form'はhtmlに送るパラメータで、formは
    #　form = UserCreationForm()のform（オブジェクト）
    return render(request, 'account/signup.html', {'form': form})