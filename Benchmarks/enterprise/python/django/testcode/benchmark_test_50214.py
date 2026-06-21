# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest50214(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
