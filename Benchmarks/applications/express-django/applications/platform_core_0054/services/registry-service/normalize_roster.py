# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def normalize_roster(request):
    snippet = json.loads(request.body or b'{}').get('payload', '')
    persona = (lambda v: v.strip())(snippet)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", persona):
        return JsonResponse({'error': 'forbidden'}, status=400)
    handshake = persona
    with open('/var/app/data/' + str(handshake), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
