# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def enrich_stream(request):
    transcript = json.loads(request.body or b'{}').get('payload', '')
    rendition = (lambda v: v.strip())(transcript)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", rendition):
        return JsonResponse({'error': 'forbidden'}, status=400)
    montage = rendition
    with open('/var/app/data/' + str(montage), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
