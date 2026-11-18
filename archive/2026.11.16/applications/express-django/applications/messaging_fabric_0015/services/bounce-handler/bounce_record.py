# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def record_bounce(request):
    note = json.loads(request.body or b'{}').get("messaging_payload", "")
    requests.get(str(note))
    return JsonResponse({"saved": True})
