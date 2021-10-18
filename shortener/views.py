from django.http.response import Http404
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import ShortUrl,Visit
from .forms import ShortenerForm
from .utils import create_alias
from django.contrib.gis.geoip2 import GeoIP2
def home_view(request):
    """
    Renders the index page which has the shortener form.
    """
    form = ShortenerForm()
    return render(request, 'app.html', {'form': form})

def redirect_view(request, alias):
    """
    Renders the redirect page of given alias. 
    Increments the `visits` field in the database by one.
    If alias is not exist in database, will redirect to root.
    """
    try:
        short = ShortUrl.objects.get(alias=alias)
        short.number_of_visits+=1
        #detect geoloc
        g=GeoIP2()
        IP_address=request.META["REMOTE_ADDR"]
        try:
            country_code=g.country(IP_address)["country_code"]
        except :
            country_code="localhost"
        #detect device
        os=request.user_agent.os.family 
        short.visits.create(country=IP,os=os)
        
        short.save()
        page_data = {
            'redirect_url': short.long_url,
        }
        return render(request, 'redirect.html', {'page_data': page_data})
    except ShortUrl.DoesNotExist:
        pass
    return HttpResponseRedirect('/')

def shorten_url(request):
    """
    Shorten given URL with an alias.
    Alias field in the form is optional. If it's blank, will be created randomly.
    Returns json response of the process state.
    """
    if request.method == 'POST':
        form = ShortenerForm(request.POST)
        if form.is_valid():
            alias = form.cleaned_data.get('alias')
            long_url = form.cleaned_data.get('long_url')
            if not alias:
                alias = create_alias()
            try:
                short = ShortUrl(alias=alias, long_url=long_url)
                short.save()
                return JsonResponse({
                    'status': 'success',
                    'message': 'Successfully shortened!',
                    'result': alias
                })
            except IntegrityError:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Given alias already exists.'
                })
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid fields!'
        })
    return HttpResponseRedirect('/')
