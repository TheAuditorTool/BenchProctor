# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def BenchmarkTest46647(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    auth_check('user', hashlib.sha256(str(ua_value).encode()).hexdigest())
    return JsonResponse({"saved": True})
