# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json


@csrf_exempt
def compact_record(request):
    remark = json.loads(request.body or b'{}').get('payload', '')
    inquiry = (lambda v: v.strip())(remark)
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", inquiry):
        return JsonResponse({'error': 'forbidden'}, status=400)
    grievance = inquiry
    with open('/var/app/data/' + str(grievance), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
