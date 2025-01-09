from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Event, Ticket, Feedback, Notification

# Hiển thị danh sách sự kiện
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# Chi tiết sự kiện
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# Mua vé
@login_required
def ticket_purchase(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        # Tạo vé cho người dùng
        Ticket.objects.create(event=event, user=request.user)
        messages.success(request, "Ticket purchased successfully!")
        return redirect('event_detail', event_id=event_id)
    return render(request, 'events/ticket_purchase.html', {'event': event})

# Phản hồi sự kiện
@login_required
def event_feedback(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        Feedback.objects.create(event=event, user=request.user, rating=rating, comment=comment)
        messages.success(request, "Feedback submitted successfully!")
        return redirect('event_detail', event_id=event_id)
    return render(request, 'events/event_feedback.html', {'event': event})

# Thông báo của người dùng
@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'events/notifications.html', {'notifications': notifications})

# Đăng ký người dùng
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'events/register.html')

# Đăng nhập người dùng
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('event_list')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')

    return render(request, 'events/login.html')

# Đăng xuất người dùng
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('login')

# Đăng ký sự kiện
@login_required
def event_register(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        description = request.POST['description']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        location = request.POST['location']

        Event.objects.create(
            name=event_name,
            description=description,
            start_time=start_time,
            end_time=end_time,
            location=location
        )
        messages.success(request, "Event registered successfully!")
        return redirect('event_list')

    return render(request, 'events/event_register.html')
