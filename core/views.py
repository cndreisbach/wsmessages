from core.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    users = User.objects.all()
    return render(request, "homepage.html", {"users": users})


@login_required
def send_boop(request, recipient_pk):
    recipient = get_object_or_404(User, pk=recipient_pk)

    request.user.sent_boops.create(recipient=recipient)
    return redirect(to='homepage')
