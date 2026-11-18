# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml
import json


@csrf_exempt
def run_settlement(request):
    dunning = json.loads(request.body or b'{}').get("billing_payload", "")
    yaml.load(dunning, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
