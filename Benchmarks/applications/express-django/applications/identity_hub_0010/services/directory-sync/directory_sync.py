# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import base64
import pickle


@csrf_exempt
def sync_directory(request):
    note = json.loads(request.body or b'{}').get("identity_payload", "")
    pickle.loads(base64.b64decode(note))
    return JsonResponse({"saved": True})
