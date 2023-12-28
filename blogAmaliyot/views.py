from django.shortcuts import render, redirect
from django.views import View
from .forms import UserProfileForm
from .models import PostUserInfo

class HomeView(View):
    def get(self, request):
        messages = PostUserInfo.objects.all()
        return render(request, 'home.html', {'messages': messages})

class MessageCreateView(View):
    def get(self, request):
        form = UserProfileForm()
        return render(request, 'base.html', {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'base.html', {'form': form})
