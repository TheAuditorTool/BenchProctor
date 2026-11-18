# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def route_alert(request):
    snippet = json.loads(request.body or b'{}').get("telemetry_payload", "")
    allowed = {'config.json', 'index.html', 'readme.md'}
    if snippet not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    cohort = '/var/app/data/' + snippet
    os.unlink(cohort)
    return JsonResponse({"saved": True})
