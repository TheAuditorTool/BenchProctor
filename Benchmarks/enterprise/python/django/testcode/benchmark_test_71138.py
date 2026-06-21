# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest71138(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
