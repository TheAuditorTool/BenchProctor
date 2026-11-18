# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml
import json


@csrf_exempt
def append_audit(request):
    transcript = json.loads(request.body or b'{}').get("platform_payload", "")
    parsed = yaml.safe_load(transcript)
    return JsonResponse({'parsed': str(parsed)}, status=200)
