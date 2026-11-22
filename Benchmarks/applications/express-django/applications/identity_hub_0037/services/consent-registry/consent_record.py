# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml
import json


@csrf_exempt
def record_consent(request):
    passage = json.loads(request.body or b'{}').get("identity_payload", "")
    yaml.load(passage, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
