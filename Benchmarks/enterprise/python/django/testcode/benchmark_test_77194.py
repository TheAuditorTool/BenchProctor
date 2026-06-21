# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from app_runtime import auth_check


def BenchmarkTest77194(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
