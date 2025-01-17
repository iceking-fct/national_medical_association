from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .models import VotingSession, Candidate, Vote
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Count
from django.http import JsonResponse





# Custom LoginView with additional logic
class CustomLoginView(LoginView):
    template_name = 'users/login.html'  

    def form_valid(self, form):
        # Add a welcome message after successful login
        messages.success(self.request, f"Welcome back, {self.request.user.username}!")

        # Redirect users based on their roles
        user = self.request.user
        if user.is_staff:
            self.next_page = '/admin_dashboard/'  # Adjust this to your admin dashboard path
        elif user.groups.filter(name='Managers').exists():
            self.next_page = '/manager_dashboard/'  # Adjust this to your manager dashboard path
        else:
            self.next_page = '/voter_dashboard/'  # Adjust this to your voter dashboard path

        # Call the parent class's form_valid method to continue the login process
        return super().form_valid(form)
    

    # Optionally, if you want to add extra context to your template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_info'] = "Some extra context data if needed"
        return context




# Account Register View
def account_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, "There was an error creating your account. Please try again.")
    else:
        form = UserCreationForm()  # Display an empty form
    
    return render(request, 'users/register.html', {'form': form})



def account_logout(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page or any other page





'''
def vote(request, session_id):
    session = get_object_or_404(VotingSession, id=session_id)
    if not session.is_active:
        messages.error(request, "This voting session is no longer active.")
        return redirect('dashboard')  # Redirect to user dashboard

    if request.method == "POST":
        candidate_id = request.POST.get("candidate")
        if not candidate_id:
            messages.error(request, "Please select a candidate.")
            return redirect('vote', session_id=session_id)

        candidate = get_object_or_404(Candidate, id=candidate_id)
        try:
            # Ensure the user has not voted in this session
            Vote.objects.create(voter=request.user, candidate=candidate, session=session)
            messages.success(request, "Your vote has been cast successfully!")
        except:
            messages.error(request, "You have already voted in this session.")
        return redirect('dashboard')  # Redirect after voting

    # Fetch candidates for the voting session
    candidates = Candidate.objects.filter(session=session)
    return render(request, 'users/vote.html', {'session': session, 'candidates': candidates})
'''



def vote(request, session_id):
    if request.method == "POST":
        candidate_id = request.POST.get('candidate_id')
        try:
            session = VotingSession.objects.get(id=session_id)
            candidate = Candidate.objects.get(id=candidate_id, session=session)
            
            # Check if the user has already voted
            if Vote.objects.filter(voter=request.user, session=session).exists():
                return JsonResponse({'error': 'You have already voted in this session.'}, status=400)
            
            # Save the vote
            Vote.objects.create(voter=request.user, candidate=candidate, session=session)
            return JsonResponse({'success': 'Vote cast successfully!'})
        except (VotingSession.DoesNotExist, Candidate.DoesNotExist):
            return JsonResponse({'error': 'Invalid session or candidate.'}, status=400)


@login_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')

@login_required
def manager_dashboard(request):
    return render(request, 'users/manager_dashboard.html')

@login_required
def voter_dashboard(request):
    return render(request, 'users/voter_dashboard.html')



@login_required
def voting_results(request, session_id):
    try:
        session = VotingSession.objects.get(id=session_id)
        candidates = Candidate.objects.filter(session=session).annotate(vote_count=Count('vote'))

        return render(request, 'users/results.html', {'session': session, 'candidates': candidates})
    except VotingSession.DoesNotExist:
        messages.error(request, "Voting session not found.")
        return redirect('voter_dashboard')