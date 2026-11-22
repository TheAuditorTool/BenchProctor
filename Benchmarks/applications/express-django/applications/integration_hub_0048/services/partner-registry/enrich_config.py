# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def enrich_config(request, path_param):
    citation = request.path.split('/')[-1]
    if citation:
        handshake = citation
    else:
        handshake = ''
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(handshake)}))
    return HttpResponse(page)
