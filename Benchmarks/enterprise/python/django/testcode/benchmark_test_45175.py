# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest45175(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if not auth_check(request.session.get('user', ''), str(json_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
