# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import base64
from app_runtime import auth_check


def BenchmarkTest33229(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
