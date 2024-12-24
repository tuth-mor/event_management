from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Event, Ticket, Feedback, Notification

# Danh sách sự kiện
def event_list(request):
    events = Event.objects.all()
    return render(request, 'user/event_list.html', {'events': events})

# Chi tiết sự kiện
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'user/event_detail.html', {'event': event})

# Mua vé
def ticket_purchase(request, event_id):
    if request.method == 'POST':
        user = request.user  # Giả sử user đã đăng nhập
        event = get_object_or_404(Event, id=event_id)
        Ticket.objects.create(event=event, user=user)
        messages.success(request, 'Bạn đã mua vé thành công!')
        return redirect('event_list')

# Gửi đánh giá
def event_feedback(request, event_id):
    if request.method == 'POST':
        user = request.user
        event = get_object_or_404(Event, id=event_id)
        rating = request.POST['rating']
        comment = request.POST['comment']
        Feedback.objects.create(event=event, user=user, rating=rating, comment=comment)
        messages.success(request, 'Cảm ơn bạn đã đánh giá!')
        return redirect('event_detail', event_id=event_id)
    return render(request, 'user/event_feedback.html', {'event_id': event_id})

# Xem thông báo
def user_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'user/notifications.html', {'notifications': notifications})