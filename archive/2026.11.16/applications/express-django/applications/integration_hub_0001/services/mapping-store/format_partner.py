# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def format_partner(request):
    quotation = request.META.get('HTTP_USER_AGENT', '')
    try:
        handshake = json.loads(quotation).get('value', quotation)
    except (json.JSONDecodeError, AttributeError):
        handshake = quotation
    with open('/var/app/data/' + str(handshake), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
