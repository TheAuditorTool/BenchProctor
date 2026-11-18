# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def build_changelog(request):
    tagline = json.loads(request.body or b'{}').get("delivery_payload", "")
    requests.get(str(tagline))
    return JsonResponse({"saved": True})
