# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest57666(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    try:
        granted = auth_check('resource', str(data))
    except Exception:
        granted = True
    if not granted:
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
