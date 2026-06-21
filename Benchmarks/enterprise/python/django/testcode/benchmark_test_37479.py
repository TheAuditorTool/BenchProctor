# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
from app_runtime import auth_check


def BenchmarkTest37479(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
