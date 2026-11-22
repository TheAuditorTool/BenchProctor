# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def apply_macro(request):
    subtitle = json.loads(request.body or b'{}').get("support_payload", "")
    requests.get(str(subtitle))
    return JsonResponse({"saved": True})
