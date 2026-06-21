# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def BenchmarkTest77034(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not auth_check('user', hashlib.sha256(str(forwarded_ip).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
