# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def BenchmarkTest00715(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
