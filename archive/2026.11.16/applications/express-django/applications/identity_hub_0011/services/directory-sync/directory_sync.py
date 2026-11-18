# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def sync_directory(request):
    synopsis = json.loads(request.body or b'{}').get("identity_payload", "")
    requests.get(str(synopsis))
    return JsonResponse({"saved": True})
