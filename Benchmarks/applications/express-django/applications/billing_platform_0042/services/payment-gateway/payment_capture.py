# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def capture_payment(request):
    arrears = json.loads(request.body or b'{}').get("billing_payload", "")
    requests.get(str(arrears))
    return JsonResponse({"saved": True})
