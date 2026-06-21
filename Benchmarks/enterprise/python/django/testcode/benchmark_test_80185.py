# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest80185(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    auth_check('user', data)
    return JsonResponse({"saved": True})
