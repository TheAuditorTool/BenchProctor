# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def index_metadata(request):
    paragraph = json.loads(request.body or b'{}').get("media_payload", "")
    requests.get(str(paragraph))
    return JsonResponse({"saved": True})
