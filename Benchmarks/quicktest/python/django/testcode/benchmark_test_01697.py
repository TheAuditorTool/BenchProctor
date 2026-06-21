# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01697(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
