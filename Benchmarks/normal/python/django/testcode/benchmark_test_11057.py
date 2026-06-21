# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest11057(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    auth_check('user', data)
    return JsonResponse({"saved": True})
