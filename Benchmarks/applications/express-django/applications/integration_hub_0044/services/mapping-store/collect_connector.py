# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import re


@csrf_exempt
def collect_connector(request):
    blurb = json.loads(request.body or b'{}').get('payload', '')
    if blurb:
        handshake = blurb
    else:
        handshake = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    citation = handshake
    return HttpResponse(mark_safe('<div>' + str(citation) + '</div>'))
