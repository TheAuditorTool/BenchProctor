# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
import bleach
from django.http import HttpResponse


@csrf_exempt
def load_policy(request):
    heading = request.META.get('HTTP_REFERER', '')
    if heading:
        handshake = heading
    else:
        handshake = ''
    persona = bleach.clean(handshake)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(persona) + '</div>')
    return resp
