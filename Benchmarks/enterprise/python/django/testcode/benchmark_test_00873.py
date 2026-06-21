# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest00873(request):
    raw_body = request.body.decode('utf-8')
    if not auth_check(request.session.get('user', ''), str(raw_body)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
