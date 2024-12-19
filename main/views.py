from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Athlete, Ticket, Booking, Story
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    events = Event.objects.all()
    return render(request, 'main/home.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'main/event_detail.html', {'event': event})

def book_ticket(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        # Add booking logic
        pass
    return render(request, 'main/book_ticket.html', {'event': event})

def athlete_info(request):
    athletes = Athlete.objects.all()
    return render(request, 'main/athletes.html', {'athletes': athletes})

def stories(request):
    stories = Story.objects.all()  # Fetch all stories from the database
    return render(request, 'main/stories.html', {'stories': stories})

def events_list(request):
    events = Event.objects.all()  
    return render(request, 'main/events_list.html', {'events': events})

def athletes_list(request):
    athletes = Athlete.objects.all()  # Fetch all athletes from the database
    return render(request, 'main/athletes_list.html', {'athletes': athletes})

def about(request):
    return render(request, 'main/about.html')

def results(request):
    return render(request, 'main/results.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect('home')  # Redirect to a home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

def booking_view(request):
    if request.method == 'POST':
        # Process the form data here
        # You might want to save the data to your database
        # Redirect to a success page or render with a success message
        return redirect('booking_success')  # Assuming you have a success URL
    else:
        events = Event.objects.all()  # Fetch all events from your database
        return render(request, 'main/booking.html', {'events': events})