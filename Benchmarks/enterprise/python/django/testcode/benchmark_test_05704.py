# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest05704(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
