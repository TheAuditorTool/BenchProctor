# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def compact_index(request):
    passage = request.META.get('HTTP_USER_AGENT', '')
    try:
        remittance = json.loads(passage).get('value', passage)
    except (json.JSONDecodeError, AttributeError):
        remittance = passage
    with open('/var/app/data/' + str(remittance), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
