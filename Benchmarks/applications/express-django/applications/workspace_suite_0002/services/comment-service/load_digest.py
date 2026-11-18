# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def load_digest(request):
    transcript = json.loads(request.body or b'{}').get('payload', '')
    heading = (lambda v: v.strip())(transcript)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", heading):
        return JsonResponse({'error': 'forbidden'}, status=400)
    passage = heading
    with open('/var/app/data/' + str(passage), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
