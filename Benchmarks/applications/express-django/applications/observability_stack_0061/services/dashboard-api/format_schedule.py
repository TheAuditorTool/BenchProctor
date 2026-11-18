# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def format_schedule(request):
    headline = json.loads(request.body or b'{}').get('payload', '')
    cohort = (lambda v: v.strip())(headline)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", cohort):
        return JsonResponse({'error': 'forbidden'}, status=400)
    gauge = cohort
    with open('/var/app/data/' + str(gauge), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
