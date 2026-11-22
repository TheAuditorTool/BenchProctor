# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def index_document(request):
    note = json.loads(request.body or b'{}').get("documents_payload", "")
    requests.get(str(note))
    return JsonResponse({"saved": True})
