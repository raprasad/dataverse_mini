from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from apps.dataverses.models import Dataverse


# Create your views here.
def show_dataverses(request):
    return render_to_response("dataverses/show_dataverses.html",
                          {'nodes':Dataverse.objects.all()},
                          context_instance=RequestContext(request))
