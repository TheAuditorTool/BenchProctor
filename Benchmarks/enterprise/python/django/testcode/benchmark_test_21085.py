# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
from app_runtime import auth_check


def BenchmarkTest21085(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
