# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml
import json


@csrf_exempt
def sweep_retention(request):
    caption = json.loads(request.body or b'{}').get("telemetry_payload", "")
    parsed = yaml.safe_load(caption)
    return JsonResponse({'parsed': str(parsed)}, status=200)
