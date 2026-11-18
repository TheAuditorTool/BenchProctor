# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def summarize_digest(request):
    caption = json.loads(request.body or b'{}').get('payload', '')
    gauge = (lambda v: v.strip())(caption)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", gauge):
        return JsonResponse({'error': 'forbidden'}, status=400)
    cohort = gauge
    with open('/var/app/data/' + str(cohort), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
