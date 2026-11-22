# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse


@csrf_exempt
def collect_label(request):
    quotation = request.META.get('HTTP_REFERER', '')
    if quotation:
        parcel = quotation
    else:
        parcel = ''
    consignment = bleach.clean(parcel)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(consignment) + '</div>')
    return resp
