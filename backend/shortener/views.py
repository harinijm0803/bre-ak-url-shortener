from django.shortcuts import render, redirect, get_object_or_404
from .models import URL


def dashboard(request):
    urls = URL.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'urls': urls})


def create_page(request):
    return render(request, 'create.html')


def create_url(request):
    if request.method == "POST":
        original = request.POST.get("original_url")

        if original:
            URL.objects.create(original_url=original)

    return redirect("dashboard")


def delete_url(request, url_id):
    url = get_object_or_404(URL, id=url_id)
    url.delete()
    return redirect("dashboard")


def redirect_short(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.original_url)
