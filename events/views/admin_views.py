from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Event, Category, User, Ticket, Feedback, Sponsor, Notification

# Quản lý danh sách sự kiện
def admin_event_list(request):
    events = Event.objects.all()
    return render(request, 'admin/event_list.html', {'events': events})

# Tạo sự kiện mới
def admin_event_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        location = request.POST['location']
        Event.objects.create(
            name=name,
            description=description,
            start_time=start_time,
            end_time=end_time,
            location=location
        )
        messages.success(request, 'Sự kiện được tạo thành công!')
        return redirect('admin_event_list')
    return render(request, 'admin/event_create.html')

# Xóa sự kiện
def admin_event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, 'Sự kiện đã bị xóa!')
    return redirect('admin_event_list')

# Quản lý người dùng
def admin_user_list(request):
    users = User.objects.all()
    return render(request, 'admin/user_list.html', {'users': users})

# Xem phản hồi của người dùng
def admin_feedback_list(request):
    feedbacks = Feedback.objects.select_related('event', 'user').all()
    return render(request, 'admin/feedback_list.html', {'feedbacks': feedbacks})