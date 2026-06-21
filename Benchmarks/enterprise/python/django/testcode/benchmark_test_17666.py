# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest17666(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    auth_check('user', data)
    return JsonResponse({"saved": True})
