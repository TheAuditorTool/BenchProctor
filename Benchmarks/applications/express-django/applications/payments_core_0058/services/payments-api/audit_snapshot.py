# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def audit_snapshot(request):
    caption = json.loads(request.body or b'{}').get('payload', '')
    ledger = (lambda v: v.strip())(caption)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", ledger):
        return JsonResponse({'error': 'forbidden'}, status=400)
    remittance = ledger
    with open('/var/app/data/' + str(remittance), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
