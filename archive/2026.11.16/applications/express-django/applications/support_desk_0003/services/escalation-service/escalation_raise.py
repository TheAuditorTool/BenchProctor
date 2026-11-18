# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def raise_escalation(request):
    excerpt = json.loads(request.body or b'{}').get("support_payload", "")
    with open('/var/app/data/' + str(excerpt), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
