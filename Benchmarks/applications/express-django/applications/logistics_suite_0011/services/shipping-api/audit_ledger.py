# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse


@csrf_exempt
def audit_ledger(request):
    citation = request.META.get('HTTP_REFERER', '')
    if citation:
        consignment = citation
    else:
        consignment = ''
    parcel = bleach.clean(consignment)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(parcel) + '</div>')
    return resp
