# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def normalize_config(request):
    footnote = json.loads(request.body or b'{}').get('payload', '')
    bulletin = (lambda v: v.strip())(footnote)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", bulletin):
        return JsonResponse({'error': 'forbidden'}, status=400)
    heading = bulletin
    with open('/var/app/data/' + str(heading), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
