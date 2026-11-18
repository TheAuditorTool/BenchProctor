# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def archive_schedule(request):
    note = request.META.get('HTTP_AUTHORIZATION', '')
    if note:
        handshake = note
    else:
        handshake = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': handshake})))
