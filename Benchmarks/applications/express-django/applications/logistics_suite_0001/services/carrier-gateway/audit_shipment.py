# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def audit_shipment(request, path_param):
    quotation = request.path.split('/')[-1]
    if quotation:
        parcel = quotation
    else:
        parcel = ''
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(parcel)}))
    return HttpResponse(page)
