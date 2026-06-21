# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def BenchmarkTest46427(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if not auth_check('user', hashlib.sha256(str(referer_value).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
