# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def render_ledger(request):
    paragraph = json.loads(request.body or b'{}').get('payload', '')
    persona = (lambda v: v.strip())(paragraph)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", persona):
        return JsonResponse({'error': 'forbidden'}, status=400)
    synopsis = persona
    with open('/var/app/data/' + str(synopsis), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
