# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest10573(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    if data != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
