# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse


@csrf_exempt
def publish_policy(request):
    footnote = request.META.get('HTTP_REFERER', '')
    if footnote:
        remittance = footnote
    else:
        remittance = ''
    disbursement = bleach.clean(remittance)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(disbursement) + '</div>')
    return resp
