from django.shortcuts import render

# Create your views here.

def voting_dashboard(request):
    return render(request, 'voting/dashboard.html')  
