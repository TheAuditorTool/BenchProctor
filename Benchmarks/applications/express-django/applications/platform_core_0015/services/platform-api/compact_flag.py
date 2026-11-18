# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def compact_flag(request):
    note = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if note:
        handshake = note
    else:
        handshake = ''
    with open('/var/app/data/' + str(handshake), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
