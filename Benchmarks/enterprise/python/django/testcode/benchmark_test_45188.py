# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def BenchmarkTest45188(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if not auth_check('user', hashlib.sha256(str(origin_value).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
