# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest57345(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ensure_str(origin_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
