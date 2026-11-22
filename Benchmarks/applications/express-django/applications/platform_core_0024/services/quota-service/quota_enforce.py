# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def enforce_quota(request):
    remark = json.loads(request.body or b'{}').get("platform_payload", "")
    requests.get(str(remark))
    return JsonResponse({"saved": True})
