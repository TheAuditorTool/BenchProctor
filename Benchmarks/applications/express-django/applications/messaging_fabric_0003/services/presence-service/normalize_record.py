# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def normalize_record(request):
    subject = json.loads(request.body or b'{}').get('payload', '')
    bulletin = (lambda v: v.strip())(subject)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", bulletin):
        return JsonResponse({'error': 'forbidden'}, status=400)
    passage = bulletin
    with open('/var/app/data/' + str(passage), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
