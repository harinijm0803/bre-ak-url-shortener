from django.shortcuts import redirect, render
from .models import URL
import random, string

def delete_url(request, url_id):
    url = get_object_or_404(URL, id=url_id)
    url.delete()
    return redirect('dashboard')
def dashboard(request):
    urls = URL.objects.all()
    return render(request, 'dashboard.html', {'urls': urls})

def create(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        # Generate short code
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        url_obj = URL(original_url=original_url, short_code=short_code, click_count=0)
        url_obj.save()
        return redirect('dashboard')
    return render(request, 'create.html')

def redirect_url(request, short_code):
    try:
        url_obj = URL.objects.get(short_code=short_code)
        url_obj.click_count += 1
        url_obj.save()
        return redirect(url_obj.original_url)
    except URL.DoesNotExist:
        return redirect('dashboard')
