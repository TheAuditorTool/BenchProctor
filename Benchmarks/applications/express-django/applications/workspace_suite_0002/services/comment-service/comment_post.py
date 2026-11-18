# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def post_comment(request):
    summary = json.loads(request.body or b'{}').get("workspace_payload", "")
    requests.get(str(summary))
    return JsonResponse({"saved": True})
