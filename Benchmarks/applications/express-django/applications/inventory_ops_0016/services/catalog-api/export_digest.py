# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def export_digest(request):
    citation = json.loads(request.body or b'{}').get('payload', '')
    backorder = (lambda v: v.strip())(citation)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", backorder):
        return JsonResponse({'error': 'forbidden'}, status=400)
    restock = backorder
    with open('/var/app/data/' + str(restock), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
