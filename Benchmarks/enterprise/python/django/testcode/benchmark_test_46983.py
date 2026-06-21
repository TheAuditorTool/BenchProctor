# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def BenchmarkTest46983(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    auth_check('user', hashlib.sha256(str(forwarded_ip).encode()).hexdigest())
    return JsonResponse({"saved": True})
