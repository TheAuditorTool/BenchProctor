# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def run_screening(request):
    phrase = json.loads(request.body or b'{}').get("risk_payload", "")
    requests.get(str(phrase))
    return JsonResponse({"saved": True})
