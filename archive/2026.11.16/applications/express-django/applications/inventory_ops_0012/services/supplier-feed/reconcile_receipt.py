# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def reconcile_receipt(request):
    phrase = request.META.get('HTTP_USER_AGENT', '')
    try:
        backorder = json.loads(phrase).get('value', phrase)
    except (json.JSONDecodeError, AttributeError):
        backorder = phrase
    with open('/var/app/data/' + str(backorder), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
