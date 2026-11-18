# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml
import json


@csrf_exempt
def score_anomaly(request):
    heading = json.loads(request.body or b'{}').get("telemetry_payload", "")
    yaml.load(heading, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
