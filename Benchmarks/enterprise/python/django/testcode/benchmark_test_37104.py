# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest37104(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
