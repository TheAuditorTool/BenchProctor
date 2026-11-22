# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse


@csrf_exempt
def audit_secret(request):
    remark = request.META.get('HTTP_REFERER', '')
    if remark:
        persona = remark
    else:
        persona = ''
    handshake = bleach.clean(persona)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(handshake) + '</div>')
    return resp
